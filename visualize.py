from graphviz import Digraph
class VisualizeData:    
    def visualize_data(self, tree, dot=None, initial_call=True):    
        """
        Tranverses the tree and creates a graph.
            Arguments:
            arg1: [object] The binary tree.
            arg2: [object] The graphviz object.
            arg3: [boolean] The first node is root: True. 
            
        Returns:
            [object]: The graph (needed to be formatted).
        """        
        # For first call use the root node. For subsequent calls use the node.
        if initial_call:
            tree = tree.root
        
        # Create Digraph object.
        if dot is None:
            dot = Digraph()
            dot.node(name=str(tree), label=str(tree.key), xlabel=str(tree.height))

        # Traverse through the left subtree.
        if tree.left:
            # Add node to the graph.
            dot.node(name=str(tree.left), label=str(tree.left.key), xlabel=str(tree.left.height))
            # Add the child node to the parent node.
            dot.edge(str(tree), str(tree.left))
            # Recursive call through left subtree.
            dot = self.visualize_data(tree.left, dot=dot, initial_call=False)
        
        # Traverse through the right subtree.  
        if tree.right:
            # Add node to the graph.
            dot.node(name=str(tree.right), label=str(tree.right.key), xlabel=str(tree.right.height))
            # Add the child node to the parent node.
            dot.edge(str(tree), str(tree.right))
            # Recursive call through right subtree.
            dot = self.visualize_data(tree.right, dot=dot, initial_call=False)

        # Return the graph.
        return dot
