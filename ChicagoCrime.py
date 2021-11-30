# Python standard library
import csv, webbrowser, os, sys
from random import randint

# PIP3 packages
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import numpy as np
import gmplot

# Our own code
from avl import AVLTree, CrimeData, AVLTreeNode
from heap import MinHeap

test_fn = sys.argv[1] if len(sys.argv) > 1 else ""

TRAIN_FILE = "Chicago_Crimes_2018-2019_Train.csv" if test_fn == "" else test_fn

print("Using dataset:" + TRAIN_FILE)

API_KEY = "AIzaSyC5DbWswLfC0oLuFLe8ZhSOfOL5VkCsJ60"
s = os.sep


class ChicagoCrimeFun:
    def __init__(self):
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

        # https://docs.python.org/3/library/csv.html
        with open(TRAIN_FILE, newline="") as csvfile:
            csvreader = csv.reader(csvfile)  # read in the file, split it into a list.
            for lines in csvreader:
                self.data.append(lines)

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

        # first "crime" is just the header
        self.total_crimes -= 1

        print("Total data points: " + str(self.total_crimes))

    def do_sort(self, x):
        return {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

    def build_loc_priority(self):
        """
        Should be used to build your location-priority AVL tree
        """
        for cd in self.cds:
            if (
                cd.primary_type in self.priority_dict
                and self.priority_dict[cd.primary_type] != None
            ):
                location_node = AVLTreeNode(
                    cd.location, self.priority_dict[cd.primary_type]
                )
                self.type_tree.insert(location_node)
            else:
                print("Ignoring data point w/ primary type: " + cd.primary_type)

    def build_crime_priority(self):
        """
        Should be used to build your location-priority AVL tree
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

    def add_random_case(self, n):
        with open(TRAIN_FILE) as f:
            lines = f.readlines()
        for i in range(n):
            self.add_dispatch(lines[randint(0, len(lines))])

    def add_dispatch(self, dispatch_string):
        '''
        Method to add a dispatch to our dispatch_queue
        Parameters:
            dispatch_string: [string] A string that represents a recent 911 dispatch call request that is reported to the police
        '''
        csv = dispatch_string.split(",")
        primary_type = csv[5]
        if primary_type in self.priority_dict:
            priority = self.priority_dict[primary_type]
            self.dispatch_queue.insert(priority, dispatch_string)
        else:
            print("Couldn't lookup primary type: " + primary_type)
            sys.exit(1)

    def dump_next(self):
        if not self.dispatch_queue.is_empty():
            print(self.dispatch_queue.remove())
        else:
            print("Nothing to dump")

    def decide_next_patrol(self, new_request=None):
        '''
        Used to decide next place to send patrol
        Parameters:
            new_request: [string][optional] A string that represents a 911 dispatch call that is reported to the police
        Returns:
            [tuple] A tuple of length 4 that represents the 4 points of an area to patrol.
        '''
        pass

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
        fn = "maps" + s + otype + "-" + str(randint(1, 1000)) + ".html"
        gmap4.draw(fn)
        if browser:
            webbrowser.open_new_tab(fn)

    def map_all_types(self):
        for primary in self.primary_types:
            print("Making map for " + primary)
            self.google_maps(otype=primary, browser=False)

if __name__ == "__main__":
    print("1 - Loading data")
    ccf = ChicagoCrimeFun()

    print("2 - Building location tree")
    ccf.build_loc_priority()
    print("3 - Loading type priority tree")
    ccf.build_crime_priority()

    print("4 - Adding random cases")
    ccf.add_random_case(10000)
    print("5 - testing highest priority report")
    ccf.dump_next()