# Python Calculator

[Code Docs](../Code%20Docs%201b33d034d9f7811784a3f2b49b598b30.csv)

# Python Calculator

> 
> 

## Code Sample

```python
mylist = [0,1,2,3,4]

#From point 1 to the end, Index starts at 0.
print(mylist[1:]) 

#Upto index 1, but not including.
print(mylist[:1]) 

#Print the value at index point 1
print(mylist[1]) 

#Multiplication of the two values.
print(mylist[1] * mylist[3])

while True:
    try:
        my_value_1 = float(input('Enter New Value 1'))
        break
    except ValueError:
            print('Thats Not A Number!')

while True:
    try:
        my_value_2 = float(input('Enter new Value 2'))
        break
    except ValueError:
        print('Not a number')
    
symbol_check = False

while symbol_check == False:
    symbol = input('Enter a symbol')

    if symbol == '+':
        total = my_value_1 + my_value_2
        symbol_check = True
    elif symbol == '-':
        total = my_value_1 - my_value_2
        symbol_check = True
            
    elif symbol == '/':
        total = my_value_1 / my_value_2
        symbol_check = True
    elif symbol == '*':
        total = my_value_1 * my_value_2
        symbol_check = True
    elif symbol == '//':
        total = my_value_1 // my_value_2
        symbol_check = True
    else:
        symbol_check = False

print('Sum of values ' + str(total) + '.')
```

Refer to the template page to see more examples.

## Parameters

|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |

## Quick Copies

- **Variable types**
- **Pie chart**
- **Flow chart**
- **Mathematical Equations**

## Capabilities

Table of Contents

---