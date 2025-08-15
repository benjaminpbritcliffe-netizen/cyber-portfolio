# For Loop

Created: 17 March 2025 14:51
Class: 1
Is Completed: Yes

for counter in range(start, end, step);

for x in range(2, 30, 3):
print(x)

# Python For Loops

A for loop iterates over a sequence—which can be a list, tuple, dictionary, set, or string.

Unlike the for keyword in other programming languages, Python's for loop functions more like an iterator method found in object-oriented programming.

Using a for loop, we can execute a set of statements once for each item in a sequence like a list, tuple, or set.

# Example

Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]

for x in fruits:  

print(x)

```python
words = 'The quick brown fox'
allowed_letters = 'thequickbronfox'
wordlist = []

for word in words.split():
    if all(letter.lower() in allowed_letters.lower() for letter in word):
        wordlist.append(word)
print(wordlist)

```
