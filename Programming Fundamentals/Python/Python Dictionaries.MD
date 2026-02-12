# Dictionaries in Python

Created: 9 April 2025 18:54 Class: 5 Is Completed: Yes

[Python 🐍](../Research%20Paper%20Planner%201763d034d9f780cb993bf4554600d5e7/Reading%20List%201763d034d9f781f7bbbfddf4a9dfb052/Python%20%F0%9F%90%8D%2018f3d034d9f7800d8e24c046970152d9.md)

[Dictionaries](Dictionaries%20in%20Python%201d03d034d9f7800aa1ddc869f0153fbd/Dictionaries%201d03d034d9f7816baac5da9ff4aec80b.md)

```python

dict1 = {
    'jan' : 'january',
    'feb' : 'february',
    'mar' : 'march'
}

print(dict1['jan'])

people ={
    'BPB' : 'Ben',
    'HJB' : 'Henry'
}

print(people['BPB'])
```

## Transcript

In this lecture, we'll explore Python dictionaries - their creation, usage, and
comparison with other data structures.

Dictionaries (also called hash tables or maps) are key-value data structures in
Python that let you store and access data using immutable keys.

A dictionary is an unordered collection where each unique key maps to a value.
Create them using curly braces with comma-separated key-value pairs. Keys must
be immutable (strings, numbers, tuples, etc.).

Access values using square bracket notation with the key name. Add new pairs by
assigning values to new keys. Update existing values by reassigning. Remove
entries using del or pop().

Common methods include:

- keys(), values(), items() for accessing dictionary contents
- get() to safely retrieve values with defaults
- setdefault() to set values only if key doesn't exist
- update() to merge dictionaries
- clear() to remove all entries

To iterate through dictionaries, you can:

1. Loop through keys directly
2. Use items() to access key-value pairs
3. Use dictionary comprehensions for transformations

Compared to lists and sets: Advantages:

- Access by meaningful keys instead of indices
- Constant-time lookups using hashing
- Flexible key-value associations Disadvantages:
- Unordered (before Python 3.7)
- More memory usage
- Cannot be sorted directly

Note: Since Python 3.7, dictionaries maintain insertion order, though you
shouldn't rely on this for backwards compatibility.

In summary, dictionaries excel at storing and accessing data by meaningful keys
rather than position, making them ideal for many data organization tasks.

Thank you for watching and see you in the next video.

Here's a comprehensive example demonstrating the dictionary methods discussed:

```python
# Creating and accessing a dictionary
months = {
    'jan': 'January',
    'feb': 'February',
    'mar': 'March'
}

# Accessing values
print(months['jan'])  # January
print(months.get('apr', 'Not found'))  # Safe access with default

# Adding and updating
months['apr'] = 'April'  # Add new pair
months['jan'] = 'JANUARY'  # Update existing

# Dictionary methods
print(months.keys())  # Get all keys
print(months.values())  # Get all values
print(months.items())  # Get all key-value pairs

# Iterating through dictionary
for key in months:
    print(key)

for key, value in months.items():
    print(f"{key}: {value}")

# Dictionary comprehension
upper_months = {k: v.upper() for k, v in months.items()}

# Merging dictionaries
other_months = {'may': 'May', 'jun': 'June'}
months.update(other_months)

# Removing items
del months['jan']
popped_value = months.pop('feb')

# Clear dictionary
months.clear()
```

This example demonstrates all the key concepts discussed in the lecture,
including creation, access, modification, iteration, and common methods.

---

Made With Glean |
[Open Event](https://app.glean.co/event/f44d3023-3343-46b0-932c-9f29ef134f35)
