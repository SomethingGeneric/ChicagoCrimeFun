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

# TODO: Add the balancing to the AVL tree.
# TODO: Make the repr function for the AVL tree.
# TODO: Make the rebalance function for the AVL tree.
# TODO: Make the balance function for the AVL tree.
# (this is to see if the left or right is greater than the other side and using rotation to fix it.)
# TODO: Make left rotation and right rotation for the AVL tree.


class AVLTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.balance = 0
        self.height = 0


class AVLTree:
    # I want to insert all the data from CrimeData into the AVL tree. It has to have all those attributes.
    def __init__(self):
        self.root = None

    def insert(self, key, value=None):
        # value should be the node im inserting (make the object and and put it into value)
        self.root = self._insert(self.root, key, CrimeData(value))

    def _insert(self, root, key, value=None):
        # If the root is None, return a new node.
        if root is None:  # I should make a new node before this and pass it as the value in insert
            self.root = AVLTreeNode(key, value)
        # If the key is less than the root, insert it to the left.
        elif key < root.key:
            root.left = self._insert(root.left, key, value)
        # If the key is greater than the root, insert it to the right.
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        else:
            # Assign the value item to the value attribute.
            root.value = value

        # Update the height of the node.
        root.height = self.update_height(root)

        # Update the balance factor.
        root.balance = self.balance(root)

        # TODO: Make the four cases. I need to check the height of the left and right side and the balance.

        return root

    # Rotate right and left method (pivot attribute for the rotation)
    def right_rotate(self):
        pass

    def left_rotate(self):
        pass

    # Check the balance of the node.
    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.right) - self.height(root.left)

    # Get the height of the node.
    def height(self, root):
        return root.height if not root else -1

    # Update the height of the node.
    def update_height(self, root):
        root.height = max(self.height(root.left), self.height(root.right)) + 1

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

    # TODO: post order, inorder, preorder traversal functions.

    def __repr__(self):
        return "{root.key} : {root.value}"


a = AVLTree()
root = None
print(a.root)
