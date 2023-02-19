from ChicagoCrimeFun import *
from visualize import VisualizeData

def main():
    ccf = ChicagoCrimeFun()
    ccf.add_random_case(5)
    q = ccf.dispatch_queue
    v = VisualizeData()
    dot = v.visualize_heap(q)
    dot.format = "png"
    dot.view(filename="heap", directory="./visualizations/")

if __name__ == '__main__':
    main()
