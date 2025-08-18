# Sets

Created: 11 April 2025 15:57
Class: Additional Research
Is Completed: Yes

Sets are an unordered collection of unique items. This means they don't maintain any fixed order or index, and they don't allow duplicate elements.

You can create a set using curly braces with comma-separated elements, or by using the set constructor on an iterable object like a list or string.

For example, to create a set of fruits: {apple, banana, orange, mango}.

Since sets are unordered, Python doesn't guarantee any particular order for them.

A key feature of sets is that they don't allow duplicates.

When you try to add an element that already exists in the set, it will be ignored.

You can remove elements from a set using the remove method.

If you try to remove an element that isn't in the set (like "peach"), the remove method will raise a key error.

To avoid this, use the discard method instead.

The discard method won't raise an error if the element isn't in the set.

Sets are commonly used to remove duplicates from lists or strings.

For example, if you have a list of names with repetitions, converting it to a set will give you only the distinct names.

Similarly, converting a string to a set will give you its unique characters.

You can remove duplicates from a list by converting it to a set and back to a list.

Sets also support mathematical operations like union, intersection, difference, and symmetric difference.

These operations return new sets containing the results of combining or comparing two sets.

For example, the union method creates a set containing all elements from two sets.

Given sets colors1 and colors2, the union colors1.union(colors2) contains all colors from both sets.

Lists are ordered, maintaining a specific sequence of items.

Sets, however, are unordered with no guaranteed item sequence.

Unlike lists, sets don't allow duplicate items.

If you need unique items in your collection, a set is often the better choice.

Lists are mutable, letting you add or remove items.

Sets are also mutable, but their elements must be immutable.

Checking if an item exists in a set is faster than checking a list.

Lists must scan through all elements sequentially until finding a match or reaching the end.

Sets use hashing to quickly locate items without scanning through all elements.

Hashing assigns a unique code to each item and stores it in a table based on this hash value.

This allows sets to access items directly using their hash values, without comparing them to other items.

Sets use more memory than lists.

Using the sys module, we can measure each object's size in bytes.

The measurements show that sets use more memory than lists, even with the same number of elements.

```python

numbers = [1,1,2,3,4]

unique = set(numbers)
second = {1,5}
second.add(5)

print(second)
print(unique)

print(unique | second)
print(unique & second)
print(unique - second)
print(unique ^ second)

if 1 in unique:
    print('yes')
    

```

Welcome! Today we'll explore Python sets. I recently read an interesting article about their various use cases, which inspired me to create this tutorial.

Sets are an often overlooked data type, yet they're powerful for solving specific problems—particularly in coding interviews where efficiency matters.

In this tutorial, we'll explore practical examples of sets. First, let's understand what a set is: it's like a list but with one key difference—it automatically removes duplicate values.

Sets have special methods not found in other data types. You can use the intersection method to find elements that appear in multiple sets, or the difference method to find elements unique to one set. This makes sets valuable when comparing collections, such as finding items present in one list but not another.

Let's start with basic examples. To create a set, we can pass a list of values to the set() function. When we create a set containing numbers one through five and print it, you'll notice it looks like a list but uses curly braces instead of square brackets.

We can also create a set directly using curly braces, similar to a list but with curly braces instead of square brackets. Both methods produce the same result.

Important note: to create an empty set, you can't use empty curly braces {} since that creates an empty dictionary. Instead, use set() with no arguments.

To demonstrate how sets handle duplicates, let's add the numbers 1, 2, and 3 to our existing set that already contains these values. When we run the code, we still only get numbers 1 through 5—the duplicates are automatically removed.

Here's code that demonstrates how sets handle duplicates:

```python
# Create a set with initial numbers
numbers = {1, 2, 3, 4, 5}

# Try adding duplicate numbers
numbers.add(1)
numbers.add(2)
numbers.add(3)

print(numbers)  # Output: {1, 2, 3, 4, 5}

```

As shown, even when we try to add duplicate values, the set maintains only unique elements. This is because sets don't allow duplicates.
