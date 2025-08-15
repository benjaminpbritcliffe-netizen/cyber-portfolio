# Data Structures and Algorithms

Created: 27 April 2025 19:01
Is Completed: Yes

https://www.youtube.com/watch?v=g2o22C3CRfU&t=42s&ab_channel=Fireship

[Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell](https://www.bigocheatsheet.com/)

Data Structures

Are specialised formats for organising and storing data to perform operation efficiently

Integers, Floats, Characters, Strings > Primitive Data Types

Linear Data Structures > Arranged in Linear/Sequential

Arrays, Linked Lists, Stacks and Queues

Non Linear

Trees, Graphs and Heaps

Algorithms

Step by step set of instructions or sequence of operations designed to perform a sepcific task or solve a particular problem

Algorithm Types:

Searching
Sorting

Graph

Tree

Big O Notation

We never keep the constants in a Big O Notation.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image.png)

Dominant Factor and Non Dominant

We always take the dominant O Notation. For example we have n * n times of an array, and a singular n loop.

we have an O(N^2 + n)  as N^2 is the dominant, we drop the non dominant factor as it has no impact on the time or space complexity.

Big O Notation measures the efficency of code based on runtime or space requirements

Time Complexity > Time it takes to run

Space Complexity > How much space it takes

Linear Complexity O(n)

scales proportionally with the input size.

As the input grows > The Time and Space grows linearly.

Plain English Example:

Consider a truck carrying one container that requires 100 liters of gasoline to reach its destination.

With two containers, it needs 200 liters of gasoline.

With three containers, it needs 300 liters of gasoline.

This demonstrates how the gasoline consumption increases linearly with the number of containers.

The fuel usage grows in direct proportion to the container count—a perfect example of linear complexity.

Code Example:

When the array size is 1, there will be 1 execution step.

When the array size is 2, there will be 2 execution steps.

When the array size is 100, there will be 100 execution steps.

This demonstrates how the number of execution steps increases linearly with the size of the input array.

In other words, if we represent the array size as N, the number of execution steps will also be N.

When an array has one element, there will be one execution step, and when the array has two elements, there will be two execution steps.

For an array of size N, the function will perform N execution steps, demonstrating linear time complexity (Big O).

The same principle applies to space complexity. The function has linear space complexity because it uses a forEach loop to copy all elements from the input array to a new array of the same size.

For example, if the input array has size one, the function will consume space for one element by creating a new array of the same size.

Similarly, if the input array has size N, the space consumed will also be N, indicating linear space complexity (Big O).

In essence, linear complexity means that an algorithm's execution time or space requirements increase proportionally with the input size.

O(1)

The amount of time or space consumed by an algorithm is constant and has no relation with the size of the input.

Plain English Example:

Consider a truck where we want to calculate its gasoline consumption to reach a destination while carrying containers.

When the truck carries one container, it uses 100 liters of gasoline to reach its destination.

If we increase to two containers, the truck still uses 100 liters of gasoline.

Even with three containers, the truck continues to use 100 liters of gasoline.

In this analogy, the truck represents the algorithm, and the containers represent the input.

The gasoline consumption represents the runtime.

No matter how much we increase the input size (number of containers), the gasoline consumption remains constant and isn't affected by the container count.

This illustrates how constant complexity works in computer science.

Code Example:

The function takes an input array and prints its size.

When the array contains one element, the line executes once, resulting in one execution step.

Even if the array size increases to 100, the line still executes just once because it simply prints the array's size, regardless of how many elements it contains.

Since the execution step remains constant (one) regardless of the input size N, we can say this function has O(1) or constant time complexity.

O(n^2)

Piece of code scaled quadratically.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%201.png)

Plain English Example:

Let's calculate how many liters of gasoline a truck needs to reach its destination based on the number of containers it carries.

While these numbers are simplified for the example, they illustrate the concept well.

With one container, the truck consumes one liter of gasoline.

With two containers, it consumes four liters of gasoline.

With three containers, it consumes nine liters of gasoline.

This shows that the gasoline consumption grows quadratically with the number of containers.

To relate this to computer science, think of the truck as an algorithm and the containers as the input to this algorithm.

The gasoline consumption represents the running time, which grows quadratically with the input size.

Code Example:

This code contains a nested loop structure where both the outer and inner loops iterate from 0 to N-1. Within the inner loop, we print the element at index j (the inner loop counter).

The outer loop executes N times, and for each of these iterations, the inner loop also executes N times. This results in N × N total executions.

Since the operation is executed N² times, the function has quadratic time complexity.

Quadratic complexity is generally inefficient, particularly for large inputs. While the performance impact may be negligible for small inputs, the execution time grows dramatically as the input size increases—much faster than linear or logarithmic algorithms.

Therefore, whenever possible, we should look for alternative algorithms with lower complexity, such as linear or logarithmic solutions.

O(log n)

Logrithmically with the size of an input

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%202.png)

The best way to understand logarithmic complexity is through an example of binary search finding a specific element in a sorted array.

Let's examine how this works. Suppose we want to find the position of element T2 in a sorted array.

The process works by locating the middle element of the array and comparing our target element against it.

