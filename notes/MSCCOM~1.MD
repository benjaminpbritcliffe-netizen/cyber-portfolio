# MSc Computer Science & Cyber Security Prep

Status: To read

## Algorithms and Data Structures

- **Book:** [*Algorithms and Data Structures* by Niklaus Wirth](https://www.e-booksdirectory.com/details.php?ebook=10068)
A foundational text covering essential algorithms and data structures.

https://drive.google.com/file/d/1CAOglSC4Z7RFSgd0sArHDcq8Hc8PudFL/view?usp=drive_web

### **Main Topics Covered**

### **1. Fundamental Data Structures**

- Introduces **primitive data types** (integers, reals, booleans, characters, and sets).

A **primitive data type** is a basic type of data that is built into a programming language. These types are the fundamental building blocks for data manipulation and are typically predefined by the language itself. 

### **1. Primitive Data Types Characteristics**

A **primitive data type** is:

- **Fundamental**: Cannot be broken down into smaller components.
- **Memory-Efficient**: Stored directly in memory as a simple value.
- **Directly Supported by the Language**: Comes built-in without requiring an external library.
- **Immutable**: Often has a fixed, unchangeable representation.

### **Examples of Primitive Data Types**

- **Integers** (`int`, `short`, `long`)
- **Floating-point numbers** (`float`, `double`)
- **Characters** (`char`)
- **Boolean values** (`true/false`)

| Data Type | Primitive? | Why? |
| --- | --- | --- |

| **int** | ✅ Yes | Stores a single integer value in memory |
| --- | --- | --- |

| **char** | ✅ Yes | Represents a single character |
| --- | --- | --- |

| **float** | ✅ Yes | Represents a single numerical value, even if displayed with multiple digits |
| --- | --- | --- |

| **boolean** | ✅ Yes | Only stores `true` or `false` |
| --- | --- | --- |

- Discusses **arrays** and **records** as fundamental structures.

### **Characteristics of an Array**

1. **Fixed Size (in most languages)**:
    - In many languages (e.g., C, Java), arrays have a **fixed size** when declared.
    - Some languages like Python allow **dynamic resizing** (e.g., lists in Python behave like dynamic arrays).
2. **Same Data Type**:
    - Arrays store elements **of the same type** (e.g., all `int`, all `float`, all `char`).
    - Some languages (like Python) allow mixed types in lists, but typical arrays (e.g., in C) do not.
3. **Indexed Storage**:
    - Each element in an array is accessed via an **index**, starting from `0` in most languages.
4. **Continuous Memory Allocation**:
    - Elements are stored in **contiguous memory locations**, making access very fast.
    
- Covers **file sequences** and **buffering techniques**.

<aside>
💡

- **File sequences** define how data is processed (sequential, random, appending, etc.).
- **Buffering** improves performance by reducing disk accesses and optimizing memory use.
- Choosing the right **buffering technique** depends on the **file size, speed requirements, and application needs**.
</aside>

File Sequences are the form of ordering and structure and the way the data is read:

| File Sequence Type | Description | Example Use Case |
| --- | --- | --- |

| **Sequential File Access** | Data is read/written **in order, from start to end** | Reading a log file line by line |
| --- | --- | --- |

| **Random File Access** | Data can be read/written **at any position in the file** | Database file storage, multimedia files |
| --- | --- | --- |

| **Appending to Files** | New data is **added at the end** of the file | Logging, transaction history |
| --- | --- | --- |

| **Overwriting Files** | Existing data is **replaced** | Configuration updates |
| --- | --- | --- |

Buffering:

Buffering is a technique that temporarily stores **chunks of data in memory** before reading/writing to a file. This reduces the number of disk accesses, improving efficiency.

### **Types of Buffering Techniques**

| Buffering Type | Description | Example Use Case |
| --- | --- | --- |
| **Fully Buffered** | Reads/writes **entire files** or **large chunks** at once | Loading an entire image into memory |
| **Line Buffered** | Reads/writes **one line at a time** | Processing text files line by line |
| **Unbuffered (Direct I/O)** | No buffering, data is read/written **directly to disk** | Critical real-time applications (e.g., logging, databases) |

- Introduces **searching algorithms**, including:
    - Linear search
    - Binary search
    - Knuth-Morris-Pratt and Boyer-Moore string search algorithms.
    
    ### Naive Pattern Searching Algorithm
    
    The idea is, we start at every index in the text and compare it with the first character of the pattern, if they match we move to the next character in both text and pattern. If there is a mismatch, we start the same process for the next index of the text. You can refer this article for the complete implementation of this approach – [**Naive algorithm for pattern searching**](https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/).
    
    ### KMP Pattern Searching Algorithm
    
    The Knuth-Morris-Pratt (KMP) algorithm is a string-searching algorithm which is used to find a pattern within large texts efficiently. Unlike naive pattern searching algorithm which starts from the beginning of the pattern after each mismatch, KMP uses the **structure of the pattern** to avoid redundant comparisons. It preprocesses the **pattern** string and creates an array called the **Longest Prefix Suffix** (lps) array which indicates how much of the pattern can be reused after a mismatch.
    
    ![image.png](MSc%20Computer%20Science%20&%20Cyber%20Security%20Prep%201793d034d9f780dea7d2c577dc371be7/image.png)
    

### **2. Sorting Algorithms**

- Covers basic and advanced sorting techniques:
    - **Insertion Sort**
    - **Selection Sort**
    - **Bubble Sort**
    - **Tree Sort**
    - **QuickSort (Partition Sort)**
    - **Merge Sort (Straight and Multiway Merging)**
- Compares sorting techniques based on efficiency and use cases.

### **3. Recursive Algorithms**

- Explains when and when not to use recursion.
- Covers **backtracking algorithms** such as:
    - The **Eight Queens Problem**
    - The **Stable Marriage Problem**
    - The **Optimal Selection Problem**.

### **4. Dynamic Information Structures**

- Introduces **pointers** and **linked lists**.
- Discusses **tree structures**, including:
    - Binary trees
    - Balanced trees
    - B-Trees (multiway and binary)
    - Priority search trees.
- Covers **topological sorting** and **tree traversal methods**.

### **5. Key Transformations (Hashing)**

- Explores **hash functions** and **collision handling** techniques.
- Analyzes the efficiency of hashing compared to tree-based structures.

---

### **Key Takeaways**

1. **Strong Emphasis on Structured Programming**
    - The book follows structured programming principles, demonstrating how data structures and algorithms must be designed hand-in-hand.
2. **Efficiency and Analysis of Algorithms**
    - Each algorithm is analyzed in terms of time and space complexity.
    - Sorting methods are compared in detail to highlight their advantages.
3. **Recursive and Dynamic Structures**
    - Recursion is presented as a powerful tool, but its trade-offs are discussed.
    - Dynamic structures like trees and linked lists are explored extensively.
4. **Practical Code Examples**
    - The book provides Modula-2 code examples, making it accessible to those familiar with Pascal-like languages.

---

## Cyber Security Threats

- **Book:** [*The Absolute Beginners Guide to Cyber Security*](https://archive.org/details/the-absolute-beginners-guide-to-cyber-security)
An introductory guide to understanding cyber security threats and defenses.

https://drive.google.com/file/d/1qV2_JkJeLeocLhvb_Q19IGwglywlD4J6/view?usp=drive_web

---

## Security Engineering

- **Book:** [*Security Engineering* by Ross Anderson](https://www.cl.cam.ac.uk/~rja14/book.html)
A comprehensive guide on building secure systems.

https://drive.google.com/file/d/16zTVwMLvn8sl5n0hDM4WD7HiIJMqW31g/view?usp=drive_web

---

## Advanced Programming

- **Book:** [*Advanced Programming in the UNIX Environment* by W. Richard Stevens](https://archive.org/details/advancedprogrammingintheunixenvironment3rdedition)
In-depth coverage of UNIX system programming.

https://drive.google.com/file/d/1XEp1ISUi9QLORcGn1_N0S-GPcI5KPU8V/view?usp=drive_web

---

## Computer and Mobile Networks

- **Book:** [*Computer Networking: Principles, Protocols and Practice* by Olivier Bonaventure](https://www.e-booksdirectory.com/details.php?ebook=10822)
An open-source ebook on computer networking fundamentals.

https://drive.google.com/file/d/10LEJz1CbnLS9L1JKcAU3Qh5G4FcycC-9/view?usp=drive_web

---

## Software Engineering

- **Book:** [*Software Engineering* by Ian Sommerville](https://archive.org/details/SoftwareEngineering9thEditionByIanSommerville)
A comprehensive introduction to software engineering principles.

https://drive.google.com/file/d/1aweS2lXe8x50FnYucgb0pQXuT3Gw19Mt/view?usp=drive_web

---

## Computer Architecture and Operating Systems

- **Book:** [*Computer Systems: A Programmer's Perspective*](https://archive.org/details/ComputerSystemsAProgrammersPerspective3rdEdition)
An in-depth look at computer systems from a programmer's viewpoint.

https://drive.google.com/file/d/1hzbkUk18HI1yaPX6X_pq0DZNr0fTUOtW/view?usp=drive_web

---

## Artificial Intelligence and Machine Learning

- **Book:** [*Understanding Machine Learning: From Theory to Algorithms*](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/)
A comprehensive text on machine learning theories and algorithms.

https://drive.google.com/file/d/164H3GsU2AHPokzYE-KooRA0CAicSsMmW/view?usp=drive_web

---

## Research Methods

- **Book:** [*Research Methods in Computer Science* by Mannila and Ronkainen](https://www.e-booksdirectory.com/details.php?ebook=11358)
An introduction to research methodologies in computer science.

https://drive.google.com/file/d/1zCLpM7G-SnUzPjLFK70MI_3scHiquycN/view?usp=drive_web

---

## Research Proposal and Individual Research Project

- **Book:** [*How to Write a Thesis* by Umberto Eco](https://archive.org/details/HowToWriteAThesis)
A guide on crafting effective research proposals and theses.

https://drive.google.com/file/d/1Tfh5kYJqeOpp1mWHy-9_rO7WITFkfJNz/view?usp=drive_web