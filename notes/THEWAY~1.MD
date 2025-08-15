# The Way Of The Program

Attachments: Unit-10.pdf
Language: Python

A **program** is a sequence of instructions that specifies how to perform a computation. The computation might be something mathematical, such as solving a system of equations or finding the roots of a polynomial, but it can also be a symbolic computation, such as searching and replacing text in a document or (strangely enough) compiling a program.

The details look different in different languages, but a few basic instructions appear in just about every language:

- **Input:** Get data from the keyboard, a file, or some other device.
- **Output:** Display data on the screen or send data to a file or other device.
- **Math:** Perform basic mathematical operations like addition and multiplication.
- **conditional execution:** Check for certain conditions and execute the appropriate sequence of statements.
- **repetition:** Perform some action repeatedly, usually with some variation.

**Definition -Natural languages** are the languages people speak, such as English, Spanish, and French. They were not designed by people (although people try to impose some order on them); they evolved naturally.

**Definition - Formal languages** are languages that are designed by people for specific applications. For example, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols. Chemists use a formal language to represent the chemical structure of molecules.

Although formal and natural languages have many features in common-tokens, structure, syntax, and semantics-there are some important differences:

- **Ambiguity:** Natural languages are full of ambiguity, which people deal with by using contextual clues and other information. Formal languages are designed to be nearly or completely unambiguous, which means that any statement has exactly one meaning, regardless of context.
- **Redundancy:** In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots of redundancy. As a result, they are often verbose. Formal languages are less redundant and more concise.
- **Literalness:** Natural languages are full of idiom and metaphor. If I say, "The penny dropped", there is probably no penny and nothing dropping. Formal languages mean exactly what they say.

programs written in a high-level language have to be processed before they can run. This extra processing takes some time, which is a small disadvantage of high-level languages. (Such as Python)

![image.png](The%20Way%20Of%20The%20Program%201b23d034d9f780abaef4db63207f3bb4/image.png)

Python is considered an interpreted language because Python programs are executed by an interpreter. There are two ways to use the interpreter: **interactive mode** and **script mode**.

### **Syntax errors**

Python can only execute a program if the syntax is correct; otherwise, the interpreter displays an error message. **Syntax** refers to the structure of a program and the rules about that structure. For example, parentheses have to come in matching pairs, so `(1 + 2)` is legal, but `1 + 2)` is a **syntax error**.

In plain English, readers can tolerate most syntax errors, however Python is not so forgiving. If there is a single syntax error anywhere in your program, Python will display an error message and quit, and you will not be able to run your program. During the first few weeks of your programming career, you will probably spend a lot of time tracking down syntax errors. As you gain experience, you will make fewer errors and find them faster.

### **Runtime errors**

The second type of error is a runtime error, so called because the error does not appear until after the program has started running. These errors are also called **exceptions** because they usually indicate that something exceptional (and bad) has happened. Runtime errors are rare in the simple programs you will see in the first few chapters, so it might be a while before you encounter one.

### **Semantic errors**

The third type of error is the **semantic error**. If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages, but it will not do the right thing. It will do something else. Specifically, it will do what you told it to do. The problem is that the program you wrote is not the program you wanted to write. The meaning of the program (its semantics) is wrong. Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing.

## **Code Layout Requirements:**

- **Indentation:** Use 4 spaces per indentation level.
- **Tabs or Spaces?** Spaces are the preferred indentation method. Tabs should be used solely to remain consistent with code that is already indented with tabs. Python 3 disallows mixing the use of tabs and spaces for indentation.
- **Maximum Line Length:** Limit all lines to a maximum of 79 characters. For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters. Limiting the required editor window width makes it possible to have several files open side-by-side, and works well when using code review tools that present the two versions in adjacent columns.
The default wrapping in most tools disrupts the visual structure of the code, making it more difficult to understand. The limits are chosen to avoid wrapping in editors with the window width set to 80, even if the tool places a marker glyph in the final column when wrapping lines. Some web based tools may not offer dynamic line wrapping at all.
The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses. These should be used in preference to using a backslash for line continuation.

### **Should a Line Break Before or After a Binary Operator?**

For decades the recommended style was to break after binary operators. But this can hurt readability in two ways: the operators tend to get scattered across different columns on the screen, and each operator is moved away from its operand and onto the previous line. Here, the eye has to do extra work to tell which items are added and which are subtracted:

Copy