If our target is smaller, we eliminate the right half of the array and continue our search in the left half.

This process divides the array in half at each step until we either find our target element or narrow down to a single element.

In this array, we find that the middle element is 10, which is larger than 2.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%203.png)

Therefore, we eliminate that half and continue searching in the left half.

Within the left half, we find the middle element is 6, which is larger than 2.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%204.png)

So we eliminate that half and continue searching in the remaining portion. The new middle element is 4, which is larger than 2.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%205.png)

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%206.png)

After removing this half, we're left with just one element—2—which is exactly what we were looking for.

Throughout this process, we divided the input array by 2 at each step.

Let's count how many steps it took: we divided the array by two until we either found our target element or reached a single element. In this case, it took 1, 2, 3 steps.

We divided the input array by two three times before reaching a single element.

In mathematics, when you divide a number by 2 repeatedly until you reach 1, this is called a logarithm to base 2.

In our example, log₂(8)—where 8 is the size of our input array—equals 3, which matches the number of steps we performed.

This demonstrates that the runtime complexity is O(log n), where n represents the size of the input array.

Complexity Comparison

Input Size vs Time or Space Complexity:

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%207.png)

Conclusion of Big O Notation:

Big O notation is specifically designed to describe how an algorithm’s efficiency changes with different input sizes, helping you understand its performance.

O(n) complexity means its runtime increases in direct proportion to the input size

O(1) means the algorithm’s running time stays the same no matter how large the input grows, demonstrating constant time complexity

Big O notation focuses on how an algorithm’s performance grows with input size, so constant factors don’t affect this growth and are therefore ignored

O(n)

```python
def example1(arr):
    for num in arr:
        print(num)
```

the function processes each element in the input array once, so its running time grows linearly with the input size

O(log n)

```python
def function1(n):
    if n <= 0:
        return
    function1(n // 2)
```

Each call halves the problem size, so the total steps grow slowly and proportionally to the logarithm of n.

Time: O(n)

Space: O(1)

```python
 def my_function(nums):
    total = 0
    for num in nums:
        total += num
    return total
```

because the function goes through each item once (O(n) time), but only keeps a single running total, so it uses constant space (O(1)).

Time: O(n)

Space: O(n)

```python
def my_function(nums):
    squares = []
    for num in nums:
        squares.append(num ** 2)
    return squares
```

the function creates a new list to store the squares of all input numbers, so both the time to process each element and the space to store all results grow linearly

Linked Lists

A collection of data elements where the order is determined by connections between elements rather than their physical location in memory. Each element points to the next element in the sequence.

Nodes contain two components: data and a pointer to the next node.

The "head" points to the first node in the list.

The "tail" tracks the last node in the list.

Since nodes can be placed anywhere in memory, their physical locations are not sequential.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%208.png)

How adding a linked list works.

Let's start with adding a new element at the beginning of the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%209.png)

In this example, we want to add element 2 to the beginning. We'll make element 2's "next" pointer point to element 4, which is currently the first element in the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2010.png)

Since the head node always points to the first node in the linked list, we'll update the head to point to element 2, making it the new first element.

Next, let's add element 2 between elements 6 and 8 in the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2011.png)

To do this, we'll make node 6's "next" pointer point to node 2, and node 2's "next" pointer point to node 8. This effectively inserts element 2 between elements 6 and 8.

Now, let's see how to append an element to the end of the linked list.

Let's add element 10 to the end. Currently, element 8 is the last element, and its "next" pointer points to null.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2012.png)

We'll update element 8's "next" pointer to point to element 10 instead of null.

Since element 10 is now the last element, its "next" pointer will point to null.

We'll also update the tail to point to element 10, as it's now the last element in the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2013.png)

Finally, let's consider adding element 10 to an empty linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2014.png)

In this case, element 10 will be both the first and last element in the linked list.

Append Linked List

First, we create a new node by instantiating the node class with our value.

Next, we need to update the pointers. The last node (accessed through the tail pointer) should point to our new node.

Finally, we move the tail pointer to the new node, making it the last element in the list.

That's all we need to do for a basic append. Feel free to review the animation if you need to visualize these steps.

However, we need to handle an important edge case: appending to an empty linked list.

In this case, both head and tail pointers should point to the new node, since it will be the only element in the list.

To implement this, we first check if the list is empty by seeing if the head pointer is None.

If the list is empty, we assign both head and tail to point to the new node.

Otherwise, we execute our standard append code for non-empty lists.

You might wonder why we don't explicitly set the new node's next pointer to None.

This is because the node class constructor already handles this—whenever we create a new node, its next pointer is automatically set to None.

Prepend:

First, we create a new instance of the node class with our value as an argument.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2015.png)

Next, we set the new node's next pointer to point to the current head of the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2016.png)

Finally, we update the head pointer to point to our new node, making it the first element in the list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2017.png)

That's all there is to prepending a node!

However, we still need to handle one special case: prepending a node to an empty linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2018.png)

In this case, we check if the tail is null, which indicates that the linked list was empty before adding the new node.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2019.png)

Since the new node will be the only node in the linked list, we must make both head and tail point to it.

