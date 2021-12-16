import graphviz

# TODO: Have a use case for the parent attribute. I update when I rotate it (i.e. left rotation and right rotation), but don't use it for any other purpose.
# TODO: AVL, AVL --> f(x) --> heap (crime dispatch)
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
        self.parent = None
        self.left = None
        self.right = None
        self.balance = 0
        self.height = 1

    def __repr__(self):
        return str(self.value)


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        self._insert(self.root, node)

    def _insert(self, root, node):
        # If the root is None, return a new node.
        if self.root is None:
            self.root = node
            return self.root
        # If the root value is greater than the node value, insert the node to the left.
        elif node.value < root.value:
            # Check if the left child is None if not call the insert function again.
            root.left = self._insert(root.left, node) if root.left is not None else node
            # Assigns the parent of the node.
            root.left.parent = root
        # If the root value is less than the node value, insert the node to the right.
        else:
            # Check if the right child is None if not call the insert function again.
            root.right = self._insert(root.right, node) if root.right is not None else node
            # Assigns the parent of the node.
            root.right.parent = root

        # Update the height of the nodes.
        # self.update_height(root)
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1

        # Update the balance of the nodes.
        # self.balance(root)
        root.balance = self._get_height(root.left) - self._get_height(root.right)

        # Update the root node based on the new node.
        self.root = self.rebalance(root)

        return self.root

    # Rebalance the tree if it is unbalanced.
    def rebalance(self, node):

        # Case 1: Right Right
        if node.balance == -2:
            return self.left_rotate(node)

        # Case 2: Left Left
        if node.balance == 2:
            return self.right_rotate(node)

        # Case 3: Right Left
        if node.balance == -2 and node.right.balance > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Case 4: Left Right
        if node.balance == 2 and node.left.balance < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        return node

    # Rotate the tree to the right.
    def right_rotate(self, node):
        """The unbalanced node becomes the right child of the left child."""
        # Check if the node left child is None.
        if node.left is None:
            return node

        # TODO: Do a step before assigning the pivot.
        pivot = node.left
        temp_node = pivot.right
        pivot.right = node
        pivot.parent = node.parent
        node.parent = pivot
        node.left = temp_node

        # Update the height of the nodes.
        # self.update_height(node)
        # self.update_height(pivot)
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        pivot.height = (max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1)

        # Update the balance of the nodes.
        # self.balance(node)
        # self.balance(pivot)
        node.balance = self._get_height(node.left) - self._get_height(node.right)
        pivot.balance = self._get_height(pivot.left) - self._get_height(pivot.right)

        # Return the new node.
        return pivot

    def left_rotate(self, node):
        """The unbalanced node becomes the left child of the right child."""
        # Check if the node right child is None.
        if node.right is None:
            return node

        # TODO: Do a step before assigning the pivot.
        pivot = node.right
        temp_node = pivot.left
        pivot.left = node
        pivot.parent = node.parent
        node.parent = pivot
        node.right = temp_node

        # Update the height of the nodes.
        # self.update_height(node)
        # self.update_height(pivot)
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1

        # Update the balance of the nodes.
        # self.balance(node)
        # self.balance(pivot)
        node.balance = self._get_height(node.left) - self._get_height(node.right)
        pivot.balance = self._get_height(pivot.left) - self._get_height(pivot.right)

        # Return the new node.
        return pivot

    # Check the balance of the node.
    def balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    # Get the height of the node.
    def _get_height(self, node):
        # If the node is None 0 will be returned else the height of the node will be returned.
        return node.height if node is not None else 0

    def update_height(self, node):
        # Update the height of the node.
        return max(self._get_height(node.left), self._get_height(node.right)) + 1

    # Remove a specific node from the tree.
    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        # TODO: Get the successor and predecessor of the node.
        if node is None:
            return node
        elif key < node.value:
            node.left = self._remove(node.left, key)
        elif key > node.value:
            node.right = self._remove(node.right, key)
        else:
            pass  # TODO: Code to be written.

        # Update the height of the nodes.
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        # Update the balance of the nodes.
        node.balance = self._get_height(node.left) - self._get_height(node.right)

        return self.rebalance(node)

    # TODO: Find a better print statement to do this with. I don't know... it works, however, its ugly.
    # Returns the tree as a string as an in_order traversal.
    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        """Returns the string of an in_order traversal"""
        return (
            "{} {} {}".format(
                self._in_order(node.left), node.value, self._in_order(node.right)
            ).strip()
            if node is not None
            else ""
        )

    # TODO: Fix up these print statements they look horrible.
    # Returns the tree as a string as a postorder traversal.
    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        """Returns the string of an postorder traversal"""
        return (
            "{} {} {}".format(
                self._postorder(node.left), self._postorder(node.right), node.value
            ).strip()
            if node is not None
            else ""
        )

    # Returns the tree as a string as a preorder traversal.
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        """Returns the string of an preorder traversal"""
        return (
            "{} {} {}".format(
                node.value, self._preorder(node.left), self._preorder(node.right)
            ).strip()
            if node is not None
            else ""
        )


if __name__ == "__main__":
    a = AVLTree()
