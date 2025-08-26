# Big O Notation

Analysis of how well an algorithm will perform.

Big O Notation describes the upper bound of an algorithm's growth rate. In other
words, it tells you how the runtime or memory usage of an algorithm increases as
the input size (n) increases.

It abstracts away constants and less significant terms, focusing on the most
impactful part of the growth rate.

<https://www.youtube.com/watch?v=aWKEBEg55ps&ab_channel=GregHogg>

## Binary Search

Binary search is a way to find things quickly by checking the middle of a sorted
list and eliminating half the remaining items each time. Think of it like
finding a word in a dictionary - you open to the middle, see if your word comes
before or after that page, and then only look in that half.

To understand how fast binary search works, we use something called logarithms:

- A logarithm (base 2) tells us how many times we need to cut something in half
- For example: If you start with 8 items and keep dividing by 2, you need to do
  it 3 times to get to 1 (8 → 4 → 2 → 1)

A helpful example: Think about the number 100. If we ask "how many times do we
multiply 10 by itself to get 100?" the answer is 2 (10 × 10 = 100). That's what
we call log10 100 = 2. Logarithms are just the opposite of multiplication.

### Big O Notation Explained Simply

Big O notation is a way to measure how well a program will run as it handles
more data. It's like measuring fuel efficiency in a car - we want to know how
well it performs under different conditions.

## How Different Programs Perform

| **Speed Rating** | **Name**     | **What It Means**                   | **Common Uses**             | **How Well It Works** |
| ---------------- | ------------ | ----------------------------------- | --------------------------- | --------------------- |
| O(1)             | Constant     | Always takes the same time          | Looking up items directly   | Excellent             |
| O(log n)         | Logarithmic  | Gets slightly slower with more data | Binary search               | Very good             |
| O(n)             | Linear       | Time increases with data size       | Checking each item once     | Good                  |
| O(n log n)       | Linearithmic | Somewhat faster than squared        | Good sorting methods        | Fair                  |
| O(n²)            | Quadratic    | Gets much slower with more data     | Simple sorting              | Poor                  |
| O(2ⁿ)            | Exponential  | Gets very slow very quickly         | Complex problem-solving     | Very poor             |
| O(n!)            | Factorial    | Extremely slow with more data       | Finding all possible orders | Terrible              |

![image.png](Big%20O%20Notation%20Recap%201c83d034d9f780c99fdcfe0ba323aeb7/image%201.png)

```python
a = 10
b = 20
c = 30
d = 40
e = 50

array = [10,20,30,40,50]

#O(1)
print(array[1])

#O(n)

while d < e:
    print(d)
    d +=1

#O(n2)

for n in range(10, 20):
    print(n)
    for o in range(20, 30):
        print(o)


#O(n3)
for n in range(10, 20):
    print(n)
    for o in range(20, 30):
        print(o)
        for p in range(30,40):
            print(p)


#O(n log n)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0  # count how many steps it takes

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        print(f"Step {steps}: low={low}, high={high}, mid={mid}, checking {arr[mid]}")

        if arr[mid] == target:
            print(f"Found {target} at index {mid} in {steps} steps.")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} is less than {target}, searching right half.")
            low = mid + 1
        else:
            print(f"{arr[mid]} is more than {target}, searching left half.")
            high = mid - 1

    print(f"{target} not found after {steps} steps.")
    return -1

binary_search(array,20)
```

Big O notation helps us understand how fast or slow our code will run. It's an
important tool for writing better programs.

Think of it this way: If you have two programs that do the same thing, how do
you know which one is better? It's not just about which one finishes faster on
your computer. A program might be quick on a fast computer but slow on a slower
one. That's why we count the number of steps (operations) instead of measuring
time in seconds.

When we write programs, we need to think about two things:

- How fast the program runs (time efficiency)
- How much computer memory it uses (space efficiency)

Sometimes a fast program uses lots of memory, while a slower program uses less.
You need to choose what's more important for your specific needs.

When measuring program efficiency, we usually focus on three scenarios:

- Best case: When everything works perfectly (like finding what you want
  immediately)
- Average case: What usually happens most of the time
- Worst case: When things take the longest (like having to look through
  everything)

When we talk about Big O notation, we're usually talking about the worst case -
we want to know how bad things might get.

The simplest example is O(n), where n is the amount of data. If you have a list
of 100 items and need to check each one, that's O(n) because you might need to
look at all 100 items.

Here's a helpful tip: When we write Big O notation, we keep it simple. If a
program needs to do something twice, we might think it's O(2n), but we just
write it as O(n). Whether it's O(2n), O(10n), or O(100n), we simplify it to
O(n).

In simple terms, Big O notation tells us how well a program will handle more
data. It helps programmers write better, more efficient code.

The main things to remember about Big O notation:

- It measures how many steps a program takes, not how many seconds
- It looks at both speed and memory usage
- We always simplify the notation (O(2n) becomes O(n))

Different types of programs range from very fast O(1) to very slow O(n!), and
choosing the right approach depends on what you need to accomplish.
