class CrimeData:  # use the key for data
    def __init__(self, data):
        self.id = data[0]
        self.case_number = data[1]
        self.date = data[2]
        self.block = data[3]
        self.iucr = data[4]
        self.primary_type = data[5]
        self.description = data[6]
        self.location_description = data[7]
        self.arrest = data[8]
        self.domestic = data[9]
        self.beat = data[10]
        self.district = data[11]
        self.ward = data[12]
        self.community_area = data[13]
        self.fbi_code = data[14]
        self.x_coordinate = data[15]
        self.y_coordinate = data[16]
        self.year = data[17]
        self.updated_on = data[18]
        self.latitude = data[19]
        self.longitude = data[20]
        self.location = data[21]


class AVLTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.balance = 0
        self.height = 0
    
    def __str__(self):
        return str(self.key) + " " + str(self.value) 

# TODO: I want to insert all the data from CrimeData into the AVL tree. It has to have all those attributes.


class AVLTree:
    def __init__(self):
        self.root = None
        self.n_inserts = 0

    def insert(self, node):
        self._insert(self.root, node)

    def _insert(self, root, node):
        print("root is: " + str(self.root))
        print("new node is: " + str(node))
        print("this is insert # " + str(self.n_inserts))
        self.n_inserts += 1
        # If the root is None, return a new node.
        if root is None: 
            print("Creating new root node")
            self.root = node
            return node
        # If the key is less than the root, insert it to the left.
        elif node.value < root.value:
            print("Value less than root")
            root.left = self._insert(root.left, node)
        # If the key is greater than the root, insert it to the right.
        elif node.value > root.value:
            print("Value greater than root")
            root.right = self._insert(root.right, node)
        else:
            # Assign the value item to the value attribute.
            print("what the fuck they're equal")
            root.value = node.value

        node.height = self.update_height(node)
        print("Update the height of the node to " + str(node.height))

        node.balance = self.balance(node)
        print("Update the balance factor of this node to " + str(node.balance))

        """
        A balance value of [-2, 2] means that the tree is unbalanced.
        Also, it has to check if values of the keys are greater than the others.
        """
        

        # Case 1: Left Left
        if node.balance == 2 and node.value < root.left.value:
            print("Left Left")
            return self.right_rotate(node)

        # Case 2: Right Right
        if node.balance == -2 and node.value > root.right.value:
            print("Right Right")
            return self.left_rotate(node)

        # Case 3: Left Right
        if node.balance == 2 and node.value > root.left.value:
            print("Left Right")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4: Right Left
        if node.balance == -2 and node.value < root.right.value:
            print("Right Left")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        print()
        return node

    # Rotate the tree to the right.
    def right_rotate(self, pivot):
        """
        The unbalanced node becomes the right child of the left child.
        """
        # Assign the attribute left_child to the left child of the root.
        left_child = pivot.left
        # Make the left child of the root the right child of the left child.
        pivot.left = left_child.right
        # Make the right child of the left child the root.
        left_child.right = pivot

        # Update the height of the node.
        self.update_height(root)
        self.update_height(left_child)

        return left_child

    def left_rotate(self, pivot):
        """
        The unbalanced node becomes the left child of the right child.
        """
        # Assign the attribute right_child to the right child of the root.
        right_child = pivot.right
        # Make the right child of the root the left child of the right child.
        pivot.right = right_child.left
        # Make the left child of the right child the root.
        right_child.left = pivot

        # Update the height of the node.
        self.update_height(pivot)
        self.update_height(right_child)
        
        return right_child

    # Check the balance of the node.
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right) 

    # Get the height of the node.
    def height(self, node):
        # If the node is None -1 will be returned. Else the height of the node will be returned.
        # return node.height if node is not None else -1
        if node is None:
            return -1
        else:
            print("Node's height was " + str(node.height))
            return node.height

    # Update the height of the node.
    def update_height(self, node):
        return max(self.height(node.right), self.height(node.left)) + 1

    # Remove a specific node from the tree.
    def remove(self, key):
        self.root = self._remove(self.root, key)

    # Helper function for the remove function.
    def _remove(self, root, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self._remove(root.left, key)
        else:
            root.right = self._remove(root.right, key)
        return root

    # Returns the tree as a string as an in_order traversal.
    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, root):
        """Returns the string of an in_order traversal"""
        if root is not None:
            return (
                self._in_order(root.left)
                + " " 
                + str(root.key)
                + " "
                + self._in_order(root.right)
            )
        else:
            return ""

    # Returns the tree as a string as a postorder traversal.
    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, root):
        """Returns the string of an postorder traversal"""
        if root is not None:
            return (
                self._postorder(root.left)
                + self._postorder(root.right)
                + " "
                + str(root.key)
            )
        else:
            return ""

    # Returns the tree as a string as a preorder traversal.
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, root):
        """Returns the string of an preorder traversal"""
        if root is not None:
            return (
                " "
                + str(root.key)
                + self._preorder(root.left)
                + self._preorder(root.right)
                + " "
            )
        else:
            return ""

if __name__ == "__main__":
    a = AVLTree()
    root = None
    print(a.root)
