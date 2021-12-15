from visualize import *
from ChicagoCrimeFun import *

def main():
	ccf = ChicagoCrimeFun()
	ccf.add_random_case(10)
	q = ccf.dispatch_queue
	
	# Visualize the Heap 
	my_tree = visualize_heap(q)
	dot.format="png"
	dot.view(filename="heap", directory="./visualizations/")

def visualize_heap(self, tree, dot=None, initial_call=True):
	if initial_call:
	   tree = tree.FRONT

	if dot is None:
		dot = Digraph(strict=False)
		dot.node(name=str(tree), label=(tree.peek())
	if tree.leftChild:
		dot.node(name=str(tree.leftChild), label=str(tree.peek()))
		dot.edge(str(tree), str(tree.leftChild))
		dot = self.visualize_heap(tree.leftChild, dot=dot, initial_call=False)
	if tree.rightChild:
		dot.node(name=str(tree.rightChild), label=str(tree.peek()))
		dot.edge(str(tree), str(tree.rightChild))
		dot = self.visualize_heap(tree.rightChild, dot=dot, initial_call=False)
	return dot
		

if __name__ == '__main__':
	main()
