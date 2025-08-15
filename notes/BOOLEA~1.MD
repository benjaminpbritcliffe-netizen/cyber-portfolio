# Boolean

[Code Docs](../Code%20Docs%201b33d034d9f7811784a3f2b49b598b30.csv)

# Template

Welcome to the `Template` page! 

Click the “+ New” button in the left menu to automatically create a new documentation page with this template. 

To edit this page, go to the left menu, find the blue “New” button and click the arrow pointing down. Then, find the “Template” page, click the three dots, and hit “Edit”.

> 📘 This is a callout you can use to highlight important notes.
> 

## Code Sample

```python
while True:
    try:
        name = input('Enter your name')
        break
    except ValueError:
        print('Incorrect value')

while True:
    try:
        age = int(input('Enter your age'))
        break
    except ValueError:
        print('Not a number')
    
banned = False

if name == 'Ben':
          banned = True
else:
    banned = False

if age >= 18 and banned == False:
          print('Ok')
elif age < 18:
    print('Underage')
elif banned == True:
    print('Banned')
    
    
    

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