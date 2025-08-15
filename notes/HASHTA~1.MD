# Hash Tables and Chaining

Created: 16 April 2025 20:44
Class: Additional Research
Is Completed: Yes

Hash tables enable efficient data storage and retrieval through hash functions, which map keys to specific locations in the table.

This guide covers separate chaining for handling collisions and explains how to add, search, and remove elements. We'll analyze performance using Big O notation to compare hash tables with other data structures.

Hash functions are fundamental to how hash tables work—they convert input keys into table indices. Let's look at some examples:

- For integers in a table with 11 slots, we use modulus: Hash(key) = key mod 11. For instance, key 42 maps to index 9 (42 mod 11 = 9).
- For strings, we convert characters to ASCII values. The word "cat" maps to index 4 ((99 + 97 + 116) mod 11 = 4).

A good hash function must be deterministic and distribute keys evenly to minimize collisions.

- Hash tables store key-value pairs and use these hash functions to compute indices for quick data access. When collisions occur, separate chaining handles them by using linked lists at each index.
- To add elements:

Calculate the hash value

1. Store at the corresponding index
2. If collision occurs, add to the front of the linked list
3. For searching:

Calculate hash value

1. Check the linked list at that index
2. Traverse list if needed
3. Deletion follows a similar process, first locating the element before removing it.

Performance depends on the load factor (n/s), where n is the number of elements and s is the table size. With good distribution, average operations take O(1) time. The worst case is O(n) when all elements hash to the same slot.

Tables automatically resize when the load factor exceeds 0.7-0.75.

- Hash tables with separate chaining provide efficient data storage and retrieval, but their success relies on well-designed hash functions and proper load factor management.
- Next, we'll explore searching, removing elements, and handling collisions with open addressing.
- Consider a simple example with a table of size 10, using key mod 10 as our hash function. We'll demonstrate adding elements and handling collisions through linear probing.

Adding element 5 is straightforward—it goes to index 5. Elements 24, 50, 19, and 57 are similarly added without collision.

When searching for element 24, we check index 4 and find it immediately. If searching for 33, we check index 3, find it empty, and conclude 33 isn't present.

- Collisions happen when adding element 55, which maps to the occupied index 5. Using linear probing, we place it at index 6. Adding element 35 requires multiple probes before finding space at index 8. Performance degrades when the table becomes 80% full.
- For deletion, we use "tombstone" markers instead of direct removal to preserve probe sequences for future searches. When encountering a tombstone during probing, we continue searching until finding the target element or an empty slot.
- Performance depends heavily on the load factor (n/s) and probing strategy:

Average insertion: O(1/(1-λ)) where λ is load factor

- Search and deletion have similar complexity
- Linear probing is simple but prone to clustering
- Tables typically resize at 70-80% capacity

When comparing collision resolution methods:

- Open addressing is memory-efficient but sensitive to load factor
- Separate chaining handles high loads better but uses extra memory
- Choose based on expected load and memory constraints

A hash table is like a smart storage system that helps us find and store data quickly. It works by using a special formula (called a hash function) that tells us exactly where to put each piece of data.

Let's break down how it works:

Think of a hash table as a row of numbered boxes (like mailboxes). The hash function helps us decide which box to use for each item. Here are two simple examples:

- For numbers: If we have 11 boxes, we divide our number by 11 and use the remainder. So number 42 goes in box 9 (because 42 ÷ 11 leaves remainder 9)
- For words: We convert letters to numbers and add them up. The word "cat" ends up in box 4

Sometimes two items might need to go in the same box. We handle this in two ways:

- Method 1 (Chaining): We attach a list to each box, so multiple items can share it
- Method 2 (Open Addressing): We look for the next empty box nearby

To add something to our storage system:

1. Figure out which box it belongs in
2. Put it in that box
3. If the box is taken, use one of our sharing methods

To find something:

1. Calculate which box it should be in
2. Look in that box
3. If needed, check the attached list or nearby boxes

The system works best when it's not too full. We usually add more boxes when it gets about 70-75% full.

Let's look at a real example with 10 boxes:

- Storing number 5 is easy - it goes in box 5
- Numbers 24, 50, 19, and 57 each get their own boxes too
- When we want to store 55, but box 5 is taken, we put it in the next empty box (box 6)

When we need to remove something, we mark its spot as "empty" but keep track of it to help us find other items later.

The system's speed depends on:

- How full the storage is
- Which method we use to handle shared boxes
- How well our formula spreads things out

Choose between the two sharing methods based on your needs:

- Open Addressing: Uses less memory but slows down when getting full
- Chaining: Works better when very full but needs extra memory
- Pick the one that fits your storage space and how many items you'll store