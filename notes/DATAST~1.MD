# Data Structures and algorithms

Language: Python

Binary Search:

When the sequence is sorted and indexable, there is a much more efficient
algorithm. (For intuition, think about how you would accomplish this task by
hand!) For any index j, we know that all the values stored at indices 0,..., j − 1
are less than or equal to the value at index j, and all the values stored at indices
j +1,...,n−1 are greater than or equal to that at index j. This observation allows
us to quickly “home in” on a search target using a variant of the children’s game
“high-low.” We call an element of the sequence a candidate if, at the current stage
of the search, we cannot rule out that this item matches the target. The algorithm
maintains two parameters, low and high, such that all the candidate entries have
index at least low and at most high. Initially, low = 0 and high = n− 1. We then
compare the target value to the median candidate, that is, the item data[mid] with
index

mid = (low +high)/2 .

This algorithm is known as binary search. We give a Python implementation
in Code Fragment 4.3, and an illustration of the execution of the algorithm in Figure 4.5. Whereas sequential search runs in O(n) time, the more efficient binary
search runs in O(logn) time. This is a significant improvement, given that if n
is one billion, logn is only 30. (We defer our formal analysis of binary search’s
running time to Proposition 4.2 in Section 4.2.)
1 def binary search(data, target, low, high):

2 ”””Return True if target is found in indicated portion of a Python list.
3
4 The search only considers the portion from data[low] to data[high] inclusive.
5 ”””
6 if low > high:
7 return False # interval is empty; no match
8 else:
9 mid = (low + high) // 2
10 if target == data[mid]: # found a match
11 return True
12 elif target < data[mid]:
13 # recur on the portion left of the middle
14 return binary search(data, target, low, mid − 1)
15 else:
16 # recur on the portion right of the middle
17 return binary search(data, target, mid + 1, high)
Code Fragment 4.3: An implementation of the binary search algorithm.
mid
high
low high
low mid
low mid
low=mid=high
high
14 19 22 25 27 28 33 37
6 7 8 9 10 11 12 13 14 15
2 9 754 8
2 4 5 7 8 12 14 17 9
37332827252219
2 4 5 7 8 12 14 17 19 22 25 27 28 33 37 9
19 22 25 27 28 33 37
01234 5
171412
2 4 5 7 8 12 17 9
Figure 4.5: Example of a binary search for target value 22.

Sequential Search:

When the sequence is unsorted, the standard approach to search for a target
value is to use a loop to examine every element, until either finding the target or
exhausting the data set. This is known as the sequential search algorithm

Low Level Arrays:

To accurately describe the way in which Python represents the sequence types,
we must first discuss aspects of the low-level computer architecture. The primary
memory of a computer is composed of bits of information, and those bits are typically grouped into larger units that depend upon the precise system architecture.

Such a typical unit is a byte, which is equivalent to 8 bits.

A computer system will have a huge number of bytes of memory, and to keep
track of what information is stored in what byte, the computer uses an abstraction
known as a memory address.

In general, a programming language keeps track of the association between
an identifier and the memory address in which the associated value is stored. For
example, identifier x might be associated with one value stored in memory, while y
is associated with another value stored in memory.

A group of related variables can be stored one after another in a contiguous
portion of the computer’s memory. We will denote such a representation as an
array

In Python, each character is represented using the Unicode
character set, and on most computing systems, Python internally represents each
Unicode character with 16 bits (i.e., 2 bytes).

Figure 5.2: A Python string embedded as an array of characters in the computer’s
memory. We assume that each Unicode character of the string requires two bytes
of memory. The numbers below the entries are indices into the string.
We describe this as an array of six characters, even though it requires 12 bytes
of memory

## **📖 The Algorithm Design Manual (3rd Edition) – Steven S. Skiena**

### **Section 1.5 – Mathematical Tools**

- Algorithms often involve mathematical concepts like logarithms, factorials, and summations.

An algorithm is a procedure to accomplish a specific
task. An algorithm is the idea behind any reasonable computer program

An algorithm is a procedure that takes any of the possible input instances
and transforms it to the desired output. There are many different algorithms
that can solve the problem of sorting. For example, insertion sort is a method
that starts with a single element (thus trivially forming a sorted list) and then
incrementally inserts the remaining elements so that the list remains sorted

- **Big-O Notation**: Used to describe an algorithm's efficiency and how it scales with input size.
- **Growth Rates**: Some functions grow faster than others (e.g., exponential vs. polynomial vs. logarithmic).
- **Recurrence Relations**: Used to analyze recursive algorithms (e.g., divide-and-conquer methods).
- Understanding these concepts helps in designing and analyzing efficient algorithms.

---

1. **Graph Theory (1.6)** – Graphs model relationships (nodes & edges), useful in networking, maps, and pathfinding.
2. **NP-Completeness (1.7)** – Some problems are hard to solve exactly (e.g., Sudoku, Traveling Salesman Problem).
3. **Algorithm Design Techniques (1.8)** – Greedy, divide & conquer, dynamic programming, and backtracking strategies.
4. **Data Structures (1.9)** – Arrays, linked lists, stacks, queues, trees, graphs, and hash tables.

---

## **📖 Data Structures and Algorithms in Python – Goodrich, Tamassia, Goldwasser**

Linear data structures organise data in a sequential manner, i.e. every element has only one element before and after it (except the first and last elements). Common linear data structures include.

- **Array**:
- **Description**: A collection or list of elements, each identified by an index
- **Example**: A list of finishers in a race with the finishing position

- **Linked List**:
- **Description**: A sequence of elements structured as nodes where each node contains data and a reference to the next node
- **Example**: A set of directions for a journey on the London underground, by station showing where to change and what line to change to from a start station to an end station

- **Stack**:
- **Description**: A collection of elements that follows Last-In-First-Out (LIFO) principle
- **Example**: Adding or removing a plate from a pile

- **Queue**:
- **Description**: A collection of elements that follows First-In-First-Out (FIFO) principle
- **Example**: A queue at a kiosk

Non-linear data structures do not arrange data sequentially. They are used to represent hierarchical relationships and connections among data. Common non-linear data structures include:

- **Tree**:
- **Description**: A hierarchical structure with a root node, where each node has zero or more child nodes
- **Example**: A family tree

**Binary Tree**:

- **Description**: A tree structure where each node has at most two children, often referred to as the left and right child
- **Example**: A tennis tournament draw

**Graph**:

- **Description**: A collection of nodes (vertices) connected by edges. Graphs can be directed or undirected
- **Example**: The London Underground map

1. **Stacks and Queues (4.1.3)**
    - **Stack (LIFO)**: Last in, first out (like a stack of plates).
    - **Queue (FIFO)**: First in, first out (like a waiting line).
    - **Deque (Double-ended queue)**: Can add/remove from both ends.
2. **Priority Queues & Heaps (5.2)**
    - **Priority Queue**: A queue where elements have priorities (e.g., emergency room patients).
    - **Heaps**: A tree-based structure that maintains the priority order efficiently.
    - **Min-Heap**: Smallest element at the top; **Max-Heap**: Largest element at the top.
3. **Heaps & Implementing Priority Queues (5.3 - 5.3.1)**
    - **Binary Heap**: A complete binary tree where the parent is smaller (or larger) than its children.
    - **Heapify**: Ensures heap structure is maintained after insertions/deletions.
    - Operations like insertions and removals take **O(log n)** time, making heaps efficient.