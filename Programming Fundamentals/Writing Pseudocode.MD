# Writing Pseudocode

Tags: Idea

Bridge between human language and computing code

Explain ideas to others with non technical background

Improves logic

- Simple and Clear
- Structured
- Abstract

- Capitalize the first word of each line
- Capitalize keywords (FOR, WHILE, etc.)
- Indent to enhance readability and demonstrate the structure
- Maintain clarity (For instance, write 'Add the first variable to the second
  variable' instead of 'Add m to n')

```pseudocode
SET variable to 1
FOR each variable from 1 to 20
  IF variable is even
    PRINT variable
END FOR

```

## **How to Read Pseudocode**

Reading pseudocode is generally straightforward, as it’s designed to be easily
understood. However, there are some common conventions and structures you should
be familiar with:

## **1. Sequential Statements**

Simple statements are written one after another, indicating a sequence of
actions:

```pseudocode
INPUT user_name
PRINT "Hello, " + user_name
CALCULATE total = price * quantity
DISPLAY total
```

## **2. Conditional Statements**

Conditional statements use keywords like IF, ELSE, and ELSE IF to represent
decision-making in the algorithm:

```psuedocode
IF age >= 18 THEN
    PRINT "You are eligible to vote"
ELSE
    PRINT "You are not eligible to vote"
END IF
```

## **3. Loops**

Loops are represented using keywords like WHILE, FOR, or REPEAT-UNTIL:

```psuedocode
FOR i = 1 TO 10
    PRINT i
END FOR

WHILE balance > 0
    SUBTRACT monthly_payment FROM balance
END WHILE
```

## **4. Functions or Procedures**

Functions or procedures are often denoted with keywords like FUNCTION,
PROCEDURE, or METHOD:

```pseudocode
FUNCTION calculate_area(length, width)
    RETURN length * width
END FUNCTION
```

## **5. Input and Output**

Input and output operations are usually indicated with keywords like INPUT,
READ, PRINT, or DISPLAY:

```pseudocode
INPUT user_age
PRINT "Your age is: " + user_age
```

1. **SEQUENCE** represents linear tasks sequentially performed one after the
   other.
2. **WHILE** is a loop with a condition at its beginning.
3. **REPEAT-UNTIL** is a loop with a condition at the bottom.
4. **FOR** is another way of looping.
5. **IF-THEN-ELSE** is \*\*\*\*a [conditional statement](https://builtin.com/data-science/python-conditional-statement)
   changing the flow of the algorithm.
6. **CASE** is the generalization form of IF-THEN-ELSE.

![Pseudocode constructs diagram](https://builtin.com/sites/www.builtin.com/files/styles/ckeditor_optimize/public/inline-images/national/pseudocode%2520constructs.png)

Although these six constructs are the ones we use most often you can
theoretically use them to implement any algorithm. You might find yourself
needing more based on your specific application. Perhaps the two most needed
commands are:

1. Invoking classes
   or [calling functions](https://builtin.com/software-engineering-perspectives/callback-function)
   (using
   the CALL keyword).
2. [Handling exceptions](https://builtin.com/software-engineering-perspectives/how-to-write-clean-exception-handling-code-c%2B%2B)
   (using
   EXCEPTION, 5WHEN keywords).

![Extra pseudocode constructs diagram](https://builtin.com/sites/www.builtin.com/files/styles/ckeditor_optimize/public/inline-images/national/extra%2520pseudocode%2520constructs.png)

Of course, based on the field you’re working in, you might add more constructs
(keywords) to your pseudocode glossary as long as you never use these keywords
as variable names and ensure they’re well-known within your field or company.
