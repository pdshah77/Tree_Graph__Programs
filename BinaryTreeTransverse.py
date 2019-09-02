''' 
	Write a Program to Transverse Binary Tree in All possible  ways
	
	We can transverse Binary Tree in three differnent possible ways:
	1. InOrder Transverse: Left -> Root -> Right
	2. PreOrder Transverse: Root -> Left -> Right
	3. PostOrder Transverse: Left -> Right -> Root
	
	Python Version: Pyython 3.7
'''


# Define a Node for Binary Tree
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
		
# Define Three Different Order Transverse

def InOrderTransverse(root):

	if root:
		
		InOrderTransverse(root.left)
		print(root.val)
		InOrderTransverse(root.right)

def PreOrderTransverse(root):

	if root:
		
		print(root.val)
		PreOrderTransverse(root.left)
		PreOrderTransverse(root.right)
	
def PostOrderTransverse(root):
	
	if root:
		PostOrderTransverse(root.left)
		PostOrderTransverse(root.right)
		print(root.val)
		
# Main Code

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("InOrder Transverse of a Binary Tree is ")
InOrderTransverse(root)

print("PreOrder Transverse of a Binary Tree is ")
PreOrderTransverse(root)

print("PostOrder Transverse of a Binary Tree is ")
PostOrderTransverse(root)