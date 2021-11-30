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

    def __repr__(self):
        return str(self.value)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        self._insert(self.root, node)

    def _insert(self, root, node):
        # print(node)
        # If the root is None, return a new node.
        if self.root is None:
            self.root = node
            return self.root
            # If the root value is greater than the node value, insert the node to the left.
        elif node.value < root.value:
            # Check if the left child is None if not call the insert function again.
            root.left = self._insert(root.left, node) if root.left is not None else node
        # If the root value is less than the node value, insert the node to the right.
        else:
            # Check if the right child is None if not call the insert function again.
            root.right = (
                self._insert(root.right, node) if root.right is not None else node
            )

        # Update the height of the node.
        root.height = self.update_height(root)

        # Update the balance of the node.
        balance = self.balance(root)

        """
        A balance value of [-2, 2] means that the tree is unbalanced.
        Also, it has to check if values of the keys are greater than the others.
        """

        if root is None:
            return root

        # Case 1: Right Right
        if balance < -1 and node.value > root.right.value:
            # print("Right Right")
            return self.left_rotate(root)

        # Case 2: Left Left
        if balance > 1 and node.value < root.left.value:
            # print("Left Left")
            return self.right_rotate(root)

        # Case 3: Right Left
        if balance < -1 and node.value < root.right.value:
            # print("Right Left")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Case 4: Left Right
        if balance > 1 and node.value > root.left.value:
            # print("Left Right")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        return root

    # Rotate the tree to the right.
    def right_rotate(self, pivot):
        """The unbalanced node becomes the right child of the left child."""

        if pivot.left is None:
            return pivot

        left_child = pivot.left
        b = left_child.right
        left_child.right = pivot
        pivot.left = b

        pivot.height = self.update_height(pivot)
        left_child.height = self.update_height(left_child)

        return left_child

    def left_rotate(self, pivot):
        """The unbalanced node becomes the left child of the right child."""
        if pivot.right is None:
            return pivot

        right_child = pivot.right
        b = right_child.left
        right_child.left = pivot
        pivot.right = b

        pivot.height = self.update_height(pivot)
        right_child.height = self.update_height(right_child)

        return right_child

    # Check the balance of the node.
    def balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

        # Get the height of the node.

    def get_height(self, node):
        # If the node is None -1 will be returned. Else the height of the node will be returned.
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        # Update the height of the node.
        return max(self.get_height(node.left), self.get_height(node.right)) + 1

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

    def _in_order(self, node):
        """Returns the string of an in_order traversal"""
        if node is not None:
            return (
                self._in_order(node.left)
                + " "
                + str(node.value)
                + " "
                + self._in_order(node.right)
            )
        else:
            return ""

    # Returns the tree as a string as a postorder traversal.
    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        """Returns the string of an postorder traversal"""
        if node is not None:
            return (
                self._postorder(node.left)
                + self._postorder(node.right)
                + " "
                + str(node.value)
            )
        else:
            return ""

    # Returns the tree as a string as a preorder traversal.
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        """Returns the string of an preorder traversal"""
        if node is not None:
            return (
                " "
                + str(node.value)
                + self._preorder(node.left)
                + self._preorder(node.right)
                + " "
            )
        else:
            return ""


if __name__ == "__main__":
    a = AVLTree()
    root = None
