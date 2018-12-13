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

## Binary Tree

<!-- ```java
class Tree {
    public int value;
    public Tree left;
    public Tree right;

    public Tree(int value) {
        this(value, null, null)
    }

    public Tree(int value, Tree left, Tree right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}
``` -->

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
