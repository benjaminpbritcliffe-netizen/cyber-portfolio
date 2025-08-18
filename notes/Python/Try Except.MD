# Try Except

[Code Docs](../Code%20Docs%201b33d034d9f7811784a3f2b49b598b30.csv)

## Code Sample

```python
import random

while True:
    try:
        user_input = int(input('Enter a number between 1 and 2'))
        random_num = int(random.randrange(1,2))
        if user_input == random_num:
            print('Correct')
            break
        else:
            print('incorrect')
    except ValueError:
            print('Not a number')
    
        

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
