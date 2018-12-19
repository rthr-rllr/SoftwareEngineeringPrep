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

<!-- ```java
public class Edge {
    public int weight;
    public int from;
    public int to;
}

public class Vertex implements Comparable<Vertex> {
    public int id;
    public Set<Edge> edges = new HashSet<>();
    public Vertex parent = null;

    public int distance = Integer.MAX_VALUE; // for dijkstra
    public boolean discovered = false;       // for bfs/bfs traversal

    public Vertex(int id) {
        this.id = id;
    }

    /*
     * For dijkstra priority queue
     */
    @Override
    public int compareTo(Vertex o) {
        if (this.distance < o.distance) return -1;
        else if (o.distance < this.distance) return 1;
        else return 0;
    }
}

public class Graph {
    public Map<Integer, Vertex> vertices = new HashMap<>();
}
``` -->

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
