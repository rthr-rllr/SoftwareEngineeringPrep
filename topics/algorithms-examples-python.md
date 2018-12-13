# Algorithms Code Examples

<!-- All examples can use the utility function `swap`:

```java
private void swap(int[] a, int i, int j) {
    int tmp = a[i];
    a[i] = a[j];
    a[j] = tmp;
}
``` -->

## Tree Traversal

### In-Order

<!-- ```java
public void inOrder(Tree tree) {
    if (tree == null) return;

    inOrder(tree.left);
    // process tree.value
    inOrder(tree.right);
}
``` -->

Without recursion:

<!-- ```java
public void inOrder(Tree tree) {
    Stack<Tree> stack = new Stack<>();
    Tree curr = tree;

    while (curr != null || !stack.isEmpty()) {
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }

        curr = stack.pop();
        // process curr.value
        curr = curr.right;
    }
}
``` -->

### Pre-Order

<!-- ```java
public void preOrder(Tree tree) {
    if (tree == null) return;

    // process tree.value
    preOrder(tree.left);
    preOrder(tree.right);
}
``` -->

Without recursion:

<!-- ```java
public void preOrder2(Tree tree) {
    Stack<Tree> stack = new Stack<>();
    stack.push(tree);
    Tree curr;

    while (!stack.isEmpty()) {
        curr = stack.pop();

        // process curr.value
        if (curr.right != null) stack.push(curr.right);
        if (curr.left != null) stack.push(curr.left);
    }
}
``` -->

### Post-Order

<!-- ```java
public void postOrder(Tree tree) {
    if (tree == null) return;

    postOrder(tree.left);
    postOrder(tree.right);
    // process tree.value
}
``` -->

Without recursion:

<!-- ```java
public void postOrder(Tree tree) {
    Stack<Tree> tmp = new Stack<>();
    Stack<Tree> all = new Stack<>();
    tmp.push(tree);
    Tree curr;

    while (!tmp.isEmpty()) {
        curr = tmp.pop();
        all.push(curr);
        if (curr.left != null) tmp.push(curr.left);
        if (curr.right != null) tmp.push(curr.right);
    }

    while (!all.isEmpty()) {
        curr = all.pop();
        // process curr.value
    }
}
``` -->

## Sorting

### Insertion Sort

<!-- ```java
public void sort(int[] a) {
    for (int j = 1; j < a.length; j++) {
        int key = a[j];
        int i = j - 1;

        while (i >= 0 && a[i] > key) {
            a[i + 1] = a[i];
            i--;
        }

        a[i + 1] = key;
    }
}
```
 -->

### Selection Sort

<!-- ```java
public void sort(int[] a) {
    for (int i = 0; i < a.length; i++)
        swap(a, i, min(a, i));
}

private int min(int[] a, int start) {
    int smallest = start;

    for (int i = start + 1; i < a.length; i++)
        if (a[i] < a[smallest])
            smallest = i;

    return smallest;
}
``` -->

### Mergesort

```python
def mergeSort(ls):
    """ returns a new list sorted """
    
    def merge(ls1, ls2):
        """ returns the merge of two *sorted* lists """
        i1, i2 = 0, 0
        n1, n2 = len(ls1), len(ls2)
        ls = []
    
        while i1 < n1 and i2 < n2: # maybe better to use .pop() ...
            a1, a2 = ls1[i1], ls2[i2]
            if a1 <= a2:
                ls.append(a1)
                i1 += 1
            else:
                ls.append(a2)
                i2 += 1
        if i1 == n1:
            ls += ls2[i2:] # ... pecifically to avoid using [i2:] ...
        if i2 == n2:
            ls += ls1[i1:]
    
        return ls

    n = len(ls)
    if n <= 1:
        return ls
    else:
        m = int(n/2)
        lsL = ls[:m]
        lsR = ls[m:]
        
        lsL_sorted = mergeSort(lsL)
        lsR_sorted = mergeSort(lsR)

        ls_merged = merge(lsL_sorted, lsR_sorted)

        return ls_merged
```

### Quicksort

```python
def quickSort(ls):
    """
    returns a new list sorted
    no random pivot here: we take the last element
    version presented [here](https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/71181150370923)
    """

    if len(ls) <= 1:
        return ls
    else:
        ip = len(ls)-1
        i = 0
        
        while i < ip:
            if ls[i] > ls[ip]:
                # swap and move pivot
                tmp = ls[i]
                ls[i] = ls[ip-1]
                ls[ip-1] = ls[ip]
                ls[ip] = tmp
                ip -= 1
            else:
                # continue
                i += 1

        return quickSort(ls[:ip]) + [ls[ip]] + quickSort(ls[ip+1:])
```

### Heapsort

