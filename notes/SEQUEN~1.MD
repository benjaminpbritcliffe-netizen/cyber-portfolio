# Sequential and Unsorted Arrays

Created: 17 March 2025 11:56
Class: 1
Is Completed: Yes

### **Binary Search Algorithm**

1. **Initialize Pointers**:
    - Set `low = 0` (start of the array).
    - Set `high = len(array) - 1` (end of the array).
2. **Find Middle Index**:
    - Compute `mid = (low + high) // 2` (integer division).
3. **Compare Target with Middle Element**:
    - If `array[mid] == target`: Found it! ✅
    - If `array[mid] > target`: Search the **left half** (`high = mid - 1`).
    - If `array[mid] < target`: Search the **right half** (`low = mid + 1`).
4. **Repeat Until Found or `low > high`**:
    - The process continues until the search space is exhausted.

Linear Search on an unsorted array > Each element is checked one by one. 

Sorted Array > Diving the search in half, to reduce the number of checks, making searching data faster.

| **Scenario** | **Use Linear Search?** |
| --- | --- |

| **Small dataset?** | ✅ Yes |
| --- | --- |

| **Data is unsorted & search is rare?** | ✅ Yes |
| --- | --- |

| **Data changes frequently?** | ✅ Yes |
| --- | --- |

| **Stored in a linked list?** | ✅ Yes |
| --- | --- |

| **Need the first occurrence only?** | ✅ Yes |
| --- | --- |

| **Very large sorted dataset?** | ❌ No, use Binary Search |
| --- | --- |