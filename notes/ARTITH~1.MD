# Artithmetic Operators

Created: 5 April 2025 09:56
Class: Additional Research
Is Completed: Yes

```python

#Modulus

print(10 % 3)  #Remainder
print(2 ** 5)  #Exponent To the power of.
print( 2 * 2 * 2 * 2 * 2) #The same as
print(10 // 3) #Divides 2 numbers and rounds down the result
x = 10 #Assignment Operator
x += 10 #can use all operators above
print(x)
#x = x + 10  - above is the same as.

#Comparisson
#==
#!=
#<
#>
#<=
#>=

x = 10
y = 20

print(x == y)
print(x < y)
print(x <= y)
print(x != y)

print('Strings')
x = 'Hello'
y = 'Hi'

print(x == y)
print(x != y)

print('Comparison Ops')
#and or not

x = 10
y = 20
z = 30

print(x < y and y < z) #Both statements are true
print(x < y and z < y) #Both must be true
print(x < y or z < y) #Either must be true

print(not x < y) #Not negates/opposite
print(not y < x)

#Input
x = input('enter a value')
y = input('enter second value')

#Type Cast Input Values
x = int(x)
y = int(y)

print(x + y)
```