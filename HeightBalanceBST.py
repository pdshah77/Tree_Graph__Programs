'''
	Given a binary tree write a Program, determine whether or not it is height-balanced.
	A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.
'''

class Node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data
		
# Function to find Height of Binary Tree
def height(root):
	if root is None:
		return 0
	return max(height(root.left),height(root.right))+1

def isBalanced(root):
	if root is None:
		return True
	
	lh = height(root.left)
	rh = height(root.right)
	
	if (abs(lh-rh)<=1) and isBalanced(root.left) is True and isBalanced(root.right) is True:
		return True
	
	return False

root = Node(1)	
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

if isBalanced(root):
	print("Tree is Balanced")
else:
	print("Tree is Not Balanced")