# Data Structures Examples

> To be completed, following the original `Java` cheatsheet.

_____


## Linked List

```python
#- from this [lecture](https://classroom.udacity.com/courses/ud513/lessons/7117335401/concepts/78875247320923)
# NB:
# - they append Nodes instead of values
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

    def search(self, find_val):
        # use a helper function to allow passing current element as input, while using head here
        return self.search_helper(self.head, find_val)
        
    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            else:
                # must "return", not only call recursively (even if base case does return)
                return self.search_helper(current.next, find_val) 
        else:
            return False
```


## Stack

Backed by linked list:

```python
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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            out = self.head
            self.head = out.next
            return out
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
```

## Queue

Backed by `list()`:

```python
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0] 

    def dequeue(self):
        out = self.peek()
        del self.storage[0]
        return out
```

## Hash Map

```python
class HashTable(object):
    """
    Write a (basic, non-space optimised)
    HashTable class that stores strings
    in a hash table, where keys are calculated
    using the first two letters of the string.
    """

    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        idx = self.calculate_hash_value(string)
        if self.table[idx] is None:
            self.table[idx] = [string]
        else:
            self.table[idx].append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        idx = self.calculate_hash_value(string)
        if self.table[idx] is None:
            return -1
        else:
            if string in self.table[idx]:
                return idx
            else:
                return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if len(string) < 2:
            raise ValueError('string must have 2 elements at least')
        upp = string.upper()
        return 100*ord(upp[0]) + ord(upp[1])
```


## Binary Tree

```python
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None  # Node
        self.right = None # Node

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        # use a helper function to allow passing current element as input, while using root here
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        return self.preorder_print(self.root, "")[:-1]

    def preorder_search(self, current, find_val):
        """ current: Node """
        if current:
            if current.value == find_val:
                return True
            else:
                # must "return", not only call recursively (even if base case does return)
                return self.preorder_search(current.left, find_val) or self.preorder_search(current.right, find_val)
        return False

    def preorder_print(self, current, traversal):
        """ current: Node """
        if current:
            traversal += (str(current.value) + "-")
            traversal = self.preorder_print(current.left, traversal)
            traversal = self.preorder_print(current.right, traversal)
        return traversal
```

## Graph

```python
"""
a simplified Graph class with redundant information in order to define
multiple ways to output the content
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False # for search functions

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

    def __str__(self):
        return 'edge:({})-{}-({})'.format(self.node_from.value,self.value,self.node_to.value)
    
class Graph(object):
    """ assume nodes have unique values to simplify code """
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

	def get_edge_list(self):
	    edge_list = []
	    for edge_object in self.edges:
	        edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
	        edge_list.append(edge)
	    return edge_list

	def get_adjacency_list(self):
	    max_index = self.find_max_index()
	    adjacency_list = [None] * (max_index + 1)
	    for edge_object in self.edges:
	        if adjacency_list[edge_object.node_from.value]:
	            adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
	        else:
	            adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
	    return adjacency_list

	def get_adjacency_matrix(self):
	    max_index = self.find_max_index()
	    adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
	    for edge_object in self.edges:
	        adjacency_matrix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
	    return adjacency_matrix

	def find_max_index(self):
	    max_index = -1
	    if len(self.nodes):
	        for node in self.nodes:
	            if node.value > max_index:
	                max_index = node.value
	    return max_index


    def dfs_helper(self, start_node):
        """The helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        REQUIRES: self._clear_visited() to be called before
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """
        ret_list = [start_node.value]
        start_node.visited = True
        edges_out = [e for e in start_node.edges
                     if e.node_to.value != start_node.value]
        for edge in edges_out:
            if not edge.node_to.visited:
                ret_list.extend(self.dfs_helper(edge.node_to))
        return ret_list

    def dfs(self, start_node):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        return self.dfs_helper(start_node)

    def bfs(self, start_node):
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        ret_list = []

        queue = [start_node]
        start_node.visited = True
        def enqueue(n, q=queue):
            n.visited = True
            q.append(n)
        def unvisited_outgoing_edge(n, e):
            return ((e.node_from.value == n.value) and
                    (not e.node_to.visited))
        while queue:
            node = queue.pop(0)
            ret_list.append(node.value)
            for e in node.edges:
                if unvisited_outgoing_edge(node, e):
                    enqueue(e.node_to)
        return ret_list
```

## Trie

<!-- ```java
public class Trie {
    public Character c;
    public Map<Character, Trie> chars = new HashMap<>();
    public boolean isLeaf = false;

    /*
     * For root element that has no char
     */
    public Trie() {
        this(null);
    }

    public Trie(Character c) {
        this.c = c;
    }
}
``` -->

## BitSet

<!-- ```java
public class BitSet {
    private byte[] a;

    public BitSet(int size) {
        this.a = new byte[size];
    }

    public boolean get(int i) {
        return (a[i / 8] & 1 << (i % 8)) == 1 << (i % 8);
    }

    public void set(int i, boolean value) {
        if (value)
            a[i / 8] |= 1 << (i % 8);
        else
            a[i / 8] ^= 1 << (i % 8);
    }
}
``` -->
