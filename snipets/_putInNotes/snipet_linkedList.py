
# example of linked list

#%%

#- first attempt

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


#- second attempt, lighter

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, value=None):
        if value is not None:
            value = Node(value)
        self.head = value

    def append(self, value):
        newNode = Node(value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def get_position(self, position):
        counter = 0
        current = self.head
        if position < 0:
            return None
        while current and counter <= position:
            if counter == position:
                return current.value
            current = current.next
            counter += 1
        return None

    def insert(self, value, position):
        newNode = Node(value)
        counter = 0
        current = self.head
        if position > 0:
            while current and counter < position:
                if counter == position - 1:
                    newNode.next = current.next
                    current.next = newNode
                current = current.next
                counter += 1
        elif position == 0:
            newNode.next = self.head
            self.head = newNode

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

# Test cases
# Set up some Elements
e1 = 0
e2 = 'one'
e3 = 2
e4 = 'three'

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
# ll.append(e4)

# Test get_position
# Should print 2
print(ll.head.next.next.value)
# Should also print 2
print(ll.get_position(2))

# Test insert
ll.insert(e4,2)
# Should print three now
print(ll.get_position(2))

# Test delete
ll.delete('one')
# Should print 0 now
print(ll.get_position(0))
# Should print three now
print(ll.get_position(1))
# Should print 2 now
print(ll.get_position(2))


#- solution from [lecture](https://classroom.udacity.com/courses/ud513/lessons/7117335401/concepts/78875247320923)
# NB:
# - they append Node instead of values
# - they use 1-indexing

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next