<!-- ```java
public void sort(int[] a) {
    // build a max-heap
    for (int i = a.length - 1; i >= 0; i--)
        heapify(a, i, a.length);

    // extract max element from the head to the end and shrink the size of the heap
    for (int last = a.length - 1; last >= 0; last--) {
        swap(a, 0, last);
        heapify(a, 0, last);
    }
}

// heapify for a max-heap:
private void heapify(int[] a, int root, int length) {
    int left = 2 * root + 1;
    int right = 2 * root + 2;
    int largest = root;

    if (left < length && a[largest] < a[left])
        largest = left;

    if (right < length && a[largest] < a[right])
        largest = right;

    if (largest != root) {
        swap(a, root, largest);
        heapify(a, largest, length);
    }
}
``` -->

### Counting Sort

<!-- ```java
public int[] sort(int[] a) {
    int max = findMax(a);
    int[] sorted = new int[a.length];
    int[] counts = new int[max + 1];

    for (int i = 0; i < a.length; i++)
        counts[a[i]]++;

    for (int i = 1; i < counts.length; i++)
        counts[i] += counts[i - 1];

    for (int i = 0; i < a.length; i++) {
        sorted[counts[a[i]] - 1] = a[i];
        counts[a[i]]--;
    }

    return sorted;
}

private int findMax(int[] a) {
    if (a.length == 0) return 0;

    int max = Integer.MIN_VALUE;
    for (int i = 0; i < a.length; i++) {
        if (a[i] > max)
            max = a[i];
    }
    return max;
}
``` -->

## Searching

### Binary Search

```python
def binary_search(input_array, value):
    n = len(input_array)
    i, j = 0, n
    while j >= i: # consider i==j too !
        m = int((j+i)/2)
        if input_array[m] == value:
            return m
        elif input_array[m] < value:
            # must go right
            i = m+1
        else:
            # must go left
            j = m-1
    return -1
```

## Selection

### Quickselect

<!-- ```java
public int quickselect(int[] a, int k) {
    return quickselect(a, k, 0, a.length - 1);
}

private int quickselect(int[] a, int k, int low, int high) {
    int pivot = partition(a, low, high);
    if (pivot == k) return a[pivot];
    else if (k < pivot) return quickselect(a, k, low, pivot - 1);
    else return quickselect(a, k, pivot + 1, high);
}

private int partition(int[] a, int low, int high) {
    int pivot = low;
    int rand = new Random().nextInt(high - low + 1) + low;
    swap(a, low, rand);

    for (int i = low + 1; i <= high; i++) {
        if (a[i] < a[pivot]) {
            swap(a, i, pivot + 1);
            swap(a, pivot, pivot + 1);
            pivot++;
        }
    }

    return pivot;
}
``` -->

## Graph Algorithms

<!-- Utility function:

```java
private void reset(Graph graph) {
    for (Vertex v : graph.vertices.values()) {
        v.parent = null;
        v.discovered = false;
        v.distance = Integer.MAX_VALUE;
    }
}
``` -->

### BFS

<!-- ```java
public void bfs(Graph graph, Vertex source) {
    reset(graph);
    Queue<Vertex> q = new LinkedList<>();
    q.add(source);
    source.discovered = true;

    while (!q.isEmpty()) {
        Vertex from = q.remove();

        for (Edge e : from.edges) {
            Vertex to = graph.vertices.get(e.to);

            if (!to.discovered) {
                to.parent = from;
                to.discovered = true;
                q.add(to);
            }
        }
    }
}

``` -->

### DFS

<!-- ```java
public void dfs(Graph graph) {
    reset(graph);

    for (Vertex v : graph.vertices.values()) {
        if (!v.discovered)
            dfs(graph, v);
    }
}

private void dfs(Graph graph, Vertex v) {
    v.discovered = true;
    // TODO: insert application of DFS here

    for (Edge e : v.edges) {
        Vertex to = graph.vertices.get(e.to);

        if (to.discovered) {
            // cycle found (back edge)! What should we do? depends on the application...
        } else {
            to.parent = v;
            dfs(graph, to);
        }
    }

    // TODO: insert application of DFS here. For example: if we're doing topological sorting
    //       then add v to head of a linked list at this point
}
``` -->

### Dijkstra

<!-- ```java
public void dijkstra(Graph graph, Vertex source) {
    reset(graph);
    source.distance = 0;
    PriorityQueue<Vertex> q = new PriorityQueue<>(graph.vertices.values());

    while (!q.isEmpty()) {
        Vertex from = q.remove();

        for (Edge edge : from.edges) {
            Vertex to = graph.vertices.get(edge.to);
            int newDistance = from.distance + edge.weight;

            if (newDistance < to.distance) {
                to.distance = newDistance;
                to.parent = from;
                q.remove(to);
                q.add(to);
            }
        }
    }
}
``` -->
