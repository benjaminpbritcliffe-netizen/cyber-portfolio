# If-elif-else

## Code Sample

```python
temperature = 25

if temperature <= 15:
print('Cold')
elif temperature >= 25:
print('Hot')
else:
print('Moderate')
```

```python
user_number = 35

if user_number < 10:
    print('Less than 10')
elif user_number > 30:
    print('Greater than 30')
else:
    print('Between 10 and 30')
```

```python
user_number = 29

if user_number < 10:
    print('Less than 10')
elif user_number > 30 and user_number <= 35:
    print('Greater than 30 but less than 35')
elif user_number >= 35:
    print('Greater than 35')
else:
    print('Between 10 and 30')
```

```python

while True:
    try:
        bananas_kg = int(input('Enter Kg of bananas required'))
        price_of_bananas = float(3.00)
        subtotal = round(bananas_kg * price_of_bananas,2)
        print(subtotal)
        if subtotal > float(50.00):
            total = round(subtotal + float(1.50),2)
            print(total)
        else:
            total = round(subtotal + float(4.99),2)
            print(total)
    except:
        print('enter a number')

```

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
