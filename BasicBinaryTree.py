'''
	Write a Program to Create a Generate Binary Tree
	
	Example:       1			---> ROOT
				2	 3			---> NODES
			 4		    5		---> LEAVES
			 
	Python Version: Python 3.7
'''

class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
		
# Create a Root Object of Node
root = Node(1)

# Assign Left and Right Node Values
root.left = Node(2)
root.right = Node(3)

# Assign More Values to Left and Right Nodes
root.left.left = Node(4)
root.right.right = Node(5)