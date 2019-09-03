''' 
	Write a Program to Insert the Given Key Value inside Binary Tree
	
	Before Insert:
				3
			4		5
		7		9		11
	
	Insert Key: 12
	
	After Insert:
				  3

			4			5
			
		7		12	9		11
'''

# Node Class to be utilised at every level of Binary Tree
class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# In Order Transverse of Binary Tree 
def inOrderTransverse(root):
	
	if (not root):
		return
	
	inOrderTransverse(root.left)
	print(root.val)
	inOrderTransverse(root.right)
	
# Insert Key Function to insert Value in Binary Tree
def insertKey(root,key):
	# Take Empty List and add root into it
	temp_list = []
	temp_list.append(root)
	
	# For Every Order do the transverse
	while (len(temp_list)):
		# Fetching Recently added Root Element
		root = temp_list[0]
		temp_list.pop(0)
		
		if (not root.left):
			root.left = Node(key)
			break
		else:
			temp_list.append(root.left)
		
		if (not root.right):
			root.right = Node(key)
			break
		else:
			temp_list.append(root.right)

# Driver Code
if __name__ == '__main__':
	root = Node(3)
	root.left = Node(4)
	root.left.left = Node(7)
	root.right = Node(5)
	root.right.left = Node(9)
	root.right.right = Node(11)
	
	print("Before Insert Inorder Transverse of BS: ")
	inOrderTransverse(root)
	
	# Insert a Key using Insert Method
	insertKey(root,'12')
	
	print("After Insert Inorder Transverse of BS: ")
	inOrderTransverse(root)
		
