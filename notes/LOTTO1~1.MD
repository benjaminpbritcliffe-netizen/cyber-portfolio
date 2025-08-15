# Lotto

[Code Docs](../Code%20Docs%201b33d034d9f7811784a3f2b49b598b30.csv)

# Template

Welcome to the `Template` page! 

Click the “+ New” button in the left menu to automatically create a new documentation page with this template. 

To edit this page, go to the left menu, find the blue “New” button and click the arrow pointing down. Then, find the “Template” page, click the three dots, and hit “Edit”.

> 📘 This is a callout you can use to highlight important notes.
> 

## Code Sample

```python
import random
import operator as op

numbers = []

while len(numbers) < 6:
    while True:
        try:
            number = int(input("Enter a number between 1 and 59"))

            

            if number in numbers:
                print('Already selected')
            else:
                numbers.append(number)
                break

        except ValueError:
                    print('Not a number')
        
print('your numbers are:' + str(numbers))

selected_numbers = []

while len(selected_numbers) < 6:
    selected_number = random.randrange(1,59)
    if selected_number in selected_numbers:
        pass
    else:
        selected_numbers.append(selected_number)

print('winning numbers are:' + str(selected_numbers))

bonus_ball = []
if len(selected_numbers) == 6:
    bonus_ball_value = random.randrange(1,59)
    if bonus_ball_value in selected_numbers:
        pass
    else:
        bonus_ball.append(bonus_ball_value)
print('the bonus ball is:' + str(bonus_ball))

matched = [x for x in numbers if x in selected_numbers]
bball_matched = [x for x in numbers if x in bonus_ball]

print(matched)
print(bball_matched)

```

Refer to the template page to see more examples.

## Parameters

| Property | Type | Description |
| --- | --- | --- |
| `name` | `string` | If the name already exists, returns `false`. Otherwise, `true`. |
| `level` | `int` | The character level. Must be between `0` and `100`. |
| `inventory` | `list` | Coins are included using an `int` in the list. |

## Quick Copies

- **Variable types**
    - `None`
    - `string`
    - `int`
    - `signed`
    - `unsigned`
    - `float`
    - `boolean`
    - `true`
    - `false`
    - `list`
    - `array`
    - `tuple`
    - `range`
    - `dict`
    - `complex`
    - `bytes`
    - `set`
- **Pie chart**
    
    ```mermaid
    %%{init: {'theme': 'default'} }%%
    pie title Common Error Codes
    	"301" : 30
    	"404" : 40
    	"503" : 30
    ```
    
- **Flow chart**
    
    ```mermaid
    flowchart LR
    	I[(Idea)] ---> C(Code)
    	C ---> R(Review)
    	R --> I
    ```
    
- **Mathematical Equations**
    
    *Inline Equation:* $F=G\frac{m_1m_2}{d^2}$
    
    *Block equation:*
    
    $$
    \frac{df}{dt}=\lim_{h\to 0} \frac{f(t+h)-f(t)}{h}
    $$
    

## Capabilities

| Model | Feature X | Feature Y | Feature Z |
| --- | --- | --- | --- |
| A | ✅ | ✅ | ❌ |
| B | ❌ | ✅ | ✅ |
| C | ✅ | ❌ | ✅ |

Table of Contents

---