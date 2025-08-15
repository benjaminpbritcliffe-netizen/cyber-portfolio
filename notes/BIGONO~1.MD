# Big O Notation

Created: 25 March 2025 11:42
Class: 3
Is Completed: Yes

Speed an Efficiency

### **Common Big O Classes (from fast to slow)**

| Big O | Name | Example | n |
| --- | --- | --- | --- |
| O(1) | Constant | Accessing an array item | Operation takes the same amount of time, no matter how much data there is. |
| O(log n) | Logarithmic | Binary search | Splits the sort in half. |
| O(n) | Linear | Loop through list | As the data increases the time increases |
| O(n log n) | Linearithmic | Merge sort, quicksort (avg) |  |
| O(n²) | Quadratic | Nested loops | Each item in a dataset has to interact with each other. |
| O(2^n) | Exponential | Recursive Fibonacci |  |
| O(n!) | Factorial | Brute-force permutations |  |

### **5. Use This Rule of Thumb Table**

| Pattern | Time Complexity |
| --- | --- |
| Access by index | O(1) |
| Single loop over input | O(n) |
| Loop inside a loop | O(n²) |
| Divide input each step | O(log n) |
| Sort input with divide & conquer | O(n log n) |
| All subsets / combos | O(2ⁿ) |
| All permutations | O(n!) |

### **Big O Analogies with Cookies**

| Big O | Analogy | What It Means |
| --- | --- | --- |
| **O(1)** | You reach into a cookie jar and grab a cookie—no matter how many there are. | Constant time. Doesn’t matter if the jar has 1 or 1 million cookies. |
| **O(log n)** | You split the cookie jar in half repeatedly to find the chocolate chip one. | Like binary search. Cuts the problem in half each time. Super efficient. |
| **O(n)** | You check each cookie one by one until you find the chocolate chip one. | Linear time. More cookies = more time. |
| **O(n log n)** | You organize the cookies by flavor using a clever sorting system. | Efficient sorting. A bit slower than linear, but still manageable. |
| **O(n²)** | For every cookie, you compare it to every other cookie. | Quadratic time. Gets slow fast—Like comparing each cookie taste to every other cookie. Gets tiring fast. |
| **O(2ⁿ)** | For each cookie, you try all combinations of adding toppings (chocolate, nuts, sprinkles, etc.). | Exponential growth. The number of combinations explodes. |
| **O(n!)** | You try every possible way to arrange the cookies in a line. | Factorial time. Way too many options—it becomes unmanageable very quickly. |

---

### **How it Feels in Real Life**

- **O(1)**: Like grabbing your favorite cookie instantly.
- **O(log n)**: Like using a smart trick to find it quickly in a pile.
- **O(n)**: You’re methodically searching—still fine unless there are *a lot*.
- **O(n²)**: Like comparing each cookie to every other cookie. Gets tiring fast.
- **O(n!)**: You’re making a line-up of cookies in every possible order. Who has time for that?
- **O(2ⁿ)**: You’re exploring all possible topping combos. Tasty... but slow.

![image.png](Big%20O%20Notation%201c13d034d9f780baa27ee11f4ea53f1d/image.png)

### 🚨 Is Big O Just Theory?

Not at all! Understanding Big O helps you:

- Choose the right **algorithm or data structure**
- Avoid building code that works on small data but **chokes on big data**
- Identify and fix **performance bottlenecks**

### 💡 When Would You Use It?

Here are **real-world scenarios** where Big O impacts your work as a developer or analyst:

---

### ✅ **1. Searching Data**

**Scenario**: You need to find a record in a database or a value in an array.

- **Linear search (O(n))** = fine for 10 items, terrible for 10 million.
- **Binary search (O(log n))** = *amazing* if the data is sorted.

👉 **Control**: You choose the algorithm. This is in your hands.

---

### ✅ **2. Sorting Data**

**Scenario**: You're sorting names, scores, files, etc.

- **Bubble sort (O(n²))** = easy to write, but slow.
- **Merge sort or Timsort (O(n log n))** = fast even on big lists.

👉 In Python, `sorted()` is already optimized with **Timsort (O(n log n))**—but if you wrote your own, **Big O makes or breaks performance**.

---

### ✅ **3. Combinations or Subsets**

**Scenario**: You’re writing code to generate **all subsets**, combinations, or permutations (like in machine learning, brute force cracking, or puzzle-solving).

- These problems often fall into **O(2ⁿ)** or **O(n!)**
- Very quickly become **too slow**, so you need smarter strategies (e.g. memoization, pruning, dynamic programming)

👉 **Control**: You can often redesign the approach to avoid full brute force.

---

### ✅ **4. Front-End and API Optimization**

**Scenario**: You're looping through DOM elements, or building a report dashboard.

- Nested loops? O(n²)? May work fine on a few rows, but laggy on 1000+.
- Fixing this might mean caching, pagination, or chunking.

👉 **Control**: This is entirely under your control as a developer.

---

### ❌ **When It’s Out of Your Control**

Sometimes, you’re using third-party tools, databases, or libraries.

- A database’s **query planner** decides how fast something runs.
- An API might **limit results or throttle calls**, regardless of your algorithm.

But even then, **knowing Big O helps you work smarter within those limits**.

```python

'-- O(n2)

cars1 = ['Honda','Mazda','Jeep','Nissan']

cars2 = ['Mercedes','Fiat','Honda','Nissan']

for car in cars1:
    for car2 in cars2:
        if car == car2:
            print(car)

'--  O(n)'
cars1 = ['Honda', 'Mazda', 'Jeep', 'Nissan']
cars2 = ['Mercedes', 'Fiat', 'Honda', 'Nissan']

# Convert one list to a set for fast lookup
cars2_set = set(cars2)

# Only one loop needed now!
for car in cars1:
    if car in cars2_set:
        print(car)

'--- O(1)'
cars = ['Honda', 'Mazda', 'Jeep', 'Nissan']
print(cars[2])  # always returns 'Jeep'

'----- O(n!)'
import itertools

cars = ['Honda', 'Mazda', 'Jeep']

permutations = list(itertools.permutations(cars))

for perm in permutations:
    print(perm)

'-- O(log n)'

def binary_search(cars, target):
    left = 0
    right = len(cars) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = cars[mid]

        print(f"Checking: {guess}")

        if guess == target:
            return f"Found '{target}' at index {mid}"
        elif guess < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return f"'{target}' not found."

# Test it
cars = ['Honda', 'Jeep', 'Mazda']  # Must be sorted
print(binary_search(cars, 'Jeep'))

```