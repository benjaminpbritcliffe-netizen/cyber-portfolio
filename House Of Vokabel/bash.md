# Bash

- Most Linux distributions use Bash (Bourne Again Shell) as their default shell.
- The default shell displayed when you open the terminal depends on your Linux distribution

- To see your current working directory, you can execute pwd (Print Working Directory).

- You can change your directory as well. To do that, you can use cd (Change Directory).

- The 'grep' command is a very popular command among Linux users.

This powerful command can search for any word or pattern inside a file.

Unlike the other commands we type in the shell,
we first need to create a file using any text editor for the script.
The file must be named with an extension .sh

Every script should start from shebang.
Shebang is a combination of some characters added at the beginning of a script,
starting with #! followed by the name of the interpreter to use while executing.
As we are writing our script in bash,
let’s define it as the interpreter in the shebang.

## A full script

```` bash

# Defining the Interpreter
#!/bin/bash

# Asking the user to enter a value.
echo "Please enter your name first:"

# Storing the user input value in a variable.
read name

# Checking if the name the user entered is equal to our required name.
if [ "$name" = "Stewart" ]; then

# If it equals the required name, the following line will be displayed.
echo "Welcome Stewart! Here is the secret: THM_Script"

# Defining the sentence to be displayed if the condition fails.
else
        echo "Sorry! You are not authorized to access the secret."
fi
````

```` Bash

# Defining the Interpreter
#!/bin/bash

# Defining the variables
username=""
companyname=""
pin=""

# Defining the loop
for i in {1..3}; do
# Defining the conditional statements
        if [ "$i" -eq 1 ]; then
                echo "Enter your Username:"
                read username
        elif [ "$i" -eq 2 ]; then
                echo "Enter your Company name:"
                read companyname
        else
                echo "Enter your PIN:"
                read pin
        fi
done

# Checking if the user entered the correct details
if [ "$username" = "John" ] && [ "$companyname" = "Tryhackme" ] && [ "$pin" = "7385" ]; then
        echo "Authentication Successful. You can now access your locker, John."
else
        echo "Authentication Denied!!"
fi

````
