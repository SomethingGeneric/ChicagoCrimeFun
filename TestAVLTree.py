from avl import *
from visualize import *
from random import randint


def main():
    # Creates a AVL (balancing binary search tree)
    print("Create binary search tree")
    myTree = AVLTree()
    n = int(
        input(
            """
1. Choose a number of nodes to insert into the tree.
2. Generate a random tree with n nodes. Random range of (1-100).
3. Read from an array of keys.
4. Exit.
Enter option: """
        )
    )
    if n == 1:
        x = int(input("Enter a number of nodes to insert into the tree: "))
        for i in range(1, x + 1):
            myTree.insert(AVLTreeNode(i, i))
    elif n == 2:
        for i in range(1, randint(1, 100)):
            myTree.insert(AVLTreeNode(i, i))
    elif n == 3:
        """[DEBUG]
        The priority ranking is the value and the key is the crime data:
        Make sure that the keys that have the most priority are on the top of the array. Its hard to test here since I am doing count+=1 so its
        just priority 1..2..3.. being assigned to every value being passed in.
        However, the underlying data structure is still the same and working its just about now doing with keys that are different does
        it respect the priority order instead of numbers
        """
        p = input("Enter the array of strings: ")
        list_of_nodes = p.split()
        count = 1
        for i in range(len(list_of_nodes)):
            j = list_of_nodes[i]
            # J should be the attributes like location that I am passing in and then the value is the count and the first
            # attribute in the array should be near the top of the tree depending on the balancing.
            myTree.insert(AVLTreeNode(j, count))
            count += 1
    else:
        print("Exiting...")
        exit(0)

    # Print out transversal of tree.
    print("Print Preorder:")
    pre_o = myTree.preorder()
    print(pre_o)
    print("Print Postorder:")
    post_o = myTree.postorder()
    print(post_o)
    print("Print Inorder:")
    in_o = myTree.in_order()
    print(in_o)

    # Visualize the tree
    v = VisualizeData()
    dot = v.visualize_data(myTree)
    dot.format = "png"
    dot.view(filename="avltree", directory="./visualizations/")


if __name__ == "__main__":
    main()
