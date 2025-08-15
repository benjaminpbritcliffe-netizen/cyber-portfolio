# Static and Dynamic Arrays

Created: 17 March 2025 11:54
Class: 1
Is Completed: Yes

Task:

**Read the following sections**

[Data Structures and Algorithms in Python, Michael T. Goodrich, Roberto Tamassia, Michael H. Goldwasser, sections 4.1.3, 5.2, 5.3-5.3.1](https://eu.alma.exlibrisgroup.com/leganto/public/44YORK_INST/citation/56797030580001381?auth=SAML):

- Consider scenarios where flexibility matters more than speed or memory efficiency. Can you think of a real-world situation where you would clearly prefer static arrays over dynamic arrays, or vice versa?
- When comparing binary and linear search, think about how data organization affects efficiency. Would you invest time upfront to sort data for faster searches later, or use linear search for frequently changing data?

Bit: The smallest unit of information in computer memory

Byte: Contains 8 bits

Memory Address: A unique identifier assigned to each byte in memory

Programming languages track how identifiers map to memory addresses—for example, variables X and Y each point to different memory locations.

Arrays:

A collection of related variables stored in consecutive memory bytes.

💡 In Python, each character uses two bytes (16 bits) because of Unicode encoding.

Arrays consist of cells—memory locations accessed by integer indices starting at zero.

Static arrays have key limitations: They require a fixed size when created and cannot be expanded.

💡 This isn't an issue for Python tuples or strings since they're immutable—their size is fixed at creation.

Python lists use dynamic arrays, allowing automatic resizing through a growth mechanism.

**Growth Mechanism of Python Lists**

1. **Preallocation**: Python lists reserve extra memory beyond what's immediately needed for future elements.
2. **Doubling Strategy** (Amortized Growth): When the allocated space fills up and a new element is added, Python:
    - Allocates a new, **larger** memory block (growing exponentially)
    - Copies existing elements to the new block
    - Frees the old block

### **📌 When to Use a Static Array?**

A **static array** has a fixed size, with memory allocated at creation.

✅ **Use a static array when:**

1. **You know the exact number of elements needed.**
    - Example: Storing the days of the week (`7 elements`) or months of the year (`12 elements`)
2. **Memory efficiency is a priority.**
    - Example: Embedded systems or low-level programming where memory is limited
3. **You need fast access and performance.**
    - Example: A lookup table for ASCII characters (fixed at 256 elements)
4. **Your program doesn't need resizing.**
    - Example: A game storing predefined levels (e.g., `10 levels max`)

---

### **📌 When to Use a Dynamic Array?**

A **dynamic array** (like Python's `list` or C++ `vector`) grows or shrinks as needed, reallocating memory when necessary.

✅ **Use a dynamic array when:**

1. **You don't know the number of elements in advance.**
    - Example: Storing user input, where the number of entries is unpredictable
2. **You need flexibility to resize the array.**
    - Example: A dynamic list of online players in a game lobby
3. **You expect frequent insertions or deletions.**
    - Example: A playlist where users can add or remove songs dynamically
4. **You need to handle large data but don't want to preallocate too much memory.**
    - Example: Storing search results from a database query (result size unknown)

---

### **🆚 Static vs. Dynamic Array Comparison**

| Feature | Static Array | Dynamic Array |
| --- | --- | --- |
| **Size** | Fixed at creation | Can grow/shrink |
| **Memory** | Preallocated | Adjusts dynamically |
| **Speed** | Faster access (no reallocation) | Slightly slower (resizing overhead) |
| **Flexibility** | Rigid | More adaptable |
| **Usage Examples** | Fixed-size data (e.g., days of the week) | Variable-size data (e.g., user input storage) |

---

### **📢 Final Takeaway**

- Use **static arrays** when memory predictability and speed are crucial.
- Use **dynamic arrays** when flexibility is needed, and the number of elements can change.

Would you like real-world coding examples in Python or another language? 🚀