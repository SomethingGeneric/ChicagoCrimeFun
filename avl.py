import graphviz

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

        # # Update the height of the node.
        # root.height = self.update_height(root)
        # print("Height " + str(root.height))
        # # Update the balance of the node.
        # root.balance = self.balance(root)
        # print("Balance: " + str(root.balance))
        root.height = max(self._get_height(root.left), self._get_height(root.right)) + 1
        root.balance = self._get_height(root.left) - self._get_height(root.right)
        
        x = self.rebalance(root)
        self.root = x    
        # FIXME: I never update the root attribute I just send the node which kept track of 1 being root.
        # print("Parent: " + str(x.parent))
        # print("Root: " + str(x))
        # print("Left: " + str(x.left))
        # print("Right: " + str(x.right))
        # print("----------------------------------------------------")
        return x
    
    # FIXME: I never update the height properly I keep changing it between 0 and 1 and it fixes the graph.
    # Rebalance the tree if it is unbalanced.
    def rebalance(self, node):
        
        # Case 1: Right Right
        if node.balance == -2:
            print("Right Right")
            return self.left_rotate(node)

        # Case 2: Left Left
        if node.balance == 2:
            print("Left Left")
            return self.right_rotate(node)

        # Case 3: Right Left
        if node.balance == -2 and node.right.balance > 0:
            print("Right Left")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Case 4: Left Right
        if node.balance == 2 and node.left.balance < 0:
            print("Left Right")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        return node

        # FIXME: DO NOT REMOVE THIS UNCOMMENT OUT CODE USED FOR OPTIMIZATION.
        # """
        # A balance value of [-2, 2] means that the tree is unbalanced.
        # Also, it has to check if values of the keys are greater than the others.
        # """
        
        # # Case 1: Right Right
        # if node.balance == -2:
        #     print("Right Right")
        #     return self.left_rotate(node)

        # # Case 2: Left Left
        # if node.balance == 2:
        #     print("Left Left")
        #     return self.right_rotate(node)

        # # Case 3: Right Left
        # if node.balance == -2 and root.right.balance > 0:
        #     print("Right Left")
        #     node.right = self.right_rotate(node.right)
        #     return self.left_rotate(node)

        # # Case 4: Left Right
        # if node.balance == 2 and root.left.balance < 0:
        #     print("Left Right")
        #     node.left = self.left_rotate(node.left)
        #     return self.right_rotate(node)
        
        # #------------------------------------------>
        # # Case 1: Right Right
        # if node.balance < -1 and node.value > node.right.value:
        #     print("Right Right")
        #     return self.left_rotate(node)

        # # Case 2: Left Left
        # if node.balance > 1 and node.value < node.left.value:
        #     print("Left Left")
        #     return self.right_rotate(node)

        # # Case 3: Right Left
        # if node.balance < -1 and node.value < node.right.value:
        #     print("Right Left")
        #     node.right = self.right_rotate(node.right)
        #     return self.left_rotate(node)

        # # Case 4: Left Right
        # if node.balance > 1 and node.value > node.left.value:
        #     print("Left Right")
        #     node.left = self.left_rotate(node.left)
        #     return self.right_rotate(node)
        # #------------------------------------------>
        # # Case 1: Right Right
        # if node.balance == -2 and node.value > node.right.value:
        #     print("Right Right")
        #     return self.left_rotate(node)

        # # Case 2: Left Left
        # if node.balance == 2 and node.value < node.left.value:
        #     print("Left Left")
        #     return self.right_rotate(node)

        # # Case 3: Right Left
        # if node.balance == -2 and node.value < node.right.value:
        #     print("Right Left")
        #     node.right = self.right_rotate(node.right)
        #     return self.left_rotate(node)

        # # Case 4: Left Right
        # if node.balance == 2 and node.value > node.left.value:
        #     print("Left Right")
        #     node.left = self.left_rotate(node.left)
        #     return self.right_rotate(node)
        
        # return node
        
    # Rotate the tree to the right.
    def right_rotate(self, node):
        """The unbalanced node becomes the right child of the left child."""
        if node.left is None:
            return node
        
        pivot = node.left
        temp_node = pivot.right
        pivot.right = node
        pivot.parent = node.parent # Reassign the parent of the node.
        node.parent = pivot
        node.left = temp_node     
        
        # FIXME: Instead of doing the computation here do it in a different function.
        # # Update the height of the nodes.
        # node.height = self.update_height(node)
        # pivot.height = self.update_height(pivot)
        
        # # Update the balance of the nodes.
        # pivot.balance = self.balance(pivot)
        # node.balance = self.balance(node)
        
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        node.balance = self._get_height(node.left) - self._get_height(node.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.balance = self._get_height(pivot.left) - self._get_height(pivot.right)
        
        #FIXME: Do not remove this is for debugging.
        # print("Node Balance: " + str(node.balance))
        # print("Node Height: " + str(node.height))
        # print("Pivot Balance: " + str(pivot.balance))
        # print("Pivot Height: " + str(pivot.height))
        # print("----------------------------------------------------")
        
        # Return the new node.
        return pivot

    def left_rotate(self, node):
        """The unbalanced node becomes the left child of the right child."""
        if node.right is None:
            return node

        pivot = node.right
        temp_node = pivot.left
        pivot.left = node
        pivot.parent = node.parent
        node.parent = pivot
        node.right = temp_node
        
        # FIXME: Instead of doing the computation here do it in a different function.
        
        ## Update the height of the nodes.  
        # pivot.height = self.update_height(pivot)
        # node.height = self.update_height(node)
        
        # # Update the balance of the nodes.
        # pivot.balance = self.balance(pivot)
        # node.balance = self.balance(node)
                
        node.height = max(self._get_height(node.left), self._get_height(node.right)) + 1
        node.balance = self._get_height(node.left) - self._get_height(node.right)
        pivot.height = max(self._get_height(pivot.left), self._get_height(pivot.right)) + 1
        pivot.balance = self._get_height(pivot.left) - self._get_height(pivot.right)
        
        # FIXME: Do not remove this is for debugging.
        # print("Node Balance: " + str(node.balance))
        # print("Node Height: " + str(node.height))
        # print("Pivot Balance: " + str(pivot.balance))
        # print("Pivot Height: " + str(pivot.height))
        # print("----------------------------------------------------")
        
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