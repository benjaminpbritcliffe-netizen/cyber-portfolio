# While Loop

Created: 17 March 2025 14:38
Class: 1
Is Completed: Yes

# The while Loop

With the while loop we can execute a set of statements as long as a condition is true.

If using a Count Control loop, make sure you update the value inside the loop when using one of these types of loops.

# Example

Print i as long as i is less than 6:

i = 1

while i < 6:  print(i)  i += 1

**The break Statement**

With the break statement we can stop the loop even if the while condition is true:

# Example

Exit the loop when i is 3:

i = 1

while i < 6:  print(i)  if i == 3:    break  i += 1

# The continue Statement

With the continue statement we can stop the current iteration, and continue with the next:

# Example

Continue to the next iteration if i is 3:

i = 0while i < 6:  i += 1  if i == 3:    continue  print(i)

# The else Statement

With the else statement we can run a block of code once when the condition no longer is true:

i = 1

while i < 6:

print(i)

i += 1

else:

print("i is no longer less than 6")

# While True Loop:

Using while True in Python is a common way to create an infinite loop, which continues to execute until it is explicitly broken out of. Here are a few reasons why you might use while True:

Continuous Operation: When you need a program to keep running indefinitely, such as a server listening for incoming connections or a game loop that keeps updating the game state.

while True:
# Server code to handle connections
handle_connections()
Waiting for a Condition: When you need to wait for a specific condition to be met before breaking out of the loop. This is often used in scenarios where the condition is not predictable.

while True:
user_input = input("Enter 'exit' to quit: ")
if user_input.lower() == 'exit':
break
Polling: When you need to repeatedly check for a condition or poll a resource at regular intervals.

import time

while True:
check_status()
time.sleep(5)  # Wait for 5 seconds before checking again
Remember to always include a mechanism to break out of the loop, such as a break statement, to avoid creating an unintentional infinite loop that could cause your program to hang or crash.

while True:
try:
num = int(input('Enter A Number'))
print(num)
except:
print('Not a number!')