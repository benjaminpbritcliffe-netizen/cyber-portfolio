# Flow Control Structures

Created: 17 March 2025 11:59
Class: 1
Is Completed: Yes

Booleans Method:

True or False

>, <,≥,≤=,

== Equality

! = Not Equal

10 < 7  False

Make sure to use the same type when booleans.

To safely compare float values, make sure to use math.

Do not use == operators to compare two floats

Boolean Operators (in presedence order)

Not (not like)

And (match both)

Or (match either)

```python
admin = True
enabled = False

print(admin and enabled)

print(not admin)
print(not enabled)

print(admin or enabled)

print((not admin) or (not enabled))
```

User brackets to make code more readable and avoid logical errors.

Boolean expressions are evaluated from left to right.

Complex Boolean Expressions.

**Sequential Logic (Sequential Flow)**

Sequential logic as the name suggests follows a serial or sequential flow in which the flow depends on the series of instructions given to the computer. Unless new instructions are given, the modules are executed in the obvious sequence. The sequences may be given, by means of numbered steps explicitly. Also, implicitly follows the order in which modules are written. Most of the processing, even some complex problems, will generally follow this elementary flow pattern.

<aside>
💡

**sequential flow** is the default execution method in Python. This means that Python executes code **line by line**, from **top to bottom**, unless there are control flow statements (such as loops, function calls, conditionals, or exceptions) that alter the flow.

</aside>

## **Selection Logic (Conditional Flow)**

Selection Logic simply involves a number of conditions or parameters which decides one out of several written modules. The structures which use these type of logic are known as **Conditional Structures**. These structures can be of three types:

- **Single Alternative** This structure has the form:
    
    ```
    If (condition) then:
         [Module A]
    [End of If structure]
    ```
    
    **Implementation:**
    
- **Double Alternative** This structure has the form:
    
    ```
    If (Condition), then:
         [Module A]
    Else:
         [Module B]
    [End if structure]
    
    ```
    
    **Implementation:**
    
- **Multiple Alternatives** This structure has the form:
    
    ```
    If (condition A), then:
         [Module A]
    Else if (condition B), then:
         [Module B]
            ..
            ..
    Else if (condition N), then:
         [Module N]
    [End If structure]
    ```
    

## **Iteration Logic (Repetitive Flow)**

The Iteration logic employs a loop which involves a repeat statement followed by a module known as the body of a loop.

```
Repeat for i = A to N by I:
       [Module]
[End of loop]
```

```
Repeat while condition:
     [Module]
[End of Loop]
```
