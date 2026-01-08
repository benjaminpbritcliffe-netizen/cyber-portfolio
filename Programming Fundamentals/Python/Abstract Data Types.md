# Abstract Data Types

Data Structure: A way of organising data to make it easier accessible,
update-able etc.

Makes code cleaner

Instance Variabke

\_ = Protected

\_\_ = private

ADT:

Abstract Data Types (ADTs), such as stacks, queues, and linked lists, can be
implemented using classes

Encapsulation:

Group things by each essential features of something. Eg. a Class

Defines boundaries around things. (Instance Variables, Private etc.)

Information Hiding:

Hide certain aspects to the outside.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance

# Using the class
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
print(f"Current balance: ${account.get_balance()}")

# Trying to access hidden attribute
print(account.__balance)  # Will raise an AttributeError

```

| Modifier  | Syntax   | Accessible Outside Class | Accessible in Subclass | Enforced by Python?     |
| --------- | -------- | ------------------------ | ---------------------- | ----------------------- |
| Public    | `name`   | ✅ Yes                   | ✅ Yes                 | ❌ No                   |
| Protected | `_name`  | ⚠️ Yes (but discouraged) | ✅ Yes                 | ❌ No (convention only) |
| Private   | `__name` | ❌ No (mangled)          | ❌ No (unless hacked)  | ✅ Name mangling        |

Classes -

[Classes and Objects | Introduction to programming with Python](https://drlilianblot.gitbook.io/introduction-to-programming-with-python/classes/classes-and-objects)

## Classes & Objects

Classes and objects can be used to create own data types

Class is used to define your own data types.

## Creating a Class (Modelling)

Class used to define something

New File

Student.py

Created a class

class Student:

Anything indented is defined in the class

Use attributes to map out the data types/data required.

## Map out the attributes required

## Create the template

def **init**(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## Using the class to create an object

Is the item that has been defined using the class. What information is placed
into the class

Class used to define something

New File

Student.py

## #Created a class

class Student:

- Anything indented is defined in the class

- Use attributes to map out the data types/data required

- Map out the attributes required

- Create the template

- The object values get passed (stored) to the init function

- Defining the attributes that need to be assigned. Under the def **Init**
  definition

- Example the name of the student needs to be stored against the self.name
  container

def **init**(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## Created a Object using the class above

- 1st student instance = File

- 2nd Student instance = the class

from student import Student

- Using the class named "Student"

student1 = Student("Jim","Business",3.1,False)

## Print a specific part from the Student Data Type

print(student1.name)
