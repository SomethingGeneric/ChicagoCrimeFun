from ChicagoCrimeFun import *
import queue


class ChicagoCrimeTest:
    """
    Class to test 204 ChicagoCrime Project
    By Chris Dancy, Assistant Professor, Dept of Computer Science
    last modified 2021-Dec-11
    """

    NUM_TEST_ENTRIES = 10
    NUM_EMPTY_DECISIONS = 10

    def __init__(self, test_dispatch_file="Chicago_Crimes_Test.csv"):
        self._dispatch_file = open(test_dispatch_file, "r")
        # We don't need the header line
        self._dispatch_file.readline()

        print("+++++Creating chicago crime object++++")
        # You may have to modify this
        self.__chicago_crime_obj = ChicagoCrimeFun("Chicago_Crimes_Test.csv")

        self.__chicago_crime_obj.build_loc_priority()
        self.__chicago_crime_obj.build_crime_priority()

        print("---Finished creating object---")

        # We'll use this to make sure your priority queue acts as it should
        self.__test_queue = queue.PriorityQueue()

    def test_add_dispatch(self, test_decision=False, num_items=None):
        print("#------------#")
        print('Let\'s test your "add_dispatch" method!')
        print("Adding items to dispatch_queue")

        # We can use either use our class constant to determine how many items to test, or what is entered into the num_items parameter
        if num_items is None:
            num_items = ChicagoCrimeTest.NUM_TEST_ENTRIES
        for i in range(num_items):
            # Get dispatch string, then split it and remove last item (not needed)
            #  Lastly, convert back to a string
            dispatch = self._dispatch_file.readline()
            dispatch = dispatch.rstrip()
            dispatch = dispatch.split(",")
            dispatch = dispatch[0 : len(dispatch) - 1]
            dispatch = ",".join(dispatch)

            # You probably will have to change what is enqueued
            print("++++")
            print('Adding "+' + dispatch + '+" with priority ' + str(i))
            self.__chicago_crime_obj.add_dispatch(_DispNode(i, dispatch))
            # self.__chicago_crime_obj.add_dispatch(dispatch)
            # May need to use crime_obj instance get priority here
            self.__test_queue.put((i, dispatch))
            print("++++")

        print(
            'If you see an error, you may not have a method called "get_dispatch_queue" to get your queue'
        )
        if not test_decision:
            for i in range(num_items):
                print("-----")
                print("You should see - " + str(self.__test_queue.get()))
                print("")
                print(
                    "Your priority queue returned - "
                    + self.__chicago_crime_obj.get_dispatch_queue().dequeue()
                )
                print("-----")
        else:  # Empty out test queue
            for i in range(num_items):
                self.__test_queue.get()

    def test_decide_next_patrol(self, num_decisions=None):
        print("#------------#")
        print("Let's test the decisions you make!")
        print(
            'First we\'ll see how your "decide_next_patrol" method does without having anything in the queue AND without any requests'
        )

        if num_decisions is None:
            num_decisions = ChicagoCrimeTest.NUM_EMPTY_DECISIONS

        for i in range(num_decisions):
            print("-----")
            print("Requesting new patrol (number - " + str(i) + ")....")
            print(
                "We're going to send the next patrol out to : "
                + str(self.__chicago_crime_obj.decide_next_patrol())
            )
            print("-----")

        print(
            "Now, let's add some stuff to your queue & see if we can use that to determine the next patrol (you should see some differences this time with the queue being available to help the decision)"
        )
        self.test_add_dispatch(True, num_decisions)

        for i in range(num_decisions):
            print("+++++")
            print("Requesting new patrol (number - " + str(i) + ")....")
            print(
                "We're going to send the next patrol out to : "
                + self.__chicago_crime_obj.decide_next_patrol()
            )
            print("+++++")

        # Empty out priority queue
        print("If this errors out, you probably don't have a working is_empty() method")
        while not self.__chicago_crime_obj.get_dispatch_queue().is_empty():
            self.__chicago_crime_obj.get_dispatch_queue().dequeue()

        print("Lastly, let's try to get some decisions with a dispatch as a parameter")

        for i in range(num_decisions):
            # We interweave testing the decision with a dispatch parameter
            if (i % 3) == 0:
                print("-----")
                print("Requesting new patrol (number - " + str(i) + ")....")
                print(
                    "We're going to send the next patrol out to : "
                    + self.__chicago_crime_obj.decide_next_patrol()
                )
                print("-----")
            else:
                # Get dispatch string, then split it and remove last item (not needed)
                #  Lastly, convert back to a string
                dispatch = self._dispatch_file.readline()
                dispatch = dispatch.rstrip()
                dispatch = dispatch.split(",")
                dispatch = dispatch[0 : len(dispatch) - 1]
                dispatch = ",".join(dispatch)
                print("+++++")
                print("Requesting new patrol (number - " + str(i) + ")....")
                print(
                    "We're going to send the next patrol out to : "
                    + self.__chicago_crime_obj.decide_next_patrol(dispatch)
                )
                print("+++++")

        print("Testing decisions complete!")
        print("#------------#")

    def test_crime_priority_list(self):
        print("#------------#")
        print('Let\'s test how well your "crime_priority_list" attribute works!')
        print(
            "If you used an object to encapsulate the payload (key & value), you'll need to override __repr__ or __str__ method for this to be helpful"
        )

        # Go through list and print out each payload
        for i in range(
            10
        ):  # for i in range(len(self.__chicago_crime_obj.get_crime_priority_list())):
            print("-----")
            print("We probably should be at priority - " + str(i))
            print(
                "This item has the following payload - "
                + str(self.__chicago_crime_obj.get_crime_priority_list())
            )
            print("-----")

        print('Test of "test_crim_priority_list" Complete')
        print("#------------#")

    def close_dispatch_file(self):
        self._dispatch_file.close()


class _DispNode:
    def __init__(self, priority=0, disp_string="test0"):
        self.priority = priority
        self.disp_string = disp_string


test_obj = ChicagoCrimeTest()
test_obj.test_decide_next_patrol()
# test_obj.test_add_dispatch()
# test_obj.test_crime_priority_list()
# test_obj.close_dispatch_file()
