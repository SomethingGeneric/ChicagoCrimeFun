# Python standard library
import csv, webbrowser, os
from random import randint

# PIP3 packages
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import gmplot

# Our own code
from adt import CrimeData, CrimeNode

TRAIN_FILE = "Chicago_Crimes_2018-2019_Train.csv"
API_KEY = "AIzaSyC5DbWswLfC0oLuFLe8ZhSOfOL5VkCsJ60"
s = os.sep

class ChicagoCrimeFun:
    def __init__(self):
        """
        Constructor that could do several things, including read in your training data
        """
        self.root = None

        self.data = []

        self.primary_types = []
        
        data = []

        # https://docs.python.org/3/library/csv.html
        with open(TRAIN_FILE, newline='') as csvfile:
            csvreader = csv.reader(csvfile)  # read in the file, split it into a list.
            for lines in csvreader:
                data.append(lines)

        # Create instance of crime data, then nodes
        for case in data:
            data = CrimeData(case)
            self.data.append(data)
            new_node = CrimeNode()
            new_node.value = data
            new_node.key = data.location

            if data.primary_type not in self.primary_types:
                self.primary_types.append(data.primary_type)

        # item 0 is the label :(
        self.primary_types.pop(0)
        #print(str(self.primary_types))
            
    def build_loc_priority(self):
        """
        Should be used to build your location-priority AVL tree
        """
        pass

    def build_crime_priority(self):
        """
        Should be used to build your location-priority AVL tree
        """
        pass

    def decide_next_patrol(self, new_request=None):
        """
        You will need this later, but I'm just giving this here for you to keep it as a placeholder
        """

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
        fn = "maps" + s + otype + "-" + str(randint(1,1000))+".html"
        gmap4.draw(fn)
        if browser:
            webbrowser.open_new_tab(fn)

    def map_all_types(self):
        for primary in self.primary_types:
            print("Making map for " + primary)
            self.google_maps(otype=primary, browser=False)

if __name__ == "__main__":
    ccf = ChicagoCrimeFun()
    ccf.map_all_types()