```
# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

To solve this readability problem, mathematicians and their publishers follow the opposite convention. Donald Knuth explains the traditional rule in his [Computers and Typesetting series](https://www-cs-faculty.stanford.edu/~knuth/abcde.html): "Although formulas within a paragraph always break after binary operations and relations, displayed formulas always break before binary operations".

Following the tradition from mathematics usually results in more readable code:

Copy

```
# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

In Python code, it is permissible to break before or after a binary operator, as long as the convention is consistent locally. For new code Knuth's style is suggested.

### **Whitespace in Expressions and Statements**

- Avoid extraneous whitespace. For example, more than one space around an assignment (or other) operator to align it with another.

Copy

```
#Yes:
x = 1
y = 2
long_variable = 3

#No:
x             = 1
y             = 2
long_variable = 3
```

- Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it.
- Always surround these binary operators with a single space on either side: assignment (`=`), augmented assignment (`+=`, `=` etc.), comparisons (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans (`and`, `or`, `not`).
- If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator.

Copy

```
#Yes:
i = i + 1
submitted += 1
x = x_2 - 1
hypot2 = x_x + y*y
c = (a+b) * (a-b)

#No:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

### Module 1:

The common ways to represent algorithms include:

✅ **Flowcharts** – A graphical representation of an algorithm using symbols to show the flow of steps.

✅ **Natural language** – Describing an algorithm in everyday language, though it may be ambiguous.

✅ **Pseudocode** – A structured, human-readable representation of an algorithm that resembles programming logic without specific syntax.

✅ **Pseudocode is ideal for expressing large, complex algorithms.**

➡️ **True** – Pseudocode provides a structured yet flexible way to outline complex algorithms without being tied to a specific programming language..

✅ **Pseudocode helps bridge the gap between flowcharts and actual code.**

➡️ **True** – Pseudocode serves as an intermediary between high-level algorithm representation (e.g., flowcharts) and actual implementation in programming languages.

Insertion sort works by **picking one element at a time** from the unsorted portion and inserting it into its **correct position** in the sorted portion. This ensures that the sorted portion remains ordered as elements are inserted one by one.

Types and Variables in Python

[Python 🐍](../Research%20Paper%20Planner%201763d034d9f780cb993bf4554600d5e7/Reading%20List%201763d034d9f781f7bbbfddf4a9dfb052/Python%20%F0%9F%90%8D%2018f3d034d9f7800d8e24c046970152d9.md) 

## #Comment

# = Comment

## #Block Comment

'''

Comment goes here

'''

## #String

character_name = "Ben"

**Strings are immutable**

A string is a **sequence** of characters. You can access the characters one at a time with the bracket operator:

Copy

```
>>> fruit = 'banana'
>>> letter = fruit[1]
>>>
```

The second statement selects character number 1 from `fruit` and assigns it to `letter`. The expression in brackets is called an **index**. The index indicates which character in the sequence you want (hence the name). But be careful with indices, you might not get what you expect:

Copy

```
>>> print(letter)
 a
>>>
```

## #Integer

character_age = 50

## #Boolean

#0 = false

#1 = true

is_male = True

## #Comparison Figures

== for equal to

>= for greater than and equal to

> for greater than

< for less than

!= for not equal to

And operator

(1 == 2) and ('a' == 'a')

Or operator

(1 == 2) or ('a' == 'a')

**Operator**

**Description**

- *

Exponentiation (raise to the power)

+, -

Unary plus and minus (method names for the last two are +@ and -@)

- , /, %, //

Multiply, divide, modulo and floor division

+, -

Addition and subtraction

>>, <<

Right and left bitwise shift

<=, <, >, >=

Comparison operators

<>, ==, !=

Equality operators

`is`, `is not`

Identity operators

`in`, `not in`

Membership operators

not

Logical operator

and

Logical operator

or

Logical operator

= ,%=, /=, //=, -=, +=, *=, **=

Assignment operators

## Variables

Rules:

Variable names should be lowercase, with words separated by underscores as necessary to improve readability.

**mixedCase** is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.

Variable names can be arbitrarily long. They can contain both letters and numbers, but they have to begin with a letter. It is legal to use uppercase letters, but it is a good idea to begin variable names with a lowercase letter (you'll see why later). The underscore character `'_'` can appear in a name. It is often used in names with multiple words, such as `my_name` or `airspeed_of_unladen_swallow`.

If you give a variable an illegal name, you get a syntax error.

character_name = "Ben"

character_age = "28"

print('his name is ' + character_name + '.')

print('he was ' + character_age + '.')

### #Update Variable

character_name = "Dave"

print('he liked the name ' + character_name + '.')

print('he did not like being ' + character_age + '.')

One of the most common forms of multiple assignment is an `update`, where the new value of the variable depends on the old.

character_name = ‘Ben’

character_name = character_name + ‘Dave’

print(character_name)

## **Multiple assignment**

As you may have discovered, it is legal to make more than one assignment to the same variable. A new assignment makes an existing variable refer to a new value (and stop referring to the old value).

Tuples:

## **Tuples**

A tuple is a sequence of values. The values can be any type, and they are indexed by integers., so in that respect tuples are a lot like lists. The important difference is that tuples are **immutable** (like Strings). Syntactically, a tuple is a comma-separated list of values

### Valid and Invalid Variable Assignments

1. **`5 = x`** ❌ **(Invalid)**
    - This is invalid because in Python, the **left-hand side of an assignment must be a variable**, not a constant.
    - `5` is a constant and cannot be assigned a value.
    - The correct syntax would be `x = 5`.
2. **`x = 10`** ✅ **(Valid)**
    - This is a standard variable assignment, which is completely valid in Python.
3. **`y = z = 20`** ✅ **(Valid)**
    - This is **valid** in Python and is an example of **chained assignment**, where both `y` and `z` get assigned the value `20`.
4. **`a, b = 5, 6`** ✅ **(Valid)**
    - This is **valid** and is an example of **tuple unpacking (multiple assignment)**, where `a` is assigned `5` and `b` is assigned `6`.
    - 

# ## Working With Lists and Indexing ##

Unlike strings, lists are **mutable**. When the bracket operator appears on the left side of an assignment, it identifies the element of the list that will be assigned.

Copy

```
>>> numbers = [17, 123]
>>>> numbers[1] = 5
>>> print(numbers)
 [17, 5]
>>>
```

*#Using [] represents a list for python*

*#Using the number in [] when printing to define which element you require from the list*

*# Allows you to store information in a structure.*

friends = ["Kevin","Karen","Jim"]

print(friends[0])

*# = Kevin*

print(friends[1])

*# = Karen*

print(friends[2])

*# = Jim*

Print(friends)

*# = All the list*

print(friends[0:2])

*# Will print 0,1*

friends = ["Kevin","Karen","Jim"]

print(friends[-0])

# = Jim

friends[1] = "Mike"

print(friends)

#Replaces Value in position 1, "Kevin","Mike","Jim"

Nested List:

mylist = [1,2,[100,200]]

Print(mylist[2][1])

#result would be 200.

Showing this in paper form:

![image.png](The%20Way%20Of%20The%20Program%201b23d034d9f780abaef4db63207f3bb4/969c0488-cb3d-47a3-80f7-90a9230545c1.png)

Swapping values using a temp value:

![image.png](The%20Way%20Of%20The%20Program%201b23d034d9f780abaef4db63207f3bb4/image%201.png)

# **Glossary**

**Problem solving:** The process of formulating a problem, finding a solution, and expressing the solution.

**High-level language:** A programming language like Python that is designed to be easy for humans to read and write.

**Low-level language:** A programming language that is designed to be easy for a computer to execute; also called machine language or assembly language.

**Portability:** A property of a program that can run on more than one kind of computer.

**Interpret:** To execute a program in a high-level language by translating it one line at a time.

**Compile:** To translate a program written in a high-level language into a low-level language all at once, in preparation for later execution.

**Source code:** A program in a high-level language before being compiled.

**Object code:** The output of the compiler after it translates the program.

**Executable:** Another name for object code that is ready to be executed.

**Prompt:** Characters displayed by the interpreter to indicate that it is ready to take input from the user.

**Script:** A program stored in a file (usually one that will be interpreted).

**Interactive mode:** A way of using the Python interpreter by typing commands and expressions at the prompt.

**Script mode:** A way of using the Python interpreter to read and execute statements in a script.

**Program:** A set of instructions that specifies a computation.

**Algorithm:** A general process for solving a category of problems.

**Bug:** An error in a program.

**Debugging:** The process of finding and removing any of the three kinds of programming errors.

**Syntax:** The structure of a program.

**Syntax error:** An error in a program that makes it impossible to parse (and therefore impossible to interpret).

**Exception:** An error that is detected while the program is running.

**Semantics:** The meaning of a program.

**Semantic error:** An error in a program that makes it do something other than what the programmer intended.

**Natural language:** Any one of the languages that people speak that evolved naturally.

**Formal language:** Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs; all programming languages are formal languages.

**Token:** One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.

**Parse:** To examine a program and analyze the syntactic structure.

**Print statement:** An instruction that causes the Python interpreter to display a value on the screen.