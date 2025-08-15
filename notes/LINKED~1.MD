# Linked Lists

Created: 16 April 2025 20:59
Class: Additional Research
Is Completed: Yes

I'll compare Python's built-in list with a linked list to show their key differences.

Unlike lists which use indexes and store elements consecutively in memory, linked lists use nodes scattered throughout memory, connected by pointers.

In a linked list, a "head" pointer indicates the first node and a "tail" points to the last. Each node connects to the next, with the final node pointing to none.

Now, let's examine the Big O complexity of linked list operations:

Appending (end): O(1) - Update tail pointer and add node
Removing from end: O(N) - Must traverse to find second-to-last node
Adding/removing from front: O(1) - Simply update head pointer
Inserting/removing from middle: O(N) - Must traverse to target location
Lookups (by value or index): O(N) - Must traverse from start

While lists excel at end operations and index lookups, linked lists offer faster operations at the beginning.

Let's look at the implementation. A node contains both a value and a pointer to the next node. When creating a linked list, we'll need:

1. A Node class to handle value and next pointer
2. A LinkedList class with head/tail pointers
3. Methods for adding and removing nodes

To create a linked list: `mylinklist = LinkedList(4)` - This creates a list with one node containing value 4.

Based on the selected text, here's a Python implementation of a basic linked list:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

```

This implementation follows the structure outlined in the notes, with a Node class containing value and next pointer, and a LinkedList class with head and tail pointers.

Key operations have the following time complexities:

- Appending: O(1)
- Prepending: O(1)
- Looking up elements: O(N)