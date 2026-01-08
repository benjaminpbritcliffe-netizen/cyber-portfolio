# Sequential and Unsorted Arrays

Created: 17 March 2025 11:56
Class: 1
Is Completed: Yes

## **Binary Search Algorithm**

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

Sorted Array > Diving the search in half, to reduce the number of checks,
making searching data faster.

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

## Sequence and Collections

Created: 6 April 2025 19:33
Class: Additional Research
Is Completed: Yes

```python
#lists

#A list is a dynamical type. can contain multiple data types
mylist = [10,20,30,'string',True,8.97]
print(mylist)

print(mylist[3]) #Specify an index number in range
print(mylist[0:3]) #Up to (but not included)
print(mylist[1:3]) #Right Side not inluded, Left side is included
print(mylist[-2]) #Right side starts at -1 .

mylist[3] = 7 #Changing index value
print(mylist)

for x in mylist:  #print all the index in a loop
    print(x)

print('Loop')
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

x = [1,2,3]
y = [4,5,6]

print(x + y) #Concatenates the lists

#Scalars

print(x * 4) #This will not multiply, it will scale it!

#len
print(len(x))

#max - only works with numbers (float and int)
print(max(x))
#min - only works with numbers (float and int)
print(min(x))

#Append method
x = [1,2,3]

x.append(6) #Adds the object to the list

print(x)

#Insert

x.insert(1,'value')

print(x)

#remove - does not use index uses value
x.remove('value')

print(x)

#remove by index - pop
x.pop(0)
print(x)

#find where a value is
print(x.index(3))

#Sort Method - Destructive
x = [1,3,2,5,4]
x.sort()
print(x)

#Non destructive versionm of sort.
x = [1,3,2,5,4]
print(sorted(x))

#Tuples
#Data or structure can not be changed
#Tuple is imutable
y = (3,1,2)
print(y[2])

#You could convert a tuple to a list
y = list(y)
y[2] = 1
print(y)

#then back to a tuple!
y = tuple(y)
print(y)

#Dictionary
#A unique key and a value belongs to that key

person = {
    'name':'Ben',
    'age':31,
    'gender': 'Male',
    True:88  #Doesn't have to be a string for a key
}

print(person)
print(person['name'])  #Use the key to access
print(person[True])

#Items
print(person.items())
#Keys
print(person.keys())
#Values
print(person.values())

#Membership Operators
x = [1,2,3]
print(2 in x) #T
print(7 in x) #F

print(2 not in x) #F
print(7 not in x) #T

#Is and Is Not

x = 10
if type(x) is int:
    print('x is int')
else:
    print('x is not int')

if type(x) is not int:
    print('x is not int')
else:
    print('x is an int')
```
