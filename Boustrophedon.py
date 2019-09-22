'''
	Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
	
	In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon"
			
			 1
			/     \
		  2         3
		 / \       / \
		4   5     6   7
		
	Output: [1, 3, 2, 4, 5, 6, 7]
'''

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	
def boustronsphedon(root):
	
	# Corner Case
	if root is None:
		return
	
	#Define Current and Next Stack to store data
	currentLevel = []
	nextLevel = []
	result = []
	
	#Variable to keep track left or right
	lft = True
	
	currentLevel.append(root)
	
	while (len(currentLevel)>0):
		temp = currentLevel.pop(-1)
		result.append(temp.data)
		
		if lft:
			# Push Left before Right
			if temp.left:
				nextLevel.append(temp.left)
			if temp.right:
				nextLevel.append(temp.right)
		
		else:
			# Push Right before Left
			if temp.right:
				nextLevel.append(temp.right)
			if temp.left:
				nextLevel.append(temp.left)
		
		if len(currentLevel) == 0:
			# reverse lft to push node in opposite order
			lft = not lft
			currentLevel,nextLevel = nextLevel,currentLevel

	print(result)
		
# Driver Code
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
print("Boustrophedon traversal of binary tree is") 
boustronsphedon(root)