# Arrays and Linked Lists

Created: 2 April 2025 10:55
Class: Additional Research
Is Completed: Yes

Imagine memory like a set of drawers:

 Your computer looks like a giant set of drawers, and each drawer has an address.

Each time you want to store an item in memory, you ask the computer for some space, and it gives you an address where you can store your item.

Arrays: array means all your tasks are stored contiguously (right next to each other) in memory.

Adding a new task: 

you need to ask your computer for a different chunk of memory that can fit four tasks. Then you need to move all your tasks there.

Linked Lists:

With linked lists, your items can be anywhere in memory.

With linked lists, you never have to move your items. 

Arrays vs Lists:

Arrays are great if you want to read random elements because you can look up any element in your array instantly. With a linked list, the elements aren’t next to each other, so you can’t instantly calculate the position of the fifth element in memory—you have to go to the first element to get the address to the second element, then go to the second element to get the address of the third element, and so on until you get to the fifth element.

![image.png](Arrays%20and%20Linked%20Lists%201c93d034d9f780e59453df95d350144f/image.png)

What’s better if you want to insert elements in the middle: arrays or lists? With lists, it’s as easy as changing what the previous element points to.

What if you want to delete an element? Again, lists are better because you just need to change what the previous element points to. With arrays, everything needs to be moved up when you delete an element.

![image.png](Arrays%20and%20Linked%20Lists%201c93d034d9f780e59453df95d350144f/image%201.png)

With an array, you can read a whole section of items. But you can’t do this with a linked list! You don’t know where the next item is. You need to read an item, find out where the next item is, and then read the next item.

So not only do arrays give you random access, but they also provide faster sequential access!

Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with *A*. The second slot points to a linked list containing all the usernames starting with *B*, and so on.

![image.png](Arrays%20and%20Linked%20Lists%201c93d034d9f780e59453df95d350144f/image%202.png)

**Selection sort**

def selectionSort(arr):
newArr = []
copiedArr = list(arr) // copy array before mutating
for i in range(len(copiedArr)):
smallest = findSmallest(copiedArr)
newArr.append(copiedArr.pop(smallest))
return newArr

print(selectionSort([5, 3, 6, 2, 10]))

Recap:

- Your computer’s memory is like a giant set of drawers.
- When you want to store multiple elements, use an array or a linked list.
- With an array, all your elements are stored right next to each other.
- With a linked list, elements are strewn all over, and one element stores the address of the next one.
- Arrays allow fast reads.
- Linked lists allow fast inserts and deletes.