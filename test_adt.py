from adt import *

def main():
    # Creates a AVL (balancing binary search tree)
    print("Create binary search tree")
    myTree = AVLTree()
    root = None
    root = myTree.insert(root, 10)
    myTree.insert(AVLTreeNode(5), 5)
    myTree.insert(AVLTreeNode(2), 15)
    myTree.insert(AVLTreeNode(1), 3)
    myTree.insert(AVLTreeNode(3), 7)
    myTree.insert(AVLTreeNode(4), 13)
    myTree.insert(AVLTreeNode(2), 17)
    

    print("Print preorder")
    pre_o = myTree.preorder()
    print(pre_o)
    print("Print postorder")
    post_o = myTree.postorder()
    print(post_o)
    print("Print inorder")
    in_o = myTree.in_order()
    print(in_o)

if __name__ == '__main__':
    main()
