from graphviz import Digraph

class VisualizeData:
    def visualize_avl(self, node):
        dot = Digraph()
        return self._visualize_avl(node.root, dot)

    def visualize_heap(self, heap):
        dot = Digraph()
        return self._visualize_heap(heap, dot)

    def _visualize_heap(self, tree, dot=None, i=0):
        """
        Transverses the node and creates a graph.
            Arguments:
            arg1: [object] The node.
            arg2: [object] The graphviz object.

        Returns:
            [object]: The graph.
        """

        if dot is None:
            dot = Digraph(strict=True)
            dot.node(name=str(tree.heap[2 * i]), label='"' + str(tree.heap[2 * i]) + '"')

        for i in range(1, tree.size+1):
            if 2*i <= tree.size:
                dot.node(name=str(tree.heap[i]), label=str(tree.heap[i]))
                dot.edge(str(tree.heap[i//2]), str(tree.heap[i]))
            if 2*i + 1 <= tree.size:
                dot.node(name=str(tree.heap[2*i+1]), label=str(tree.heap[2*i+1]))
                dot.edge(str(tree.heap[i]), str(tree.heap[2*i+1]))

        return dot

    def _visualize_avl(self, node, dot=None):
        """
        Transverses the node and creates a graph.
            Arguments:
            arg1: [object] The node.
            arg2: [object] The graphviz object.

        Returns:
            [object]: The graph.
        """

        # Create Digraph object.
        if node is not None:
            # Add node to the graph.
            dot.node(name=str(node), label=str(
                node.key), xlabel=str(node.height))

            # Traverse through the left subnode.
            if node.left:
                # Add node to the graph.
                dot.edge(str(node), str(node.left))
                # Recursive call through left subnode.
                self._visualize_avl(node.left, dot)

            # Traverse through the right subnode.
            if node.right:
                # Add node to the graph.
                dot.edge(str(node), str(node.right))
                # Recursive call through right subnode.
                self._visualize_avl(node.right, dot)

        # Return the graph.
        return dot
