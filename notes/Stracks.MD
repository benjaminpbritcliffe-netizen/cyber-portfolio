# Stacks, Queues, DeQueues

Created: 9 April 2025 11:41
Class: Additional Research
Is Completed: Yes

Stacks - Data can only be placed on the top of the stack and can only retrieve data from the top of the stack.

Last In First Out (LIFO)

Implemented in python by using an array.

Let's explore these fundamental data structures in Python:

## Stacks

A stack follows the Last-In-First-Out (LIFO) principle. Think of it like a stack of plates - you can only add or remove from the top.

```python
# Using a list as a stack
stack = []
stack.append(1)    # Push
stack.append(2)    # Push
stack.pop()        # Pop (removes and returns 2)

```

## Queues

A queue follows the First-In-First-Out (FIFO) principle, like a line of people waiting.

```python
from collections import deque
queue = deque()
queue.append(1)       # Enqueue
queue.append(2)       # Enqueue
queue.popleft()       # Dequeue (removes and returns 1)

```

## Deques (Double-ended queues)

A deque allows adding and removing elements from both ends efficiently.

```python
from collections import deque
deque_obj = deque()
deque_obj.append(1)      # Add to right
deque_obj.appendleft(2)  # Add to left
deque_obj.pop()          # Remove from right
deque_obj.popleft()      # Remove from left

```

Key operations and their time complexities:

- **Stack**: push/pop - O(1)
- **Queue**: enqueue/dequeue - O(1) using deque
- **Deque**: append/pop from either end - O(1)

A priority queue is a data structure that works like a regular queue but assigns priorities to elements, which determine their dequeuing order. Unlike standard queues that use first-in-first-out ordering, a priority queue always removes the highest-priority element first, regardless of its position. Priority queues typically use heap structures for efficient operation, allowing both insertion and removal in logarithmic time. They're commonly used in task scheduling, pathfinding, and simulations where order of execution matters. Their unique structure makes them valuable tools for solving complex computational problems.

There are two main ways to implement a priority queue. The first uses an unsorted array, where new elements are added to the end, but finding the highest priority requires checking every element. The second uses a sorted array, which keeps elements in priority order—making it easy to get the highest-priority element but harder to insert new ones. Each approach offers different benefits for insertion speed versus retrieval speed.
