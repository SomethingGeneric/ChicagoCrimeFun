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

    def _insert(self, node, key):
        # If the root is None, return a new node.
        if self.root is None:
            self.root = key
            return self.root
        # If the root value is greater than the node value, insert the node to the left.
        elif key.value < node.value:
            # Check if the left child is None if not call the insert function again.
            node.left = self._insert(node.left, key) if node.left is not None else key
            # Assigns the parent of the node.
            node.left.parent = node
        # If the root value is less than the node value, insert the node to the right.
        elif key.value > node.value:
            # Check if the right child is None if not call the insert function again.
            node.right = self._insert(node.right, key) if node.right is not None else key
            # Assigns the parent of the node.
            node.right.parent = node
        else:
            # Return if the node exists in the tree.
            return node

        # Update the height of the nodes.
        # self.update_height(root)
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        # Update the balance of the nodes.
        # self.balance(root)
        node.balance = self._get_height(node.left) - self._get_height(node.right)

        # Update the root node based on the new node.
        self.root = self._get_balance(node)

        return self.root

    # _get_balance the tree if it is unbalanced.
    def _get_balance(self, node):

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

        pivot = node.left
        temp_node = pivot.right
        pivot.right = node
        pivot.parent = node.parent
        node.parent = pivot
        node.left = temp_node

        # Update the height of the nodes.
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        pivot.height = (max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1)

        # Update the balance of the nodes.
        node.balance = self._get_height(node.left) - self._get_height(node.right)
        pivot.balance = self._get_height(pivot.left) - self._get_height(pivot.right)

        # Return the new node.
        return pivot

    def left_rotate(self, node):
        """The unbalanced node becomes the left child of the right child."""
        # Check if the node right child is None.
        if node.right is None:
            return node

        pivot = node.right
        temp_node = pivot.left
        pivot.left = node
        pivot.parent = node.parent
        node.parent = pivot
        node.right = temp_node

        # Update the height of the nodes.
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1

        # Update the balance of the nodes.    
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
        if node is None:
            return node
        elif key < node.value:
            node.left = self._remove(node.left, key)
        elif key > node.value:
            node.right = self._remove(node.right, key)
        else:
            # Case 1: Leaf node
            if not node.left and not node.right:
                node = None
            # Case 2: Node with one child
            elif not node.left or not node.right:
                if node.left:
                    node = node.left
                else:
                    node = node.right
            # Case 3: Node with two children
            else:
                temp = self._get_min_node(node.right)
                node.key = temp.key
                node.right = self._remove(node.right, temp.key)

        # Update the height of the nodes.
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1

        # Update the balance of the nodes.
        node.balance = self._get_height(node.left) - self._get_height(node.right)

        return self._get_balance(node)
    
    def _get_min_node():
        while node.left:
            node = node.left
        return node

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