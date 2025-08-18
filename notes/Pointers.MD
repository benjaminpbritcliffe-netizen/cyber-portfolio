# Pointers

Created: 16 April 2025 12:50
Class: Additional Research
Is Completed: Yes

How pointers work with different data types

How pointers work differently with different data types.

Let's start with a variable called num1. We'll set it equal to an integer 11, and then create a second variable called num2, setting it equal to num1 = 11.

When we do this, we create an integer 11 somewhere in memory and point the variable num1 at that integer.

What happens when we set num2 to equal num1?

num1 and num2 point to the exact same address—they both point to the same number 11 in memory.

Now, what happens if we set num2 to equal 22? Does the 22 overwrite the 11, making both num1 and num2 point to 22? Or do we create a separate integer somewhere else in memory and have num2 point to that?

```python
# Initial setup
id1 = num1 = 11    # Creates integer 11 in memory, num1 points to it
id2 = num2 = num1  # num2 points to same memory location as num1

# Memory representation
print(f"ID: {id1} Value: {num1}")  # Both point to same memory location
print(f"ID: {id2} Value: {num2}")  # with value 11

# When num2 is changed to 22
num2 = 22          # Creates new integer 22 in memory
id2 = num2         # num2 now points to new memory location

# Final memory state
print(f"ID: {id1} Value: {num1}")  # Original memory location, still 11
print(f"ID: {id2} Value: {num2}")  # New memory location, value 22

```

This code demonstrates how integers work with memory addresses. When we change num2's value, a new memory location is created because integers are immutable.

This diagram shows how it works.

Integers are "immutable," which means they cannot be changed.

Once you put the number 11 into a particular place in memory, you cannot change that number 11.

You can point num1 to a different integer stored somewhere else, but you can't change the original number 11.

Let's look at another data type that works differently from integers.

I'll create a dictionary called Dictionary1 and set it equal to value 11. This variable points to the dictionary in memory.

If we create Dictionary2 and set it equal to Dictionary1, do we create an identical dictionary elsewhere in memory for Dictionary2 to point to, or does Dictionary2 point to the same dictionary?

They both point to the same dictionary.

This behavior is similar to working with integers.

But what if we set Dictionary2's value to 22? Do we overwrite the 11, or create a second dictionary for Dictionary2 to point to?

Let's create Dictionary1 with value 11, then set Dictionary2 equal to Dictionary1.

When we print out Dictionary1 and Dictionary2 and look at their memory addresses, we can see they point to the same address in memory.

Now, let's change Dictionary2's value to 22 and print out both dictionaries' values and addresses again.

After updating, both Dictionary1 and Dictionary2 have value 22. This differs from how integers behave.

Notice that Dictionary1 and Dictionary2 still point to the same address—identical to before the update.

Here's the code demonstration of how dictionaries behave with pointers in Python:

```python
# Create initial dictionaries
dict1 = {'value': 11}
dict2 = dict1  # Both point to same dictionary

# Print initial state
print(f"Dict1 ID: {id(dict1)}, Value: {dict1['value']}")
print(f"Dict2 ID: {id(dict2)}, Value: {dict2['value']}")

# Modify dict2's value
dict2['value'] = 22  # Changes both dictionaries since they point to same object

# Print final state - both dictionaries are changed
print(f"Dict1 ID: {id(dict1)}, Value: {dict1['value']}")
print(f"Dict2 ID: {id(dict2)}, Value: {dict2['value']}")

```

When run, this code will show that both dictionaries share the same memory address and changing one affects the other.

In a linked list, nodes behave similarly to dictionaries.

When two variables point to the same node, you can change that node's value.

The variables continue pointing to the same node even after changing its value from 22 to 44.

Let's change this back to 22 and demonstrate a few other dictionary concepts.

Say we create Dictionary3 with value 33.

Here's another important concept: if we set Dictionary1 equal to Dictionary2, all three variables will point to the same dictionary.

Here's how to demonstrate the linked list node behavior in Python:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create nodes and set pointers
node1 = Node(22)
node2 = node1  # Both variables point to same node

print(f"Node1 value: {node1.value}")  # 22
print(f"Node2 value: {node2.value}")  # 22

# Change value through node2
node2.value = 44  # Changes value for both since they point to same node
print(f"Node1 value: {node1.value}")  # 44
print(f"Node2 value: {node2.value}")  # 44

# Memory addresses will be the same
print(f"Node1 id: {id(node1)}")
print(f"Node2 id: {id(node2)}")

```

This code demonstrates how nodes behave similarly to dictionaries, where multiple variables can point to the same node and changing the value through any variable affects what all variables see.

What happens to the original dictionary that nothing points to anymore?

Without any variables pointing to it, we can't access it.

Python handles this through a process called garbage collection, removing the unreferenced dictionary.

And that is our overview of pointers.

Based on the context, here are the key differences between how pointers work with integers versus dictionaries in Python:

**Integers (Immutable):**

- When integers are assigned to variables, they point to specific memory locations
- Integers cannot be changed once created in memory - they are immutable
- When reassigning an integer variable, it points to a new memory location rather than modifying the original value

**Dictionaries (Mutable):**

- When multiple variables point to the same dictionary, they share the same memory address
- Modifying a dictionary through any variable that points to it will change the value for all variables pointing to that dictionary
- When a dictionary loses all references pointing to it, Python's garbage collection removes it from memory.
  