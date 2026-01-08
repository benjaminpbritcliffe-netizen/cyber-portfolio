# Control-flow structures

[Code Docs](../Code%20Docs%201b33d034d9f7811784a3f2b49b598b30.csv)

## ALGORITHMS & DATA STRUCTURES

Write a program that asks the user to guess a number between 1 and 10. The
program should

keep asking until the user guesses the correct number. After each attempt, the
program should

display a message indicating if the guess is too low or too high.

## Code Sample

```python
import random
number_to_guess = random.randint(1, 10)

while True:
    try:
        user_input = int(input('Enter a number between 1 and 10'))
        if user_input < number_to_guess:
            print('Too Low')
        elif user_input > number_to_guess:
            print('Too High')
        else:
            print('Correct')
            break
    except:
        print('not a number')
```

Table of Contents

---
