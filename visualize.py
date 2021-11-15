import ete3

from random import randint


class visualizer:
    def __init__(self, tree):
        self.srctree = tree
        self.tree = ete3.Tree()
        self.dist = 0.5
        self.support = 50

        self.node_above = None

    def draw_node(self, node):
        pass

    def draw(self, filename="output.png"):
        self.tree.add_child(
            name=self.srctree.root, dist=self.dist, support=self.support
        )

        self.draw_node(self.srctree.root.left)

        self.tree.render(filename)


class SimpleNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        print("My value is " + str(self.val))

    def __repr__(self):
        return str(self.val)


class SimpleTree:
    def __init__(self, root=None):
        self.root = root


if __name__ == "__main__":

    root = SimpleNode(randint(1, 100))
    root.left = SimpleNode(randint(1, 100))
    root.right = SimpleNode(randint(1, 100))

    tree = SimpleTree(root)

    v = visualizer(tree)
    v.draw()
