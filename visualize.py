from graphviz import Digraph

class VisualizeData:  
    def visualize_data(self, node):
        dot = Digraph()
        return self._visualize_data(node.root, dot)

    def _visualize_data(self, node, dot=None):    
        """
        Transverses the node and creates a graph.
            Arguments:
            arg1: [object] The binary node.
            arg2: [object] The graphviz object.
            arg3: [boolean] The first node is root: True. 
            
        Returns:
            [object]: The graph (needed to be formatted).
        """       
        
        # Create Digraph object.
        if node is not None:
            # Add node to the graph.    
            dot.node(name=str(node), label=str(node.key), xlabel=str(node.height))

            # Traverse through the left subnode.
            if node.left:
                # Add node to the graph.
                dot.edge(str(node), str(node.left))
                # Recursive call through left subnode.
                self._visualize_data(node.left, dot)
            
            # Traverse through the right subnode.  
            if node.right:
                # Add node to the graph.
                dot.edge(str(node), str(node.right))
                # Recursive call through right subnode.
                self._visualize_data(node.right, dot) 

        # Return the graph.
        return dot
