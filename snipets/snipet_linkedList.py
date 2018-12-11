
# example of linked list

#%%

class Node:
  
	def __init__(self):
		
		self.data = None
		self.next = None


class LinkedList:
	
	def __init__(self):

		self.headNode = None
		self.tailNode = None
		self.len = 0

	def append(self, data):
		
		newNode = Node()
		newNode.data = data
		
		if self.headNode is None:
			self.headNode = newNode

		if self.tailNode is not None:
			self.tailNode.next = newNode
		self.tailNode = newNode
		self.len += 1

	def print(self):

		if self.headNode is None:
			print('empty list')
		else:
			done = False
			currNode = self.headNode
			while not done:
				print(currNode.data)
				if currNode.next is None:
					done = True
				else:
					currNode = currNode.next



ll = LinkedList()
ll.append(1)
ll.append('a')
ll.append((2,3))
ll.append(10)
ll.append('yes')

ll.print()
print(ll.len)


			