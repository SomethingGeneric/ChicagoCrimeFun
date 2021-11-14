from adt import *

def main():
    # Creates a AVL (balancing binary search tree)
    print("Create binary search tree")
    new_root = AVLTreeNode(6, "6")
    new_tree = AVLTree()
    new_tree.insert(new_root)
    new_tree.insert(AVLTreeNode(5, "5"))
    new_tree.insert(AVLTreeNode(8, "8"))
    new_tree.insert(AVLTreeNode(3, "3"))
    new_tree.insert(AVLTreeNode(4, "4"))
    new_tree.insert(AVLTreeNode(9, "9"))
    new_tree.insert(AVLTreeNode(7, "7"))
    new_tree.insert(AVLTreeNode(2, "2"))
    new_tree.insert(AVLTreeNode(1, "1"))

    print("Print preorder")
    pre_o = new_tree.preorder()
    print(pre_o)
    print("Print postorder")
    post_o = new_tree.postorder()
    print(post_o)
    print("Print inorder")
    in_o = new_tree.in_order()
    print(in_o)

if __name__ == '__main__':
    main()
