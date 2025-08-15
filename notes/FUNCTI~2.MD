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