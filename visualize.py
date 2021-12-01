from graphviz import Digraph

class VisualizeData:
    def __init__(self):
        pass
    def visualize_data(self, tree, dot=None, inital_call=None):
        # Create Digraph object
        if dot is None:
            dot = Digraph()
            dot.node(name=str(tree), label=str(tree.value))

        # Add nodes
        if tree.left:
            dot.node(name=str(tree.left) ,label=str(tree.left.value))
            dot.edge(str(tree), str(tree.left))
            dot = self.visualize_data(tree.left, dot=dot)
            
        if tree.right:
            dot.node(name=str(tree.right) ,label=str(tree.right.value))
            dot.edge(str(tree), str(tree.right))
            dot = self.visualize_data(tree.right, dot=dot)
    
        # Add nodes recursively and create a list of edges~
        dot = self.visualize_data(tree)

        dot.format = 'png'
        dot.view(filename='digraph', directory='./')

        # Visualize the graph
        display(dot)
    
        return dot