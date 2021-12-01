from avl import *
from visualize import *
from graphviz import Digraph


def main():
    # Creates a AVL (balancing binary search tree)
    print("Create binary search tree")
    myTree = AVLTree()
    myTree.insert(AVLTreeNode(1, 1))
    myTree.insert(AVLTreeNode(2, 2))
    myTree.insert(AVLTreeNode(3, 3))

    print("Print preorder")
    pre_o = myTree.preorder()
    print(pre_o)
    print("Print postorder")
    post_o = myTree.postorder()
    print(post_o)
    print("Print inorder")
    in_o = myTree.in_order()
    print(in_o)
    
    v = VisualizeData()
    dot = v.visualize_data(myTree)
    dot.format = 'png'
    dot.view(filename='digraph', directory='./')


if __name__ == "__main__":
    main()
