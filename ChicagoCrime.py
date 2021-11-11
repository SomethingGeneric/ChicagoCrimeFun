TRAIN_FILE = "Chicago_Crimes_2018-2019_Train.csv"


class ChicagoCrimeFun:
    def __init__(self):
        """
        Constructor that could do several things, including read in your training data
        """
        with open(TRAIN_FILE) as file:
            lines = file.read().split("\n")  # read in the file, split it into a list. 
        
        for line in lines:
            print(line)
            
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


if __name__ == "__main__":
    ccf = ChicagoCrimeFun()
