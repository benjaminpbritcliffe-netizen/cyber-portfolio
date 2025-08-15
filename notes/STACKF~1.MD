# Stack Frame

Created: 26 March 2025 14:59
Class: 3
Is Completed: Yes

A stack frame is a data structure that stores information about the function called. Such as the Parameters, Local Variables and the return address.

Destroyed when the function returned

Last-In-First Out > 

That means the most recent stack frame is on

top of the stack, and it is the first one to be popped off when the function returns

Let's explore three fundamental data structures in Python: stacks, queues, and deques (double-ended queues).

## Stacks

A stack follows the Last-In-First-Out (LIFO) principle. Think of it like a stack of plates—you can only add or remove from the top.

```python
# Using a list as a stack
stack = []
stack.append(1)    # Push
stack.append(2)    # Push
stack.pop()        # Pop (removes and returns 2)

```

## Queues

A queue follows the First-In-First-Out (FIFO) principle, like people waiting in line.

```python
from collections import deque
# Using deque as a queue
queue = deque()
queue.append(1)      # Enqueue
queue.append(2)      # Enqueue
queue.popleft()      # Dequeue (removes and returns 1)

```

## Deques

A deque (double-ended queue) allows insertion and deletion at both ends.

```python
from collections import deque
deq = deque()
deq.append(1)        # Add to right
deq.appendleft(2)    # Add to left
deq.pop()           # Remove from right
deq.popleft()       # Remove from left

```

Common operations and their time complexities:

- **Stack**: push/pop - O(1)
- **Queue**: enqueue/dequeue - O(1)
- **Deque**: append/pop from either end - O(1)