from avl import *

from visualize import visualizer


def main():
    # Creates a AVL (balancing binary search tree)
    print("Create binary search tree")
    myTree = AVLTree()
    new_root = AVLTreeNode(6, 6)
    myTree.insert(new_root)
    myTree.insert(AVLTreeNode(5, 5))
    myTree.insert(AVLTreeNode(8, 8))
    myTree.insert(AVLTreeNode(3, 3))
    # myTree.insert(AVLTreeNode(4, 4))
    myTree.insert(AVLTreeNode(9, 9))
    myTree.insert(AVLTreeNode(7, 7))
    myTree.insert(AVLTreeNode(2, 2))
    myTree.insert(AVLTreeNode(1, 1))
    myTree.insert(AVLTreeNode(4, 4))
    myTree.insert(AVLTreeNode(10, 10))
    myTree.insert(AVLTreeNode(11, 11))
    myTree.insert(AVLTreeNode(12, 12))
    myTree.insert(AVLTreeNode(13, 13))

    print("Print preorder")
    pre_o = myTree.preorder()
    print(pre_o)
    print("Print postorder")
    post_o = myTree.postorder()
    print(post_o)
    print("Print inorder")
    in_o = myTree.in_order()
    print(in_o)

    # v = visualizer()
    # v.draw(myTree, "foo.html")
    
    myTree.print_tree()


if __name__ == "__main__":
    main()
