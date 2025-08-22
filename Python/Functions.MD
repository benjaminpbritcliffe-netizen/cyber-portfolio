# Functions

Created: 26 March 2025 14:52
Class: 3
Is Completed: Yes

A function is a block of code that can be reused to perform a specific task.

Function Call Stack: The sequence of function calls made during the execution of a program.

Python provides many useful built-in functions.

These built-in functions perform common tasks, such as:

- Converting data types
- Manipulating strings
- Calculating mathematical expressions
- Working with files
- Accessing the operating system

To use a built-in function, you need to know its name and the arguments that it takes. Therefore, to be

an efficient programmer, you need to learn to read Python's documentation.

Here are some of the most commonly used built-in functions in Python:

- print(): Prints text to the console.
- input(): Takes input from the user.
- len(): Returns the length of a string or list.
- type(): Returns the type of an object.
- int(): Converts a string to an integer.
- float(): Converts a string to a floating-point number.
- str(): Converts an object to a string.
- min(a,b): Returns the minimum value between a and b.max(a,b): Returns the maximum value between a and b.pow(a,b): Returns a to the power of b.abs(a): Returns the absolute value of a.Not all common mathematical functions are part of the built-in collection, for example to compute the cosine or sine of an angle, we need to import the math module first, something that we will explore in another video.

Adhoc Functions (Functions that are not built in)

## ## Functions ##

def my_func():

print('hello')

myfunc()

### #Argument required function

# requires one argument to meet the name requirement

def my_func(name):

print('hello ' + name)

my_func('Jose')

### #Using return function

# Return is saved

def square(x):

return x**2

result = square(2)

print(result)

### #Default Value function

# No Name is the default value

def my_func(name='No Name'):

print('hello ' + name)

my_func() #Will use the default value as no name we defined when running the func.

def car(carname):
if carname == 'Mazda':
print(1)
elif carname == 'Toyota':
print(2)
else:
print('Car Not In List')

carname_val = input('Enter a car name')

car(carname_val)

```python
class Car:
    def __init__(self,make,model,mileage,year,MOTFailure):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.year = year
        self.MOTFailure = MOTFailure

    def GetMake(self):
        print(self.make)

    def GetModel(self):
        print(self.model)

    def MileageStatus(self):
        if self.mileage > 30000:
            
            if self.MOTFailure == True:
                print('Car is old and has had an MOT Failure')
            else:
                print("Car is old, but hasn't had an MOT Failure")
                print('But the Car is Old')
        else:
            print('Car is new')
            if self.MOTFailure == True:
                print('MOT Failure')
            else:
                print('No MOT Failure')

Car1 = Car('Honda','Jazz',29000,'2006',False)

Car1.GetMake()

Car1.GetModel()

Car1.MileageStatus()

```

# Functions

Created: 6 April 2025 19:33
Class: 5
Is Completed: Yes

```python
#A block of reusable code

def helloworld():
    print('Hello World')

helloworld()

def add(x,y):
    return (x + y) #We wont se any result to screem

result = add(7,8)
print(result)

#Optional Parameters

def add(x =0,y=0):
    print(x + y)

add()

def mysum(*numbers):  #If you don't know how many numbers etc.
    result = 0
    for number in numbers:
        result += number
    return result

print(mysum(10,20,20))
```
