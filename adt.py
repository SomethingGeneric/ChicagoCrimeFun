class CrimeNode:
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None

class CrimeData:
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

class AVLTreeNode(CrimeNode):
    def __init__(self, key, value):
        super().__init__()
        self.key = key
        self.value = value
        self.height = 1
    
class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self, root: CrimeNode, key, value=None):
        # If the root is None, return a new node.
        if root is None:
            return CrimeNode(key, value) 
        # If the key is less than the root, insert it to the left.
        elif key < root.key:
            root.left = self._insert(root.left, key, value) 
        # If the key is greater than the root, insert it to the right.
        elif key > root.key:  
            root.right = self._insert(root.right, key, value)
        else:
            # If the key does not follow any of those confitions return the value of the root node. 
            root.value = value
        return root
    
    def remove(self, root: CrimeNode, key):
        if root is None:
            return root
        elif key < root.key:
            root.left = self._remove(root.left, key)
    
    def rebalance(self, root: CrimeNode):
        if root is None:
            return root

    def __repr__(self):
        print(self.key, self.value)
        
            
