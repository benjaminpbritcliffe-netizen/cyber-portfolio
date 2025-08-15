# Overview

[Code Docs](../Code%20Docs%201b33d034d9f7811784a3f2b49b598b30.csv)

# Template

Welcome to the `Template` page! 

Click the “+ New” button in the left menu to automatically create a new documentation page with this template. 

To edit this page, go to the left menu, find the blue “New” button and click the arrow pointing down. Then, find the “Template” page, click the three dots, and hit “Edit”.

> 📘 This is a callout you can use to highlight important notes.
> 

## Code Sample

```jsx
createCharacter({
  method: 'post',
  data: {
    name: 'Wizard Erihann',
    level: 18,
		inventory: ["Wand", "Potion", 50]
  }
});
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
- **Pie Chart**
    
    ```mermaid
    %%{init: {'theme': 'default'} }%%
    pie title Common Error Codes
    	"301" : 30
    	"404" : 40
    	"503" : 30
    ```
    
- **Flow Chart**
    
    ```mermaid
    flowchart LR
    	I[(Idea)] ---> C(Code)
    	C ---> R(Review)
    	R --> I
    ```
    

## Capabilities

| Model | Feature X | Feature Y | Feature Z |
| --- | --- | --- | --- |
| A | ✅ | ✅ | ❌ |
| B | ❌ | ✅ | ✅ |
| C | ✅ | ❌ | ✅ |

Table of Contents

---