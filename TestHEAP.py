from visualize import *
from ChicagoCrimeFun import *
from graphviz import Digraph


def main():
    ccf = ChicagoCrimeFun()
    ccf.add_random_case(5)
    q = ccf.dispatch_queue
    
    v = VisualizeData()
    dot = v.visualize_heap(q)
    dot.format = "png"
    dot.view(filename="heap", directory="./visualizations/")


class VisualizeData:
    def visualize_heap(self, tree, dot=None):    
        if dot is None:
            dot = Digraph(strict=True)
            dot.node(name=str(tree), label=str(tree.heap))

        i = 0
        while (i < (tree.size // 2) + 1):
            dot.node(name=str(tree.heap[2 * i]), label=str(tree.heap[2 * i]))
            dot.edge(str(tree), str(tree.heap[2 * i]))
            break;
        
        while (i < (tree.size // 2) + 1):
            dot.node(name=str(tree.heap[2 * i + 1]), label=str(tree.heap[2 * i + 1]))
            dot.edge(str(tree), str(tree.heap[2 * i + 1]))           
            break; 


        return dot


if __name__ == '__main__':
    main()
