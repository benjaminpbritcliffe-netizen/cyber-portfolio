# Loops

Created: 5 April 2025 15:08
Class: Additional Research
Is Completed: Yes

```python
x = 0

while x < 10:
    x +=1 #Increment by 1 each time
    print(x)

#Endless Loop

#while True:
 #   print('Something')

#For Loops iterate of a sequence
#Tell Python to do something so many time

for x in range(1,20):
    print(x)

x = 0
while x < 10:
    if x == 5:
        break #Loop control
    x +=1
    print(x)

x = 0
while x < 10:
    x +=1
    if x == 5: #Skips 5
        continue
    print(x)

#pass statement

if x == 25:
    pass #Passes the statement
print('Hello')
```

```python

words = 'the quick brown fox'

acc_letters = 'thequkcbrownfox'

wordlist = []

for word in words.split():
    if all(letters.lower() in acc_letters.lower() for letters in word):
        wordlist.append(word)

print(wordlist)

words = 'welcome my name is ben'

acceptedletters = 'welcoynaisb'

approved = []

for word in words.split():
    if all(letters.lower() in acceptedletters.lower() for letters in word):
        approved.append(word)

print(approved)

```

# For Loops and Nested Loops

## Transcript

A for loop executes a block of code a fixed number of times. You can iterate over ranges, strings, sequences, or any iterable object.

While both while and for loops can often be used interchangeably, for loops are better suited for fixed iterations, while while loops work better for indefinite iterations like user input.

Basic syntax: Use 'for x in range(start, stop)' with a colon and indented code block. The range function's stop value is exclusive. You can count backwards using reversed() or add a step parameter for counting by intervals.

For loops can iterate over strings - each character becomes the loop variable. Two helpful keywords are continue (skips current iteration) and break (exits loop entirely).

Nested loops are loops within other loops. The outer loop contains an inner loop in its code block. This creates a nested structure where the inner loop completes all its iterations for each iteration of the outer loop.

Example: To print a rectangle, use nested loops where the outer loop controls rows and the inner loop controls columns. Each loop iteration prints a symbol specified by user input.

The type of loops used in nesting doesn't matter - you can nest any combination of while and for loops as needed for your specific use case.

---

Made With Glean | [Open Event](https://app.glean.co/event/7720ff6f-66d1-40de-8942-012796df6d18)
