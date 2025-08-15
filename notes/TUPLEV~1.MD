# Tuple vs Lists

Tags: Note

### 1. **Immutability (Safety & Integrity)**

- **Tuples are immutable**, meaning their contents cannot be changed after creation.
- This makes them **safer** to use when working with **constants** or **data that shouldn’t change**.
- Example: Storing **coordinates**, **database connection settings**, or **fixed configurations**.

```python
coordinates = (52.5200, 13.4050)  # Berlin (lat, long)

```

### 2. **Performance (Faster than Lists)**

- Tuples **consume less memory** and are **faster** than lists.
- Their fixed size allows Python to optimize storage and access.
- Example: If you need **many small, read-only data structures**, tuples can improve performance.

```python
import sys
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))  # Larger memory
print(sys.getsizeof(my_tuple))  # Smaller memory

```

### 3. **Hashability (Used as Dictionary Keys & Set Elements)**

- Tuples are **hashable** if they contain only immutable elements.
- Lists are **not** hashable (since they are mutable).
- Example: Using tuples as **keys in dictionaries**.

```python
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

```

### 4. **Function Return Values (Implicit Packing & Unpacking)**

- Functions often return **multiple values** as a tuple.
- Example:

```python
def get_user():
    return "Alice", 25  # Returns a tuple implicitly

name, age = get_user()  # Tuple unpacking

```

### 5. **Ensuring Data Integrity**

- If you want to **ensure** that data remains unchanged, a tuple is preferable over a list.
- Example: Prevent accidental modification of a dataset.

```python
settings = ("dark_mode", True)  # Safer than a list

```