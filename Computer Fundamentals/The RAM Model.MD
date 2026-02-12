# The RAM Model

RAM model, a simplified framework that helps you count the basic operations of
an algorithm. This model provides a practical way to estimate the time an
algorithm takes to run, based on the assumption that each operation—such as
addition or comparison—takes a uniform amount of time. By focusing on these
elementary steps, you can gain insights into how efficient an algorithm is, even
before implementation.

![image.png](The%20RAM%20Model%201c03d034d9f7803285d3cfe0879886f1/image.png)

[Big O Notation](../Class%20Notes%201763d034d9f780cc8210c56e1827c4eb/Big%20O%20Notation%201c13d034d9f780baa27ee11f4ea53f1d.md)

![image.png](The%20RAM%20Model%201c03d034d9f7803285d3cfe0879886f1/image%201.png)

![image.png](The%20RAM%20Model%201c03d034d9f7803285d3cfe0879886f1/image%202.png)

| **Time Complexity** | **Typical Description** | **Keyword / Analogy** | **Example / Scenario** |
| ------------------- | ----------------------- | --------------------- | ---------------------- |

| `O(1)` | Constant time | **"Instant"** – same time no matter the size | Accessing an array element by index |
| ------ | ------------- | -------------------------------------------- | ----------------------------------- |

| `O(log n)` | Logarithmic time | **"Divide & conquer"** – shrink the problem fast | Binary search |
| ---------- | ---------------- | ------------------------------------------------ | ------------- |

| `O(n)` | Linear time | **"One loop"** – check each item once | Loop through a list |
| ------ | ----------- | ------------------------------------- | ------------------- |

| `O(n log n)` | Linearithmic time | **"Smart sorting"** – break & conquer, then combine | Merge sort, heap sort |
| ------------ | ----------------- | --------------------------------------------------- | --------------------- |

| `O(n²)` | Quadratic time | **"Double loop"** – compare every pair | Bubble sort, nested loops |
| ------- | -------------- | -------------------------------------- | ------------------------- |

| `O(n³)` | Cubic time | **"Triple loop"** – deep nested processing | 3D matrix operations |
| ------- | ---------- | ------------------------------------------ | -------------------- |

| `O(2ⁿ)` | Exponential time | **"Explodes"** – doubles with each step | Recursive Fibonacci, brute-force combos |
| ------- | ---------------- | --------------------------------------- | --------------------------------------- |

| `O(n!)` | Factorial time | **"Total chaos"** – try _every_ possible order | Solving permutations (e.g. traveling salesman) |
| ------- | -------------- | ---------------------------------------------- | ---------------------------------------------- |

## 🔁 Quick Order to Remember (from Fastest → Slowest)

> O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

---

## 🧠 Mnemonic (Optional Fun One)

> "One Lazy Nerd Sorts Squares, Cubes, and Explodes Fast!"
>
> (1, log n, n, n log n, n², n³, 2ⁿ, n!)
