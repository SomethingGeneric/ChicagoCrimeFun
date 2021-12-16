# Python standard library
import csv, webbrowser, os, sys
from random import randint

# PIP3 packages
# import matplotlib
# import matplotlib.pyplot as plt
# import networkx as nx
# from networkx.drawing.nx_agraph import graphviz_layout
# import numpy as np
import gmplot
from colorama import init
from termcolor import colored

init()

# Our own code
from avl import AVLTree, CrimeData, AVLTreeNode
from heap import MinHeap
from visualize import VisualizeData


test_fn = sys.argv[1] if len(sys.argv) > 1 else ""

TRAIN_FILE = "datasets" + os.sep + "Chicago_Crimes_Test.csv" if test_fn == "" else test_fn

print("Using dataset:" + TRAIN_FILE)

API_KEY = "AIzaSyC5DbWswLfC0oLuFLe8ZhSOfOL5VkCsJ60"
s = os.sep


def print_error(something):
    print(colored(something, "red"))


def print_warn(something):
    print(colored(something, "yellow"))


def print_info(something):
    print(colored(something, "cyan"))


class payload:
    def __init__(self, key, value, points=None, label="", ds=""):
        self.key = key
        self.value = value
        self.points = points
        self.label = label
        self.ds = ds


class ChicagoCrimeFun:
    def __init__(self, filename=TRAIN_FILE, scaling_factor=0.0001):
        """
        Constructor that could do several things, including read in your training data
        """
        self.data = []
        self.cds = []
        self.primary_types = []
        self.total_crimes = 0

        self.location_tree = AVLTree()
        self.type_tree = AVLTree()

        self.dispatch_queue = MinHeap()

        self.crime_priority_list = []

        self.scaling_factor = scaling_factor

        # https://docs.python.org/3/library/csv.html
        with open(filename, newline="") as csvfile:
            csvreader = csv.reader(csvfile)  # read in the file, split it into a list.
            for lines in csvreader:
                if "IUCR" not in lines:
                    self.data.append(lines)
                else:
                    print_warn("Ignoring lines: " + str(lines))

        # load our list of crimes, where the top is the "worst"
        # or most severe (there is a lot of bias here :(  )
        self.priority_dict = {}
        l = 0
        with open("primary_types.txt") as f:
            for line in f.read().split("\n"):
                self.priority_dict[line] = l
                l += 1

        self.priority_dict["Primary Type"] = None

        # Create instance of crime data, then nodes
        for case in self.data:
            self.total_crimes += 1
            tc = CrimeData(case)
            self.cds.append(tc)

        print_info("Total data points: " + str(self.total_crimes))

    def do_sort(self, x):
        return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

    def build_loc_priority(self, graphIt=False):
        """
        Should be used to build your location-priority AVL tree
        """
        for cd in self.cds:
            if (
                cd.primary_type in self.priority_dict
                and self.priority_dict[cd.primary_type] != None
            ):
                location_node = AVLTreeNode(
                    cd.beat, self.priority_dict[cd.primary_type]
                )
                self.location_tree.insert(location_node)
            else:
                print("Ignoring data point w/ primary type: " + cd.primary_type)

        if graphIt:
            # Visualize the data
            v = VisualizeData()
            dot = v.visualize_data(self.location_tree)
            dot.format = "png"
            dot.strict='true'
            dot.compound='true'
            dot.view(filename="location_tree", directory="./visualizations/")

    # Function that creates the crime priority.
    def build_crime_priority(self, graphIt=False):
        """
        Should be used to build your crime type-priority AVL tree
        """

        for cd in self.cds:
            if cd.primary_type in self.priority_dict:
                type_node = AVLTreeNode(
                    cd.primary_type, self.priority_dict[cd.primary_type]
                )
                self.type_tree.insert(type_node)
            else:
                print(
                    "I've never seen primary type: "
                    + cd.primary_type
                    + " before!!! Failing."
                )
                sys.exit(1)

        if graphIt:
            v = VisualizeData()
            dot = v.visualize_data(self.type_tree)
            dot.format = "png"
            dot.strict = True
            dot.view(filename="type_tree", directory="./visualizations/")

    def add_random_case(self, n):
        used = []
        with open(TRAIN_FILE) as f:
            lines = f.readlines()
        for i in range(n):
            index = randint(0, len(lines) - 1)
            while index in used:
                index = randint(0, len(lines) - 1)
            used.append(index)
            self.add_dispatch(lines[index])

    def add_dispatch(self, dispatch_string):
        """
        Method to add a dispatch to our dispatch_queue
        Parameters:
            dispatch_string: [string] A string that represents a recent 911 dispatch call request that is reported to the police
        """
        if not "," in dispatch_string:
            print_warn("That's not a proper string!")
        else:
            csv = dispatch_string.split(",")
            if len(csv) < 6:
                print_warn("You're missing attributes!")
            else:
                primary_type = csv[5]
                if primary_type in self.priority_dict:
                    priority = self.priority_dict[primary_type]
                    self.dispatch_queue.insert(priority, dispatch_string)
                else:
                    print_warn(
                        "Couldn't lookup primary type: "
                        + primary_type
                        + ", so we're assigning it a priority of 0 (MOST URGENT"
                    )
                    self.dispatch_queue.insert(0, dispatch_string)

    def dump_next(self):
        if not self.dispatch_queue.is_empty():
            print_info(self.dispatch_queue.peek())
        else:
            print_warn("Nothing to dump")

    def construct_crime_priority_list(self):
        """
        Construct a list of crime types, sorted by priority
        """
        for crime in self.priority_dict.keys():
            print_info("Indexing all " + crime)
            temp_list = []
            for cd in self.cds:
                if cd.primary_type == crime:
                    temp_list.append(cd)

            print_info("There are " + str(len(temp_list)) + " " + crime + "s")

            if len(temp_list) > 1:
                first = temp_list[-2]
                x1, y1 = float(first.latitude), float(first.longitude)

                second = temp_list[-1]
                x2, y2 = float(second.latitude), float(second.longitude)

                box = (
                    "(("
                    + str(x1)
                    + ", "
                    + str(y1)
                    + "), ("
                    + str(x2)
                    + ", "
                    + str(y2)
                    + "), ("
                    + str(x1)
                    + ", "
                    + str(y2)
                    + "), ("
                    + str(x2)
                    + ", "
                    + str(y1)
                    + "))"
                )

                points = ([x1, x2, x2, x1], [y1, y1, y2, y2])

                p = payload(self.priority_dict[crime], box, points, label=crime)
                self.crime_priority_list.append(p)
            else:
                print_warn("Not enough data points to extrapolate " + crime)

    def gmap_make(self, data, marker_text="", filename="map.html"):
        """
        Construct a map of the data using the Google Maps API
        """
        lats, longs = data
        gmap4 = gmplot.GoogleMapPlotter(lats[0], longs[0], 100, apikey=API_KEY)
        gmap4.polygon(lats, longs, color="cornflowerblue", title=marker_text)
        gmap4.draw(filename)

    def point_to_box(self, x1, y1):

        if x1 == "" or y1 == "":
            return None

        x1 = float(x1)
        y1 = float(y1)

        x2 = x1 + float(self.scaling_factor)
        y2 = y1 + float(self.scaling_factor)

        return ([x1, x2, x2, x1], [y1, y1, y2, y2])

    def store_ds(self, ds):
        """
        Store the dispatch string for flask
        """
        with open("dispatch_history.txt", "a+") as f:
            f.write(ds + "\n\n")

    def mark_pred(self):
        """
        We're bodging. This dotfile indicates that the last dispatch was not based on an exact call,
        but rather our guess as to where it's worth sending a patrol preemptively.
        """
        os.system("touch .pred")

    def decide_next_patrol(
        self, new_request=None, map_it=False, filename="map.html", log_it=False
    ):
        """
        Used to decide next place to send patrol
        Parameters:
            new_request: [string][optional] A string that represents a 911 dispatch call that is reported to the police
        Returns:
            [tuple] A tuple of length 4 that represents the 4 points of an area to patrol.
        """

        print_warn("-- DECIDING PATROL --")
        print_warn("New request: " + str(new_request))
        print_warn("Mapping: " + str(map_it))
        if map_it:
            print_warn("Map FN: " + filename)
        print_warn("Logging: " + str(log_it))

        if new_request is None:
            print_warn("We have no new request")
            if self.dispatch_queue.is_empty():
                # Now we need to use some past data to make best use of our resources
                if self.crime_priority_list == []:
                    self.construct_crime_priority_list()

                payload = self.crime_priority_list[0]
                self.crime_priority_list.pop(0)

                if map_it:
                    self.gmap_make(payload.points, filename)

                if log_it:
                    self.store_ds(
                        "Dispatched patrol to "
                        + str(payload.points)
                        + " since we predict "
                        + payload.label
                    )
                    self.mark_pred()

                return payload.value
            else:
                # we have an existing call, hence we need to do something *right now*
                print_warn("we had a call in the queue, let's respond to that")
                prio, recent_call = self.dispatch_queue.remove()

                 # ah yes. to list or not to list, that is the question. (thanks CSV module!)
                attrs = csv.reader([recent_call]).__next__()

                x1 = attrs[19]
                y1 = attrs[20]

                data = self.point_to_box(x1, y1)

                if data is not None:
                    if map_it:
                        self.gmap_make(
                            data,
                            filename,
                        )
                    if log_it:
                        self.store_ds(recent_call)
                    return data
                else:
                    return "No location data"
        else:
            # we have a new call, but is it more important than the previous one?
            print_info(
                "We have a new call, let's decide if we should respond to it or the existing one in queue"
            )

            if not "," in new_request or len(csv.reader([new_request]).__next__()) != 22:
                print_error(
                    "Something is wonky with this new request. Y'all should probably get on it.\n"
                )
                print_error("Here's the raw data: " + new_request)
                print_error("Here's the n of attrs: " + str(len(csv.reader([new_request]).__next__())))
                return "EMERGENCY:" + new_request
            else:

                if not self.dispatch_queue.is_empty():
                    my_priority = self.priority_dict[csv.reader([new_request]).__next__()[5]]
                    prio, recent_call = self.dispatch_queue.peek()

                    print("My prio: " + str(my_priority))
                    print("Other prio: " + str(prio))

                    if my_priority < prio:
                        # this new request is more important than the other one.
                        print_info("responding to the new call")

                        # ah yes. to list or not to list, that is the question. (thanks CSV module!)
                        attrs = csv.reader([new_request]).__next__()

                        x1 = attrs[19]
                        y1 = attrs[20]

                        data = self.point_to_box(x1, y1)

                        if data is not None:
                            if map_it:
                                self.gmap_make(
                                    data,
                                    filename,
                                )
                            if log_it:
                                self.store_ds(new_request)
                            return data
                        else:
                            return "No location data"
                    else:
                        # new request is less important than the last one
                        print_info("responding to the existing call")
                        # we don't need to save this output since we defined it above w/ the peek call
                        self.dispatch_queue.remove()
                        # let's also add the new call that we're ignoring *for now*
                        self.dispatch_queue.insert(new_request)

                        # ah yes. to list or not to list, that is the question. (thanks CSV module!)
                        attrs = csv.reader([recent_call]).__next__()

                        x1 = attrs[19]
                        y1 = attrs[20]

                        data = self.point_to_box(x1, y1)

                        if data is not None:
                            if map_it:
                                self.gmap_make(
                                    data,
                                    filename,
                                )
                            if log_it:
                                self.store_ds(recent_call)
                            return data
                        else:
                            return "No location data"

                else: # dispatch queue is empty
                    print_info("Responding to incoming call. Dispatch queue empty.")
                    # ah yes. to list or not to list, that is the question. (thanks CSV module!)
                    attrs = csv.reader([new_request]).__next__()

                    x1 = attrs[19]
                    y1 = attrs[20]

                    data = self.point_to_box(x1, y1)

                    if data is not None:
                        if map_it:
                            self.gmap_make(
                                data,
                                filename,
                            )
                        if log_it:
                            self.store_ds(new_request)
                        return data
                    else:
                        return "No location data"


        return "default case?"

    def google_maps(self, otype="THEFT", browser=True):
        """
        Generate HTML google maps of data
        """
        if not os.path.exists("maps"):
            os.makedirs("maps")
        latitudes = []
        longitudes = []
        self.data.pop(0)
        for item in self.data:
            if item.primary_type == otype:
                if item.latitude != "":
                    latitudes.append(float(item.latitude))
                if item.longitude != "":
                    longitudes.append(float(item.longitude))
        gmap4 = gmplot.GoogleMapPlotter.from_geocode("Chicago, IL", apikey=API_KEY)
        gmap4.heatmap(latitudes, longitudes)
        fn = "heatmaps" + s + otype + "-" + str(randint(1, 1000)) + ".html"
        gmap4.draw(fn)
        if browser:
            webbrowser.open_new_tab(fn)

    def map_all_types(self):
        for primary in self.primary_types:
            print_info("Making map for " + primary)
            self.google_maps(otype=primary, browser=False)


if __name__ == "__main__":
    print_info("1 - Loading data")
    ccf = ChicagoCrimeFun()

    print_info("2 - Building location tree")
    ccf.build_loc_priority(graphIt=True)
    print_info("3 - Loading type priority tree")
    ccf.build_crime_priority(graphIt=True)

    print_info("4 - Adding random cases")
    ccf.add_random_case(20)

    # print_info("5 - testing highest priority report")
    # ccf.dump_next()

    print_info("6 - Deciding next patrol location")
    print_info("Output: " + str(ccf.decide_next_patrol(map_it=True)))
    webbrowser.open_new_tab("map.html")
