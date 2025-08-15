# Code Tracing and Parson’s Puzzles

Created: 17 March 2025 14:57
Class: 1
Is Completed: Yes

# 2.3.6 Activity: Code Tracing and Parson's Puzzles

## Code comprehension: while loop

Given the following code, identify the variables and trace the program manually, that is write the state diagram of the program on a piece of paper, and update the values of the variables when applicable. What is the output of the program?

```
        text = "a,b,c,d,e,f,g,h,i,j,k,l"
        letters = text.split(",")
        index = 0
        new_list = []
        while index < len(letters):
            new_list.append(letters[index])
            index += 3
        print(new_list)
```

### Model answer:

Here is an [animation showing the execution of the code step by stepLinks to an external site.](https://acos.cs.aalto.fi/html/jsvee/jsvee-python-json/transpiler?url=https://www-users.york.ac.uk/~lb1008/modules/software1/week3-jsvee-whileloop.json). Use the animation to check if your output is correct, and that you properly updated the state diagram after each statements.

## Code comprehension: for loop

Given the following code, identify the variables and trace the program manually, that is write the state diagram of the program on a piece of paper, and update the values of the variables when applicable. What is the output of the program?

```go

        list1 = [1,3,5]
        list2 = [5,9,2]
        list_sum = []
        for index in range(len(list1)):
            list_sum.append(list1[index] + list2[index])
        print(list_sum)

```

### Model answer:

Here is an [animation showing the execution of the code step by stepLinks to an external site.](https://acos.cs.aalto.fi/html/jsvee/jsvee-python-json/transpiler?url=https://www-users.york.ac.uk/~lb1008/modules/software1/week3-jsvee-forloop.json). Use the animation to check if your output is correct, and that you properly updated the state diagram after each statements.

## Parson's puzzle: a simple loop
