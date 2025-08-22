# NumPy 🍰

Status: To read

NumPy

22 September 2022

15:49

## _Goals:_

- _Understand what NumPy Is_
- _Creating arrays with NumPy_
- _Retrieve information from NumPy array using slicing and indexing_
- _Learn basic NumPy operations_
- _Test NumPy skills with exercise and questions_

###

### _What is NumPy_

- _Numpy is a pyhton library for creating N-dimensional arrays._
- _Ability to broadcast functions_
- _Built in Linear algebra, statistical distributions, trigonometric and random
  number capabilities._
- _Numpy is more efficient_
- _Useful for quickly applying functions to our data set._

## NumPy Arrays

import numpy as np

mylist = [1,2,3]

type(mylist)

np.array(mylist)

myarr = np.array(mylist)

type(myarr)

Non NumPy version

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

Result =

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

NumPy Version

np.array(my_matrix)

Result =

array([[1, 2, 3]

[4, 5, 6]

 [7, 8, 9]])

## NumPy Range Function =

Creates a range of values from 0 to 9

np.arange(0,10)

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

Include a step size, to go up in 2 instead

np.arange(0,10,2)

array([0, 2, 4, 6, 8])

np.arange(0,101,2)

array([ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24,

26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,

52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76,

78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100])

## #dealing with zeros

np.zeros(5)

array([0., 0., 0., 0., 0.])

## #Tuple of zeros

np.zeros((5,5))

array([[0., 0., 0., 0., 0.],

[0., 0., 0., 0., 0.],

[0., 0., 0., 0., 0.],

[0., 0., 0., 0., 0.],

[0., 0., 0., 0., 0.]])

## first digit is rows, second digit is columns

np.ones((4,4))

array([[1., 1., 1., 1.],

[1., 1., 1., 1.],

[1., 1., 1., 1.],

[1., 1., 1., 1.]])

## #Linspace

Returns evenly spaced numbers over a specific interval, different syntax to arange

Start Point, Stop Point, How many numbers inbetween the start and stop evenly spaced.)

np.linspace(0,10,3)

array([ 0., 5., 10.])

5 figures over 6 points

np.linspace(0,5,6)

array([0., 1., 2., 3., 4., 5.])

Includes the stopping point

1

Identity matrix

np.eye(5)

array([[1., 0., 0., 0., 0.],

[0., 1., 0., 0., 0.],

[0., 0., 1., 0., 0.],

[0., 0., 0., 1., 0.],

[0., 0., 0., 0., 1.]])

 Random

np.random.rand(1)

Rows, Columns

np.random.rand(5,3)

## #Random Standard Normal Distribution

Values closer to 0 are more likely to appear than negatives and further away numbers

np.random.randn(3,2)

## #Random Integers

Numbers between two figures, all whole numbers, does not include the last number

The below will give us 5 numbers between 0 and 100
 From,To and then how many

np.random.randint(0,101,5)

From and to in the first brackets, and then tuple creation in the additional brackets

From,To and then how many

np.random.randint(0,101,(4,5))

Setting a seed, get a particular set

Seed is to select a particular set of random numbers

Based on the seed you will always get the same "set" of numbers

np.random.seed(42)

np.random.rand(4)

Eg. The above will always give you

array([0.37454012, 0.95071431, 0.73199394, 0.59865848])

Reshape

np.arange(0,25)

arr.reshape(5,5)
The reshape will take the original array and set it into a 5x5 range

Min and Max

ranarr.max()

ranarr.min()

Find location of Min and Max number

ranarr.argmax()

ranarr.argmin()

## Finding type of array

ranarr.dtype

## Find the shape

arr.shape

TASK: Create a numpy array of 101 evenly linearly spaced points between 0 and 10.
Assign this array to a variable called myarray.
Please note, in order for the exercise to evaluate correctly,
you must use the variable name myarray

```` python
import numpy as np

#From number, to figure (inclusive), how many numbers to split it over

myarray = np.linspace(0,10,101)

array([ 0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ,

1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. , 2.1,

2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3. , 3.1, 3.2,

3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4. , 4.1, 4.2, 4.3,

4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5. , 5.1, 5.2, 5.3, 5.4,

5.5, 5.6, 5.7, 5.8, 5.9, 6. , 6.1, 6.2, 6.3, 6.4, 6.5,

6.6, 6.7, 6.8, 6.9, 7. , 7.1, 7.2, 7.3, 7.4, 7.5, 7.6,

7.7, 7.8, 7.9, 8. , 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7,

8.8, 8.9, 9. , 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8,

9.9, 10. ])

# The above has given you 0 to 10 in 101 evenly split parts

len(myarray)

# Indexing and Selection

- Grabbing single element
- Slice of elements
- Broadcasting
- Indexing and seletion in 2-dimensions
- Conditional selection

# Grabbing a single element

# arange goes from and to (but not including the last value)

arr = np.arange(0,11)

arr

arr[8]

# Grabs the value at position 8, starts at 0. Result is 8 in this case

Grabbing a selection of numbers:

arr[1:5] #From number and to, but not including the 5th element.

Result is Array([1,2,3,4)

# Remember these start at 0 (0 is technically the 1st element)

From 0 (1st element) to to the 5th element

arr[:5]

Beginning from the the element to the end:

arr[5:]

# Broadcast

# Changing values in a list

arr

array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10])

arr[0:5] = 100

Changes the values in position 0 (1st position) to 4 (5th position) to 100

arr

array([100, 100, 100, 100, 100, 5, 6, 7, 8, 9, 10])

# Slicing

slice_of_arr = arr[0:5]

slice_of_arr

slice_of_arr[:] = 99

# This will change the original array too

# To not change the original array, need to take a copy of the original array

# Copying the array

arr_copy = arr.copy()

arr_copy[:] = 100

# Array copied

arr_copy

array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])

# Original Array

arr

array([99, 99, 99, 99, 99, 5, 6, 7, 8, 9, 10])

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

arr_2d

arr_2d.shape

arr_2d[0] #Grabs the first row of the array.

arr_2d[1,1] #At row 1, column 1 grab element, starts both at 0.

arr_2d[0,2] #Grab at row 0, element 2.

# Slicing a 2d shape

arr_2d[:2] #up to not including

arr_2d[:2,1:] # Upto column 2, got to 1.

Conditional:

arr = np.arange(1,11)

Arr

## #Broadcast

# Greater than 4?

arr > 4

# Result shows true or false in position where it matches the answer above

bool_arr = arr>4 #Setting a new variable to the broadcast above.

bool_arr

arr[bool_arr] #Will now give the array values where it shows True.

# Result

# array([ 5, 6, 7, 8, 9, 10])

Simplified:

arr = np.arange(1,11)

arr[arr>4]

# result array([ 5, 6, 7, 8, 9, 10])

Full conditional arange:

arr = np.arange(0,51)

arr

array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,

17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,

34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

arr[arr>35]

array([36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

# How many times a number larger than 2 occurred, using a selection array

importnumpyasnp

dice_rolls=np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2,
6, 6, 3, 6, 2, 3, 5, 6, 5])

total_rolls_over_two=len(dice_rolls[dice_rolls>2])
```
