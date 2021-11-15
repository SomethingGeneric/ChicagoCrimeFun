import toytree
import toyplot.html
import newick as nw


class newick:
    def __init__(self):
        return

    def to_newick(self, tree):
        newick = ""
        newick = self.traverse(tree, newick)
        newick = f"{newick};"
        print("Newick: " + newick)
        return newick

    def traverse(self, tree, newick):
        if tree.left and not tree.right:
            newick = f"(,{self.traverse(tree.left, newick)}){tree.key}"
        elif not tree.left and tree.right:
            newick = f"({self.traverse(tree.right, newick)},){tree.key}"
        elif tree.left and tree.right:
            newick = f"({self.traverse(tree.right, newick)},{self.traverse(tree.left, newick)}){tree.key}"
        elif not tree.left and not tree.right:
            newick = f"{tree.key}"
        else:
            pass
        return newick


class visualizer:
    def __init__(self):
        return

    def draw(self, tree, filename=None):
        if filename is None:
            filename = str(tree)
        n = newick()
        as_newick = n.to_newick(tree.root)

        test = nw.loads(as_newick)
        
        print(test[0].ascii_art())

        tree = toytree.tree(as_newick)
        # rte = tree.root(wildcard="")
        canvas, _, _ = tree.draw(width=400, height=300)
        toyplot.html.render(canvas, filename)