Iterating over a linked list

Let's say we have a linked list and want to iterate through all its elements to print each one.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2020.png)

To do this, we need a way to traverse the linked list nodes.

We'll create a special node called an iterator for this purpose.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2021.png)

First, we'll point our iterator to the head (first node) of the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2022.png)

Then we'll check if the current node (starting with the head) is not null—in other words, if the list is not empty.

If it's not null, we'll display the current node's value and move our iterator to the next node.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2023.png)

We'll repeat this process: check if the current node is null, and if it's not, display its value.

We'll continue these steps until we reach the last node.

At the last node, we'll print its value and move to the next node, which will be null.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2024.png)

When we hit null, we stop iterating since we've reached the end of the list.

```python

    def iterate(self):
        iterator = self.head
        while iterator:
            print(iterator.value + ' ')
            iterator = iterator.next
```

Remove Elements

When removing an element from a linked list, there are four possible scenarios.

The element could be at the beginning of the list, at the end of the list, or somewhere in between.

The fourth case is when the element is the only one in the list.

Let's explore how removal works in each of these scenarios.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2025.png)

Let's start by removing an element from the beginning of the linked list—that is, the first element.

In this example, we want to remove element 2. To do this, we simply move the head pointer to node 4 and delete node 2.

That's all there is to it. Node 2 is now deleted, and node 4 becomes the first element in the linked list.

‘

Now let's say we want to delete element 6, which is in the middle of the linked list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2026.png)

In this case we will let the pointer that points to the next node in node 4 point to node 8 instead of 6 and delete node 6 and that's it.

Now let's remove element 8, which is at the end of the linked list.

In this case, we need to update the tail to point to node 4, which is the node before node 8.

However, this raises an important question: how do we find the node that comes before the last node in the linked list?

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2027.png)

Remember that each node only has a pointer to the next node, not the previous one.

Therefore, to find the node before the tail, we must iterate through the linked list from the head until we reach it.

In this example, node 4 is the first node in the linked list, though in other cases the node before the tail could be anywhere in the list.

We need to move the iterator through the list until we reach this node.

Once found, we update the tail to point to this node and set its next pointer to null, making it the new last node in the list.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2028.png)

At this point, node 4 is both the first and last element in the linked list, so both head and tail point to it.

Now let's say we want to remove node 4 from this linked list.

To do this, we'll simply delete the element and set both the head and tail pointers to null.

![image.png](Data%20Structures%20and%20Algorithms%201e23d034d9f780e29dffeffb1cb317df/image%2029.png)

The linked list is now empty.

Big O of Linked List:

Prepend: O(1)

Deleting 1st node: O(1)

Appending at end: O(1)

Traversing: O(n)

Searching: O(n)

Inserting a new node: O(n)

Removing Node (Other than first node): O(n)

Adding a new node at the beginning of a linked list is called a prepend operation. This operation has constant time complexity (O(1)) because it only requires two steps: pointing the new node to the current first node and updating the head pointer to the new node. The number of steps remains constant regardless of list size.

Deleting the first node also has constant time complexity (O(1)). We simply update the head to point to the second node, and that's it. Again, the number of steps doesn't depend on list size.

Appending (adding a node at the end) has constant time complexity because we only need to update two pointers: the current last node's next pointer and the tail pointer. Both point to the new node, and these steps remain constant regardless of list size.

Traversing a linked list has linear time complexity (O(n)) because we must visit every node in the list. Similarly, searching has linear time complexity since we need to iterate through nodes until finding the target element.

Inserting a new node after an existing node has linear time complexity. First, we must iterate to find the target position (O(n)). Then, we perform the actual insertion by updating pointers, which is constant time. The overall operation remains linear.

Finally, removing a node (except the first node) has linear time complexity. We must first iterate to find the node before the one we want to delete (O(n)). Then we update the pointer to skip over the deleted node—a constant time operation. Because of the initial traversal, the total operation has linear time complexity.

When we should use linked lists:

If you need constant time insertions or deletions. Time complexity compared to arrays is better.

Unknown number of items as a linked list is dynamics.

Want to insert items in the middle. 

```python
class Node:
    def __init__(self,value):
        self.value = value #Value
        self.next = None #Pointer

class LinkedList:
    def __init__(self):
        self.head = None #First
        self.tail = None #Lase

    def append(self,value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head =new_node
        if not self.tail:
            self.tail = new_node

    def iterate(self):
        iterator = self.head
        while iterator:
            print(iterator.value + ' ')
            iterator = iterator.next

    def remove(self,value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        iterator = self.head
        while iterator.next:
            if iterator.next.value == value:
                iterator.next = iterator.next.next
                if not iterator.next:
                    self.tail = iterator
                return
            iterator = iterator.next

class ShoppingCart:
    def __init__(self):
        self.items = LinkedList()

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        self.items.remove(item)

    def display_cart(self):
        print("Items in the shopping cart: ")
        self.items.iterate()

cart = ShoppingCart()
cart.add_item('Apple')
cart.add_item('Banana')
cart.add_item('Orange')

cart.display_cart()

cart.remove_item('Orange')
cart.display_cart()
```