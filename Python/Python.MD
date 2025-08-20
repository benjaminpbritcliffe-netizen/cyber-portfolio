# Python

Python

26 August 2021

09:30

# Recommended Tools:

[https://youtu.be/rfscVS0vtbw](https://youtu.be/rfscVS0vtbw)

Python 3 (python.org)

Pycharm (community, jetbrains.com)

Install pip

Install selenium

# ## How to install Pip ##

*# Open a command prompt*

#check

pip --verison

# ## Setting Up Pycharm Project ##

Open Selenium >

File > New Project > Location

Make sure Virtual env Is selected and a location.

Tick Inherit global site-packages.

Click create.

Right click the folder at the left > File > New > Python file > Name (.py)

File should open.

Click Add Configuration > Click + > Python >

Select the file created in script path and make sure python interpreter is green.

Type in the script file print('Hello World') to test.

Click Run button.

# ## Basic Commands/Instructions ##

*The commands are printed in sequential order.*

*Print = send some information to show in the console.*

*\ is used as an escape character.*

*\n used to add a new line.*

## #Comment

# = Comment

## #Block Comment

'''

Comment goes here

'''

## #String

character_name = "Ben"

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

## #Converting number to a string:

*#String converting needs to be done when adding words to the number.*

my_num = 5

print(str(My_num))

## ## Using variables: ##

*#Define the variables at the top or before the variable is first used.*

Example:

character_name = "Ben"

character_age = "28"

print('his name is ' + character_name + '.')

print('he was ' + character_age + '.')

### #Update Variable

character_name = "Dave"

print('he liked the name ' + character_name + '.')

print('he did not like being ' + character_age + '.')

# 

## ## Functions ##

def my_func():

print('hello')

myfunc()

### #Argument required function

#requires one argument to meet the name requirement.

def my_func(name):

print('hello ' + name)

my_func('Jose')

7

### #Using return function.

#Return is saved.

def square(x):

return x**2

result = square(2)

print(result)

### #Default Value function

#No Name is the default value.

def my_func(name='No Name'):

print('hello ' + name)

my_func() #Will use the default value as no name we defined when running the func.

### #upper, lower

phrase = "Giraffe Academy"

print(phrase.upper())

print(phrase.lower())

print(phrase.isupper())

print(phrase.islower())

### #multiple functions

print(phrase.upper().isupper())

### #length of string

print(len(phrase))

### #indexing used to grab part of the phrase:

# Starts at 0

print(phrase[6])

### #index function, find a specific value starting position.

print(phrase.index("G"))

*#Would expect "0"*

### #Replacing a character in a string

phrase = "Giraffe Academy"

print(phrase.replace("G","H"))

*#Expected Result = Hiraffe Academy*

*# Float = Decimal Number, Int = purely just whole number*

### #Adding Numbers together using int command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = int(num1) + int(num2)

### #Adding Numbers together using float command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = float(num1) + float(num2)

print(result)

### #Using .Format Sting Interpolation:

*#input variables into a string using the ".format and {}".*

print("First Name: {FirstName} Surname: {Surname}".format(FirstName="Ben",Surname="Britcliffe"))

### #Splitting by whitespace:

St = "Hello World"

St.split()

*#Converts to a list split at the whitespace.*

Result:

['Hello', 'World']

### Spit at a different character:

*#split a the # character.*

tw = "Hello #Sports"

tw.split('#')

['Hello ', 'Sports']

# 

# ## User Input Commands ##

*#input is used to ask the user to enter some information*

input("Enter your name: ")

*#Store it in a variable*

name = input("Enter your name: ")

age = input("Enter your age: ")

print("Hello " + name + "! You are " + age)

colour = input("Enter Colour : ")

plural_noun = input("Enter Plural Noun : ")

celebrity = input("Enter Celebrity : ")

print("Roses are " + colour)

print( plural_noun + " are blue")

print("I love " + celebrity)

# ## Working With Lists and Indexing ##

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

## #Popping a value out of a list:

Mylist = [1,2,3]

Last = Mylist.pop()

*#Result would be store in the "Last" variable with a value of 3.*

Mylist = [1,2,3]

First = Mylist.pop(0)

*#Result would be stored in the "First" variable as 1*

## #Check if a value is in a list.

'x' in [1,2,3]

*#Will return false as "x" is not in the 1,2,3 list.*

1 in [1,2,3]

*#Will return true as it has found 1 in the list*

Mylist = [1,2,3]

2 in Mylist

*#Result will return true using the related variable name too.*

## #Printing a value from a list in a specific position

mylist = ['a','b','c']

print(mylist[1])

#Result is "b" as lists start at 0.

## #Backwards Counting list.

mylist = ['a','b','c']

print(mylist[-1])

#Result is "c" as lists go backwards on negatives.

## #Changing a value in a specific list position

mylist = ['a','b','c']

mylist[0] = "New"

print(mylist)

['New', 'b', 'c']

## #adding two lists together

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.extend(lucky_numbers)

#printing friends list.

print(friends)

## #Appending a value

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

#adding to the end

friends.append("Jon")

print(friends)

#Result = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie","Jon"]

## #adding to position

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.insert(1,"Kelly")

print(friends)

Result = ["Kevin","Kelly","Karen","Jim","Oscar","Teddy","Charlie"]

## #removing elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.remove("Kevin")

print(friends)

#Result = "Karen","Jim","Oscar","Teddy","Charlie"

## #removing all elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.clear()

print(friends)

#expected result is [] (No values)

## #Finding if a value is in the list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

print(friends.index("Kevin"))

#Result = 0

## 

## #Count how many times the word defined occurs in list.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

print(friends.count("Jim"))

#Result = 2

## 

## #Sort List in ascending order.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends.sort()

print(friends)

## #Copying a list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends2 = friends.copy()

print(friends2)

#Expected Result = # ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

## #Append, Remove and Insert List

names = ["Ben","Dave","Tom","Dick"]

names.append("Harry")

print(names)

names.remove("Dick")

print(names)

names.insert(3,"Richard")

print(names)

## #Tuples

*# A tuple is a data structure/container where different values can be stored.*

*# A () is used to store a tuple*

*# A tuple can not be changed or modified.*

*#A tuple ()*

coordinates = (4,5)

print(coordinates[1])

## 

# ## Using Functions ##

#lambda function

*#Bunch of lines of code which can be called throughout the code*

#This is the function

def say_hi():

*#Anything in the indent = the function*

print("Hello User")

print("Top")

#This calls the function above.

say_hi()

print("Bottom")

*#Parameter is some information given to the function*

*#Name = the parameter, the data is passed along in the calling*

*#Recommended to be done to break up the code based on what its doing…*

def say_hi(name):

print("Hello! " + name)

say_hi("Ben")

## #Return Statement

*#Used to communicate back to user from a function*

*#Nothing can be printed after the return statement.*

*#Return statement breaks out the function.*

def cube(num):

*#expected a RETURN of 27.*

return num * num * num

print(cube(3))

# ## IF Statements

*#Allow programs to make decisions based on certain values/conditions*

is_male = True

is_tall = False

if is_male:

print("You are male")

else:

print("you are not male")

if is_tall:

print("You are tall")

else:

print("You are not tall")

## IF Statement with "OR"

*# Either of the statements need to be true.*

is_male = False

is_tall = True

if is_male or is_tall:

print("You are a male or tall or both")

else:

print("You are neither male or tall")

## IF Statement with "AND"

*#Both statements need to be true*

is_male = True

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

else:

print("Your are either not male or tall or both")

## IF Statement with "Else if" (elif)

*#Have more conditions*

is_male = False

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

elif is_male and not(is_tall):

print("You are a male, but not tall")

elif is_tall and not(is_male):

print("You are tall, but not male.")

else:

print("You are not a male and not tall")

## IF Statement inside a function

*#Using the def status as a function along with elif.*

def status(is_male,is_tall):

if is_male and is_tall:

return ("You are a male and tall ")

elif is_male and not (is_tall):

return ("Your are a male, but not tall")

elif is_tall and not (is_male):

return ("You are tall, but not male.")

else:

return ("You are not a male and not tall")

print(status(False,False))

## If Statement with Inputs

*#Define Variables*

*#Convert inptus to a float.*

num1 = float(input("Enter first number: "))

op = input("Enter operator: ")

num2 = float(input("Enter second number: "))

if op == "+":

print(num1 + num2)

elif op == "-":

print(num1 - num2)

elif op == "/":

print(num1/num2)

elif op == "*":

print(num1 * num2)

else:

print("Invalid operator")

# ## Dictionaries ##

*# Converting a Key into a value.*

*# Key : Values*

*# The keys need to be unique.*

*#Dictionaries do not retain any order.*

*#Dictionary Example*

*# Key : Values*

*# The keys need to be unique.*

*# Can be a number, or a string for the Key*

monthConversions = {

"Jan" : "January",

"Feb" : "February",

"Mar" : "March",

"Apr" : "April",

"May" : "May",

"Jun" : "June",

"Jul" : "July",

"Aug" : "August",

"Sep" : "September",

"Oct" : "October",

"Nov" : "November",

"Dec" : "December",

}

*#Doing it by Key*

print(monthConversions["Nov"])

*#Doing it by the get function*

*#Can use a default value.*

*#Default = "Not A Valid Key"*

print(monthConversions.get("Dec","Not A Valid Key"))

# ## Set##

{1,2,3}

*#all elements are unique, and unordered.*

# 

# ## While Loops ##

*# Allows us to loop through a block of code multiple times while the conditions are met.*

i = 1

while i <= 10:

print(i)

i += 1

print("Done With Loop")

# ## While Loop and If Statement ##

*#Variables*

secret_word = "giraffe"

guess = ""

guess_count = 0

guess_limit = 3

out_of_guesses = False

#While Loop with nested if.

while guess != secret_word and not(out_of_guesses):

if guess_count < guess_limit:

guess = input("Enter Guess: ")

guess_count += 1

print(guess_count)

else:

out_of_guesses = True

if out_of_guesses:

print("Out Of Guesses, You Lose")

else:

print("You Win!")

## Alternative Method:

name = "Ben"

guess = ""

number_tries = 3

tries = 0

while guess != name and tries < number_tries:

guess = input("name: ")

tries += 1

else:

if guess == name:

print("winner")

else:

print("Error")

# ## For Loops ##

*Looping around a set of values.*

## Prints the array in a list.

friends = ["Jim","Karen","John"]

for friend in friends:

print(friend)

## Prints each letter individual

for letter in "giraffe academy":

print(letter)

## Prints values 3 to 9 - Range

*#Stop is up to. Indexing starts at 0.*

for index in range(3,10):

print(index)

## another way to loop

friends = ["Jim","Karen","John"]

for index in range(len(friends)):

print(friends[index])

## 

## Manipulate the range.

for index in range(5):

if index == 0:

print("1st Iteration")

else:

print(index)

## 

## For loop print out list values

## 

seq = [1,2,3,4,5]

for item in seq:

print(item)

## List Comprehension:

*#Both produce the same result. #2 is slightly better performance, but not as readable!*

*#1:*

x = [1,2,3,4,5] #number list

out = [] #blank list

for num in x: #change x to name num

out.append(num**2) #to the power of

print(out)

*#2:*

*#List comprehension*

*#defined x as num in for loop*

x = [1,2,3,4,5] #number list

y = [num**2 for num in x]

print(y)

## Functions used with an if and a for:

def gender(is_male):

if is_male == "Boy":

friends = ["Jim","Tom","Harry"]

elif is_male == "Girl":

friends = ["Karen","Lucy"]

else:

friends = []

print("Incorrect Value")

for friend in friends:

print(friend)

print(len(friends))

# ## 2D List (Nested Lists) ##

*Number Grid, nested lists, using 2 criterias in the print, Row and Column*

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

# ## 2D For Loops (Nested For Loops)

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

*#Nested For Loop*

*#2D Array*

for row in number_grid:

for column in row:

print(column)

# ## For Loop and Nested If loop:

def translate(phrase):

translation = ""

for letter in phrase:

if letter in "AEIOUaeiou":

#Append the letter to the string

translation = translation + "g"

else:

#append the letter to the string

translation = translation + letter

return translation

print(translate(input("Enter Phrase: ")))

# ## Error Catching/Handling ##

*#Try Except, try the information given, if it fails (specific error), write a failure message*

*#All errors*

try:

number = int(input("Enter a number:"))

print(number)

except:

print('NO')

*#Specific error catch*

try:

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('NO')

## ## Multiple Error Catching

try:

#value = 10/0

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('Value Error')

except ZeroDivisionError:

print("Div by zero error")

# ## Reading from external files ##

*#Using the python read command*

*#Modes = r is read, w is write, a is append, r+ is read and write.*

## #Open the file and save as a variable:

employee_file = open("employees.txt","r")

## #check the file is readable

print(employee_file.readable())

## #Prints all the info

print(employee_file.read())

## #reads the first line.

print(employee_file.readline())

*#Moves down a line after the read line command.*

*#example this would read second line:*

print(employee_file.readline())

## #Read all the lines into an string list:

for each_employee in employee_file.readlines():

print(each_employee)

## #Read all lines into array:

print(employee_file.readlines())

## #Close the file at the end

employee_file.close()

# ##Writing and Appending To File ##

## 

## #Appending

*#Modes = r is read, w is write, a is append, r+ is read and write.*

employee_file = open("employees.txt","a")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

## #Write a new file (overwrite)

#Overwrites the file

#Modes = r is read, w is write, a is append, r+ is read and write.

employee_file = open("employees.txt","w")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

# ## Modules ##

## #Creating your own Modules

*#Importing a module into another python file*

*#Tools.py*

feet_in_mile = 5280

meters_in_kilometer = 1000

def hello_world(word):

return word

*#App.py*

import tools

print(tools.hello_world("Hello"))

print(tools.meters_in_kilometer)

## #Official Modules

[https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

## # How to use external modules

*# Available in the External Libraries > Lib Folder*

*# site-packages is the installed packages list.*

#Checking if pip is installed first!

pip --verison

*#example for python docx*

pip install python-docx

or can use the settings > python interpreter > click the "+" and Install package

# ##Classes & Objects

*#Classes and objects can be used to create own data types*

*#Class is used to define your own data types.*

## # Creating a Class (Modelling)

*#Class used to define something*

*#New File*

*#Student.py*

*#Created a class*

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

#Map out the attributes required..

*# Create the template.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## #Using the class to create an object

*#Is the item that has been defined using the class. What information is placed into the class*

*#Class used to define something*

*#New File*

*#Student.py*

## 

## #Created a class

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

*#Map out the attributes required..*

*# Create the template.*

*#The object values get passed (stored) to the init function.*

*#Defining the attributes that need to be assigned. Under the def __Init__ definition.*

*#Example the name of the student needs to be stored against the self.name container.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## # Created a Object using the class above.

*#1st student instance = File*

*#2nd Student instance = the class*

from student import Student

*#Using the class named "Student"*

student1 = Student("Jim","Business",3.1,False)

*#Print a specific part from the Student Data Type*

print(student1.name)

# ## Multiple Choice Quiz ##

## 

## #Using Classes, If Statements and Loops.

*#question.py*

class Question:

def __init__(self,prompt,answer):

self.prompt = prompt

self.answer = answer

*#app.py*

from Question import Question

*#Array of the questions which you want to prompt the user with*

question_prompts = [

"What colour are Apples\n(a) Red/Green\n (b) Purple\n(C) Orange\n \n",

"What colour are Bananas\n(a) Teal\n (b) Magenta\n(C) Yellow\n \n",

"What colour are Strawberries\n(a) Yellow\n (b) Red\n(C) Blue\n \n"

]

*#Array of questions, with the expected prompt and the answer.*

*#Link the question to the answer using the expected question_prompts class.*

questions = [

Question(question_prompts[0],"a"),

Question(question_prompts[1], "c"),

Question(question_prompts[2], "b"),

]

*#Create with a list of questions that want to be answered,and loop through questions*

def run_test(questions):

*#Reset score/set score to 0*

score = 0

#For each question in the array, what do we do..

for each_question in questions:

*#Assign the answer to the variable.*

answer = input(each_question.prompt).lower()

*#If the answer above is the same as the stored answer from the object above.*

if answer == each_question.answer:

score +=1

print("You got " + str(score)+"/" + str(len(questions))+" Correct")

*#run the definition*

run_test(questions)

# ## Second Class and Object Example

*#Question.py*

class Dog:

*#Given an attribute, Init = anything that is required for user to give.*

def __init__(self,name,age):

self.name = name

self.age = age

def get_name(self):

return self.name

def get_age(self):

return self.age

*#App.py*

from Question import Dog

d = Dog("Ben",27)

e = Dog("Dave",28)

print(str(d.get_name())+" - " + str(d.get_age()))

print(str(e.get_name())+" - " + str(e.get_age()))

# ## Giving each item a definition line - Classes and Objects

*#Question.py*

*#Give the class a name*

class Item:

#Given an attribute, Init = anything that is required for user to give.

def __init__(self,serial_no,item,price,in_stock):

self.serial_no = serial_no

self.item = item

self.price = price

self.in_stock = in_stock

*#Give each value required a definition line.*

def get_serial_no(self):

return self.serial_no,"Extra Return"

*#Use a comma if want to return more than one value*

def get_item(self):

return self.item

def get_price(self):

return self.price

def get_in_stock(self):

return self.in_stock

*#App.py*

*#Import the Class form external file*

from Question import Item

#def __init__(self,serial_no,item,price,in_stock):

*#Create an array to store multiple items.*

items =[

*#Give a value to the required Item attributes.*

Item("1234","Product A","3.50",False),

Item("5678","Product B","3.50",False)

]

*#Print out the serial number for each line of the above array.*

for each_line in items:

#Expected 5678

print(each_line.get_serial_no())

# # Inheritance of Classes

*#Inherit the classes from another class into a separate class*

*#Question.py*

class Chef:

def make_chicken(self):

print("The chef makes chicken")

def make_salad(self):

print("The chef makes a salad")

def make_special_dish(self):

print("The chef makes bbq ribs")

*# Inherit Chef*

*# Innehrit functions from another class by putting the inherited class in the ()*

class ChineseChef(Chef):

def make_fried_rice(self):

print("make fried rice")

def make_special_dish(self):

print("Make Orange Chicken")

*#App.py*

from Question import Chef

from Question import ChineseChef

myChef = Chef()

myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_special_dish()

myChineseChef.make_chicken()

# #Using Classes, Object and Writing to a file

*#Myclasses.py*

class Student:

def __init__(self,name,age,dob):

self.name = name

self.age = age

self.dob = dob

def get_info(self):

return self.name,self.age,self.dob

*#Main.py*

*#Import the class*

*from myClasses import Student*

*#Add the values to the required objects.*

#def __init__(self,name,age,dob):

students = [

Student("Bill",21,"27/05/1974"),

Student("Ben", 24, "28/05/1994")

]

*#Loop through the object class list.*

for each_student in students:

#Convert the Class list into a normal list.

all = list(each_student.get_info())

#print(all)

#Convert normal list to string values.

string = ','.join([str(item) for item in all])

#Open and write values to the file.]

f = open("students.txt", "a")

f.write(str(string)+"\n")

f.close()

## #Classes and Objects Examples

*#myClasses.py*

class Person:

def __init__(self, name, age):

self.name = name

self.age = age

class Vehicle:

def __init__(self, make, model, age):

self.make = make

self.model = model

self.age = age

# Instance method

def description(self):

return f"{self.make} {self.model}"

# Another instance method

def speak(self, sound):

return f"{self.make} says {sound}"

class PersonsDetails:

def __init__(self, name, age):

self.name = name

self.age = age

def myageis(self):

print("And My Age Is " + self.age)

def greetings(self):

print("Hello My Name Is " + self.name)

*#Main.py*

from myClasses import Person,Vehicle,PersonsDetails

print("Vehicle Example")

car1 = Vehicle("Honda", "Jazz", 4)

print(car1.description())

print(car1.make)

print(car1.speak("Beep"))

print("---------------")

print("Persons Details")

x = PersonsDetails("Ben", "28")

print(x.name)

print(x.age)

x.greetings()

x.myageis()

print("---------------")

print("Person")

p1 = Person("John", 36)

print(p1.name)

print(p1.age)

## #Example 2

*#myClasses.py*

class test:

def __init__(self):

pass

*#Main.py*

*#Create a class which will be a container of related object information*

*#Example, we create a class of "Car"*

class Car:

#We create a def and allocate under the init def the REQUIRED fields.

def __init__(self,registration):

self.registration = registration

#We create more behaviours as a def file.

def drive(self):

print("I can drive!")

*#Ford is an object, the 200 is allocating a value to the REQUIRED Registration value.*

*#Example every car requires a registration plate.*

ford = Car("AA12VHK")

honda = Car("BB17ABD")

audi = Car("CC20VDF")

*#We can define more attributes on the fly too.*

ford.speed = 200

honda.speed = 220

audi.speed = 250

*#Printing the values of the required object, and on-the-fly object.*

print(ford.registration)

print(ford.speed)

*#Using other defs and allocating them to the object.. No Print required just "call" the defined function*

ford.drive()

*#Trying a class with no definition and importing from another file.*

from myClasses import test

no_requirements = test()

test1 = no_requirements

test1.test = "Test"

print(test1.test)


# Python

Python

26 August 2021

09:30

# Recommended Tools:

[https://youtu.be/rfscVS0vtbw](https://youtu.be/rfscVS0vtbw)

Python 3 (python.org)

Pycharm (community, jetbrains.com)

Install pip

Install selenium

# ## How to install Pip ##

*# Open a command prompt*

#check

pip --verison

# ## Setting Up Pycharm Project ##

Open Selenium >

File > New Project > Location

Make sure Virtual env Is selected and a location.

Tick Inherit global site-packages.

Click create.

Right click the folder at the left > File > New > Python file > Name (.py)

File should open.

Click Add Configuration > Click + > Python >

Select the file created in script path and make sure python interpreter is green.

Type in the script file print('Hello World') to test.

Click Run button.

# ## Basic Commands/Instructions ##

*The commands are printed in sequential order.*

*Print = send some information to show in the console.*

*\ is used as an escape character.*

*\n used to add a new line.*

## #Comment

# = Comment

## #Block Comment

'''

Comment goes here

'''

## #String

character_name = "Ben"

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

## #Converting number to a string:

*#String converting needs to be done when adding words to the number.*

my_num = 5

print(str(My_num))

## ## Using variables: ##

*#Define the variables at the top or before the variable is first used.*

Example:

character_name = "Ben"

character_age = "28"

print('his name is ' + character_name + '.')

print('he was ' + character_age + '.')

### #Update Variable

character_name = "Dave"

print('he liked the name ' + character_name + '.')

print('he did not like being ' + character_age + '.')

# 

## ## Functions ##

def my_func():

print('hello')

myfunc()

### #Argument required function

#requires one argument to meet the name requirement.

def my_func(name):

print('hello ' + name)

my_func('Jose')

7

### #Using return function.

#Return is saved.

def square(x):

return x**2

result = square(2)

print(result)

### #Default Value function

#No Name is the default value.

def my_func(name='No Name'):

print('hello ' + name)

my_func() #Will use the default value as no name we defined when running the func.

### #upper, lower

phrase = "Giraffe Academy"

print(phrase.upper())

print(phrase.lower())

print(phrase.isupper())

print(phrase.islower())

### #multiple functions

print(phrase.upper().isupper())

### #length of string

print(len(phrase))

### #indexing used to grab part of the phrase:

# Starts at 0

print(phrase[6])

### #index function, find a specific value starting position.

print(phrase.index("G"))

*#Would expect "0"*

### #Replacing a character in a string

phrase = "Giraffe Academy"

print(phrase.replace("G","H"))

*#Expected Result = Hiraffe Academy*

*# Float = Decimal Number, Int = purely just whole number*

### #Adding Numbers together using int command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = int(num1) + int(num2)

### #Adding Numbers together using float command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = float(num1) + float(num2)

print(result)

### #Using .Format Sting Interpolation:

*#input variables into a string using the ".format and {}".*

print("First Name: {FirstName} Surname: {Surname}".format(FirstName="Ben",Surname="Britcliffe"))

### #Splitting by whitespace:

St = "Hello World"

St.split()

*#Converts to a list split at the whitespace.*

Result:

['Hello', 'World']

### Spit at a different character:

*#split a the # character.*

tw = "Hello #Sports"

tw.split('#')

['Hello ', 'Sports']

# 

# ## User Input Commands ##

*#input is used to ask the user to enter some information*

input("Enter your name: ")

*#Store it in a variable*

name = input("Enter your name: ")

age = input("Enter your age: ")

print("Hello " + name + "! You are " + age)

colour = input("Enter Colour : ")

plural_noun = input("Enter Plural Noun : ")

celebrity = input("Enter Celebrity : ")

print("Roses are " + colour)

print( plural_noun + " are blue")

print("I love " + celebrity)

# ## Working With Lists and Indexing ##

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

## #Popping a value out of a list:

Mylist = [1,2,3]

Last = Mylist.pop()

*#Result would be store in the "Last" variable with a value of 3.*

Mylist = [1,2,3]

First = Mylist.pop(0)

*#Result would be stored in the "First" variable as 1*

## #Check if a value is in a list.

'x' in [1,2,3]

*#Will return false as "x" is not in the 1,2,3 list.*

1 in [1,2,3]

*#Will return true as it has found 1 in the list*

Mylist = [1,2,3]

2 in Mylist

*#Result will return true using the related variable name too.*

## #Printing a value from a list in a specific position

mylist = ['a','b','c']

print(mylist[1])

#Result is "b" as lists start at 0.

## #Backwards Counting list.

mylist = ['a','b','c']

print(mylist[-1])

#Result is "c" as lists go backwards on negatives.

## #Changing a value in a specific list position

mylist = ['a','b','c']

mylist[0] = "New"

print(mylist)

['New', 'b', 'c']

## #adding two lists together

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.extend(lucky_numbers)

#printing friends list.

print(friends)

## #Appending a value

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

#adding to the end

friends.append("Jon")

print(friends)

#Result = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie","Jon"]

## #adding to position

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.insert(1,"Kelly")

print(friends)

Result = ["Kevin","Kelly","Karen","Jim","Oscar","Teddy","Charlie"]

## #removing elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.remove("Kevin")

print(friends)

#Result = "Karen","Jim","Oscar","Teddy","Charlie"

## #removing all elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.clear()

print(friends)

#expected result is [] (No values)

## #Finding if a value is in the list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

print(friends.index("Kevin"))

#Result = 0

## 

## #Count how many times the word defined occurs in list.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

print(friends.count("Jim"))

#Result = 2

## 

## #Sort List in ascending order.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends.sort()

print(friends)

## #Copying a list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends2 = friends.copy()

print(friends2)

#Expected Result = # ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

## #Append, Remove and Insert List

names = ["Ben","Dave","Tom","Dick"]

names.append("Harry")

print(names)

names.remove("Dick")

print(names)

names.insert(3,"Richard")

print(names)

## #Tuples

*# A tuple is a data structure/container where different values can be stored.*

*# A () is used to store a tuple*

*# A tuple can not be changed or modified.*

*#A tuple ()*

coordinates = (4,5)

print(coordinates[1])

## 

# ## Using Functions ##

#lambda function

*#Bunch of lines of code which can be called throughout the code*

#This is the function

def say_hi():

*#Anything in the indent = the function*

print("Hello User")

print("Top")

#This calls the function above.

say_hi()

print("Bottom")

*#Parameter is some information given to the function*

*#Name = the parameter, the data is passed along in the calling*

*#Recommended to be done to break up the code based on what its doing…*

def say_hi(name):

print("Hello! " + name)

say_hi("Ben")

## #Return Statement

*#Used to communicate back to user from a function*

*#Nothing can be printed after the return statement.*

*#Return statement breaks out the function.*

def cube(num):

*#expected a RETURN of 27.*

return num * num * num

print(cube(3))

# ## IF Statements

*#Allow programs to make decisions based on certain values/conditions*

is_male = True

is_tall = False

if is_male:

print("You are male")

else:

print("you are not male")

if is_tall:

print("You are tall")

else:

print("You are not tall")

## IF Statement with "OR"

*# Either of the statements need to be true.*

is_male = False

is_tall = True

if is_male or is_tall:

print("You are a male or tall or both")

else:

print("You are neither male or tall")

## IF Statement with "AND"

*#Both statements need to be true*

is_male = True

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

else:

print("Your are either not male or tall or both")

## IF Statement with "Else if" (elif)

*#Have more conditions*

is_male = False

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

elif is_male and not(is_tall):

print("You are a male, but not tall")

elif is_tall and not(is_male):

print("You are tall, but not male.")

else:

print("You are not a male and not tall")

## IF Statement inside a function

*#Using the def status as a function along with elif.*

def status(is_male,is_tall):

if is_male and is_tall:

return ("You are a male and tall ")

elif is_male and not (is_tall):

return ("Your are a male, but not tall")

elif is_tall and not (is_male):

return ("You are tall, but not male.")

else:

return ("You are not a male and not tall")

print(status(False,False))

## If Statement with Inputs

*#Define Variables*

*#Convert inptus to a float.*

num1 = float(input("Enter first number: "))

op = input("Enter operator: ")

num2 = float(input("Enter second number: "))

if op == "+":

print(num1 + num2)

elif op == "-":

print(num1 - num2)

elif op == "/":

print(num1/num2)

elif op == "*":

print(num1 * num2)

else:

print("Invalid operator")

# ## Dictionaries ##

*# Converting a Key into a value.*

*# Key : Values*

*# The keys need to be unique.*

*#Dictionaries do not retain any order.*

*#Dictionary Example*

*# Key : Values*

*# The keys need to be unique.*

*# Can be a number, or a string for the Key*

monthConversions = {

"Jan" : "January",

"Feb" : "February",

"Mar" : "March",

"Apr" : "April",

"May" : "May",

"Jun" : "June",

"Jul" : "July",

"Aug" : "August",

"Sep" : "September",

"Oct" : "October",

"Nov" : "November",

"Dec" : "December",

}

*#Doing it by Key*

print(monthConversions["Nov"])

*#Doing it by the get function*

*#Can use a default value.*

*#Default = "Not A Valid Key"*

print(monthConversions.get("Dec","Not A Valid Key"))

# ## Set##

{1,2,3}

*#all elements are unique, and unordered.*

# 

# ## While Loops ##

*# Allows us to loop through a block of code multiple times while the conditions are met.*

i = 1

while i <= 10:

print(i)

i += 1

print("Done With Loop")

# ## While Loop and If Statement ##

*#Variables*

secret_word = "giraffe"

guess = ""

guess_count = 0

guess_limit = 3

out_of_guesses = False

#While Loop with nested if.

while guess != secret_word and not(out_of_guesses):

if guess_count < guess_limit:

guess = input("Enter Guess: ")

guess_count += 1

print(guess_count)

else:

out_of_guesses = True

if out_of_guesses:

print("Out Of Guesses, You Lose")

else:

print("You Win!")

## Alternative Method:

name = "Ben"

guess = ""

number_tries = 3

tries = 0

while guess != name and tries < number_tries:

guess = input("name: ")

tries += 1

else:

if guess == name:

print("winner")

else:

print("Error")

# ## For Loops ##

*Looping around a set of values.*

## Prints the array in a list.

friends = ["Jim","Karen","John"]

for friend in friends:

print(friend)

## Prints each letter individual

for letter in "giraffe academy":

print(letter)

## Prints values 3 to 9 - Range

*#Stop is up to. Indexing starts at 0.*

for index in range(3,10):

print(index)

## another way to loop

friends = ["Jim","Karen","John"]

for index in range(len(friends)):

print(friends[index])

## 

## Manipulate the range.

for index in range(5):

if index == 0:

print("1st Iteration")

else:

print(index)

## 

## For loop print out list values

## 

seq = [1,2,3,4,5]

for item in seq:

print(item)

## List Comprehension:

*#Both produce the same result. #2 is slightly better performance, but not as readable!*

*#1:*

x = [1,2,3,4,5] #number list

out = [] #blank list

for num in x: #change x to name num

out.append(num**2) #to the power of

print(out)

*#2:*

*#List comprehension*

*#defined x as num in for loop*

x = [1,2,3,4,5] #number list

y = [num**2 for num in x]

print(y)

## Functions used with an if and a for:

def gender(is_male):

if is_male == "Boy":

friends = ["Jim","Tom","Harry"]

elif is_male == "Girl":

friends = ["Karen","Lucy"]

else:

friends = []

print("Incorrect Value")

for friend in friends:

print(friend)

print(len(friends))

# ## 2D List (Nested Lists) ##

*Number Grid, nested lists, using 2 criterias in the print, Row and Column*

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

# ## 2D For Loops (Nested For Loops)

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

*#Nested For Loop*

*#2D Array*

for row in number_grid:

for column in row:

print(column)

# ## For Loop and Nested If loop:

def translate(phrase):

translation = ""

for letter in phrase:

if letter in "AEIOUaeiou":

#Append the letter to the string

translation = translation + "g"

else:

#append the letter to the string

translation = translation + letter

return translation

print(translate(input("Enter Phrase: ")))

# ## Error Catching/Handling ##

*#Try Except, try the information given, if it fails (specific error), write a failure message*

*#All errors*

try:

number = int(input("Enter a number:"))

print(number)

except:

print('NO')

*#Specific error catch*

try:

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('NO')

## ## Multiple Error Catching

try:

#value = 10/0

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('Value Error')

except ZeroDivisionError:

print("Div by zero error")

# ## Reading from external files ##

*#Using the python read command*

*#Modes = r is read, w is write, a is append, r+ is read and write.*

## #Open the file and save as a variable:

employee_file = open("employees.txt","r")

## #check the file is readable

print(employee_file.readable())

## #Prints all the info

print(employee_file.read())

## #reads the first line.

print(employee_file.readline())

*#Moves down a line after the read line command.*

*#example this would read second line:*

print(employee_file.readline())

## #Read all the lines into an string list:

for each_employee in employee_file.readlines():

print(each_employee)

## #Read all lines into array:

print(employee_file.readlines())

## #Close the file at the end

employee_file.close()

# ##Writing and Appending To File ##

## 

## #Appending

*#Modes = r is read, w is write, a is append, r+ is read and write.*

employee_file = open("employees.txt","a")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

## #Write a new file (overwrite)

#Overwrites the file

#Modes = r is read, w is write, a is append, r+ is read and write.

employee_file = open("employees.txt","w")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

# ## Modules ##

## #Creating your own Modules

*#Importing a module into another python file*

*#Tools.py*

feet_in_mile = 5280

meters_in_kilometer = 1000

def hello_world(word):

return word

*#App.py*

import tools

print(tools.hello_world("Hello"))

print(tools.meters_in_kilometer)

## #Official Modules

[https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

## # How to use external modules

*# Available in the External Libraries > Lib Folder*

*# site-packages is the installed packages list.*

#Checking if pip is installed first!

pip --verison

*#example for python docx*

pip install python-docx

or can use the settings > python interpreter > click the "+" and Install package

# ##Classes & Objects

*#Classes and objects can be used to create own data types*

*#Class is used to define your own data types.*

## # Creating a Class (Modelling)

*#Class used to define something*

*#New File*

*#Student.py*

*#Created a class*

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

#Map out the attributes required..

*# Create the template.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## #Using the class to create an object

*#Is the item that has been defined using the class. What information is placed into the class*

*#Class used to define something*

*#New File*

*#Student.py*

## 

## #Created a class

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

*#Map out the attributes required..*

*# Create the template.*

*#The object values get passed (stored) to the init function.*

*#Defining the attributes that need to be assigned. Under the def __Init__ definition.*

*#Example the name of the student needs to be stored against the self.name container.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## # Created a Object using the class above.

*#1st student instance = File*

*#2nd Student instance = the class*

from student import Student

*#Using the class named "Student"*

student1 = Student("Jim","Business",3.1,False)

*#Print a specific part from the Student Data Type*

print(student1.name)

# ## Multiple Choice Quiz ##

## 

## #Using Classes, If Statements and Loops.

*#question.py*

class Question:

def __init__(self,prompt,answer):

self.prompt = prompt

self.answer = answer

*#app.py*

from Question import Question

*#Array of the questions which you want to prompt the user with*

question_prompts = [

"What colour are Apples\n(a) Red/Green\n (b) Purple\n(C) Orange\n \n",

"What colour are Bananas\n(a) Teal\n (b) Magenta\n(C) Yellow\n \n",

"What colour are Strawberries\n(a) Yellow\n (b) Red\n(C) Blue\n \n"

]

*#Array of questions, with the expected prompt and the answer.*

*#Link the question to the answer using the expected question_prompts class.*

questions = [

Question(question_prompts[0],"a"),

Question(question_prompts[1], "c"),

Question(question_prompts[2], "b"),

]

*#Create with a list of questions that want to be answered,and loop through questions*

def run_test(questions):

*#Reset score/set score to 0*

score = 0

#For each question in the array, what do we do..

for each_question in questions:

*#Assign the answer to the variable.*

answer = input(each_question.prompt).lower()

*#If the answer above is the same as the stored answer from the object above.*

if answer == each_question.answer:

score +=1

print("You got " + str(score)+"/" + str(len(questions))+" Correct")

*#run the definition*

run_test(questions)

# ## Second Class and Object Example

*#Question.py*

class Dog:

*#Given an attribute, Init = anything that is required for user to give.*

def __init__(self,name,age):

self.name = name

self.age = age

def get_name(self):

return self.name

def get_age(self):

return self.age

*#App.py*

from Question import Dog

d = Dog("Ben",27)

e = Dog("Dave",28)

print(str(d.get_name())+" - " + str(d.get_age()))

print(str(e.get_name())+" - " + str(e.get_age()))

# ## Giving each item a definition line - Classes and Objects

*#Question.py*

*#Give the class a name*

class Item:

#Given an attribute, Init = anything that is required for user to give.

def __init__(self,serial_no,item,price,in_stock):

self.serial_no = serial_no

self.item = item

self.price = price

self.in_stock = in_stock

*#Give each value required a definition line.*

def get_serial_no(self):

return self.serial_no,"Extra Return"

*#Use a comma if want to return more than one value*

def get_item(self):

return self.item

def get_price(self):

return self.price

def get_in_stock(self):

return self.in_stock

*#App.py*

*#Import the Class form external file*

from Question import Item

#def __init__(self,serial_no,item,price,in_stock):

*#Create an array to store multiple items.*

items =[

*#Give a value to the required Item attributes.*

Item("1234","Product A","3.50",False),

Item("5678","Product B","3.50",False)

]

*#Print out the serial number for each line of the above array.*

for each_line in items:

#Expected 5678

print(each_line.get_serial_no())

# # Inheritance of Classes

*#Inherit the classes from another class into a separate class*

*#Question.py*

class Chef:

def make_chicken(self):

print("The chef makes chicken")

def make_salad(self):

print("The chef makes a salad")

def make_special_dish(self):

print("The chef makes bbq ribs")

*# Inherit Chef*

*# Innehrit functions from another class by putting the inherited class in the ()*

class ChineseChef(Chef):

def make_fried_rice(self):

print("make fried rice")

def make_special_dish(self):

print("Make Orange Chicken")

*#App.py*

from Question import Chef

from Question import ChineseChef

myChef = Chef()

myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_special_dish()

myChineseChef.make_chicken()

# #Using Classes, Object and Writing to a file

*#Myclasses.py*

class Student:

def __init__(self,name,age,dob):

self.name = name

self.age = age

self.dob = dob

def get_info(self):

return self.name,self.age,self.dob

*#Main.py*

*#Import the class*

*from myClasses import Student*

*#Add the values to the required objects.*

#def __init__(self,name,age,dob):

students = [

Student("Bill",21,"27/05/1974"),

Student("Ben", 24, "28/05/1994")

]

*#Loop through the object class list.*

for each_student in students:

#Convert the Class list into a normal list.

all = list(each_student.get_info())

#print(all)

#Convert normal list to string values.

string = ','.join([str(item) for item in all])

#Open and write values to the file.]

f = open("students.txt", "a")

f.write(str(string)+"\n")

f.close()

## #Classes and Objects Examples

*#myClasses.py*

class Person:

def __init__(self, name, age):

self.name = name

self.age = age

class Vehicle:

def __init__(self, make, model, age):

self.make = make

self.model = model

self.age = age

# Instance method

def description(self):

return f"{self.make} {self.model}"

# Another instance method

def speak(self, sound):

return f"{self.make} says {sound}"

class PersonsDetails:

def __init__(self, name, age):

self.name = name

self.age = age

def myageis(self):

print("And My Age Is " + self.age)

def greetings(self):

print("Hello My Name Is " + self.name)

*#Main.py*

from myClasses import Person,Vehicle,PersonsDetails

print("Vehicle Example")

car1 = Vehicle("Honda", "Jazz", 4)

print(car1.description())

print(car1.make)

print(car1.speak("Beep"))

print("---------------")

print("Persons Details")

x = PersonsDetails("Ben", "28")

print(x.name)

print(x.age)

x.greetings()

x.myageis()

print("---------------")

print("Person")

p1 = Person("John", 36)

print(p1.name)

print(p1.age)

## #Example 2

*#myClasses.py*

class test:

def __init__(self):

pass

*#Main.py*

*#Create a class which will be a container of related object information*

*#Example, we create a class of "Car"*

class Car:

#We create a def and allocate under the init def the REQUIRED fields.

def __init__(self,registration):

self.registration = registration

#We create more behaviours as a def file.

def drive(self):

print("I can drive!")

*#Ford is an object, the 200 is allocating a value to the REQUIRED Registration value.*

*#Example every car requires a registration plate.*

ford = Car("AA12VHK")

honda = Car("BB17ABD")

audi = Car("CC20VDF")

*#We can define more attributes on the fly too.*

ford.speed = 200

honda.speed = 220

audi.speed = 250

*#Printing the values of the required object, and on-the-fly object.*

print(ford.registration)

print(ford.speed)

*#Using other defs and allocating them to the object.. No Print required just "call" the defined function*

ford.drive()

*#Trying a class with no definition and importing from another file.*

from myClasses import test

no_requirements = test()

test1 = no_requirements

test1.test = "Test"

print(test1.test)

# Python

Python

26 August 2021

09:30

# Recommended Tools:

[https://youtu.be/rfscVS0vtbw](https://youtu.be/rfscVS0vtbw)

Python 3 (python.org)

Pycharm (community, jetbrains.com)

Install pip

Install selenium

# ## How to install Pip ##

*# Open a command prompt*

#check

pip --verison

# ## Setting Up Pycharm Project ##

Open Selenium >

File > New Project > Location

Make sure Virtual env Is selected and a location.

Tick Inherit global site-packages.

Click create.

Right click the folder at the left > File > New > Python file > Name (.py)

File should open.

Click Add Configuration > Click + > Python >

Select the file created in script path and make sure python interpreter is green.

Type in the script file print('Hello World') to test.

Click Run button.

# ## Basic Commands/Instructions ##

*The commands are printed in sequential order.*

*Print = send some information to show in the console.*

*\ is used as an escape character.*

*\n used to add a new line.*

## #Comment

# = Comment

## #Block Comment

'''

Comment goes here

'''

## #String

character_name = "Ben"

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

## #Converting number to a string:

*#String converting needs to be done when adding words to the number.*

my_num = 5

print(str(My_num))

## ## Using variables: ##

*#Define the variables at the top or before the variable is first used.*

Example:

character_name = "Ben"

character_age = "28"

print('his name is ' + character_name + '.')

print('he was ' + character_age + '.')

### #Update Variable

character_name = "Dave"

print('he liked the name ' + character_name + '.')

print('he did not like being ' + character_age + '.')

# 

## ## Functions ##

def my_func():

print('hello')

myfunc()

### #Argument required function

#requires one argument to meet the name requirement.

def my_func(name):

print('hello ' + name)

my_func('Jose')

7

### #Using return function.

#Return is saved.

def square(x):

return x**2

result = square(2)

print(result)

### #Default Value function

#No Name is the default value.

def my_func(name='No Name'):

print('hello ' + name)

my_func() #Will use the default value as no name we defined when running the func.

### #upper, lower

phrase = "Giraffe Academy"

print(phrase.upper())

print(phrase.lower())

print(phrase.isupper())

print(phrase.islower())

### #multiple functions

print(phrase.upper().isupper())

### #length of string

print(len(phrase))

### #indexing used to grab part of the phrase:

# Starts at 0

print(phrase[6])

### #index function, find a specific value starting position.

print(phrase.index("G"))

*#Would expect "0"*

### #Replacing a character in a string

phrase = "Giraffe Academy"

print(phrase.replace("G","H"))

*#Expected Result = Hiraffe Academy*

*# Float = Decimal Number, Int = purely just whole number*

### #Adding Numbers together using int command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = int(num1) + int(num2)

### #Adding Numbers together using float command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = float(num1) + float(num2)

print(result)

### #Using .Format Sting Interpolation:

*#input variables into a string using the ".format and {}".*

print("First Name: {FirstName} Surname: {Surname}".format(FirstName="Ben",Surname="Britcliffe"))

### #Splitting by whitespace:

St = "Hello World"

St.split()

*#Converts to a list split at the whitespace.*

Result:

['Hello', 'World']

### Spit at a different character:

*#split a the # character.*

tw = "Hello #Sports"

tw.split('#')

['Hello ', 'Sports']

# 

# ## User Input Commands ##

*#input is used to ask the user to enter some information*

input("Enter your name: ")

*#Store it in a variable*

name = input("Enter your name: ")

age = input("Enter your age: ")

print("Hello " + name + "! You are " + age)

colour = input("Enter Colour : ")

plural_noun = input("Enter Plural Noun : ")

celebrity = input("Enter Celebrity : ")

print("Roses are " + colour)

print( plural_noun + " are blue")

print("I love " + celebrity)

# ## Working With Lists and Indexing ##

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

## #Popping a value out of a list:

Mylist = [1,2,3]

Last = Mylist.pop()

*#Result would be store in the "Last" variable with a value of 3.*

Mylist = [1,2,3]

First = Mylist.pop(0)

*#Result would be stored in the "First" variable as 1*

## #Check if a value is in a list.

'x' in [1,2,3]

*#Will return false as "x" is not in the 1,2,3 list.*

1 in [1,2,3]

*#Will return true as it has found 1 in the list*

Mylist = [1,2,3]

2 in Mylist

*#Result will return true using the related variable name too.*

## #Printing a value from a list in a specific position

mylist = ['a','b','c']

print(mylist[1])

#Result is "b" as lists start at 0.

## #Backwards Counting list.

mylist = ['a','b','c']

print(mylist[-1])

#Result is "c" as lists go backwards on negatives.

## #Changing a value in a specific list position

mylist = ['a','b','c']

mylist[0] = "New"

print(mylist)

['New', 'b', 'c']

## #adding two lists together

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.extend(lucky_numbers)

#printing friends list.

print(friends)

## #Appending a value

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

#adding to the end

friends.append("Jon")

print(friends)

#Result = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie","Jon"]

## #adding to position

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.insert(1,"Kelly")

print(friends)

Result = ["Kevin","Kelly","Karen","Jim","Oscar","Teddy","Charlie"]

## #removing elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.remove("Kevin")

print(friends)

#Result = "Karen","Jim","Oscar","Teddy","Charlie"

## #removing all elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.clear()

print(friends)

#expected result is [] (No values)

## #Finding if a value is in the list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

print(friends.index("Kevin"))

#Result = 0

## 

## #Count how many times the word defined occurs in list.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

print(friends.count("Jim"))

#Result = 2

## 

## #Sort List in ascending order.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends.sort()

print(friends)

## #Copying a list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends2 = friends.copy()

print(friends2)

#Expected Result = # ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

## #Append, Remove and Insert List

names = ["Ben","Dave","Tom","Dick"]

names.append("Harry")

print(names)

names.remove("Dick")

print(names)

names.insert(3,"Richard")

print(names)

## #Tuples

*# A tuple is a data structure/container where different values can be stored.*

*# A () is used to store a tuple*

*# A tuple can not be changed or modified.*

*#A tuple ()*

coordinates = (4,5)

print(coordinates[1])

## 

# ## Using Functions ##

#lambda function

*#Bunch of lines of code which can be called throughout the code*

#This is the function

def say_hi():

*#Anything in the indent = the function*

print("Hello User")

print("Top")

#This calls the function above.

say_hi()

print("Bottom")

*#Parameter is some information given to the function*

*#Name = the parameter, the data is passed along in the calling*

*#Recommended to be done to break up the code based on what its doing…*

def say_hi(name):

print("Hello! " + name)

say_hi("Ben")

## #Return Statement

*#Used to communicate back to user from a function*

*#Nothing can be printed after the return statement.*

*#Return statement breaks out the function.*

def cube(num):

*#expected a RETURN of 27.*

return num * num * num

print(cube(3))

# ## IF Statements

*#Allow programs to make decisions based on certain values/conditions*

is_male = True

is_tall = False

if is_male:

print("You are male")

else:

print("you are not male")

if is_tall:

print("You are tall")

else:

print("You are not tall")

## IF Statement with "OR"

*# Either of the statements need to be true.*

is_male = False

is_tall = True

if is_male or is_tall:

print("You are a male or tall or both")

else:

print("You are neither male or tall")

## IF Statement with "AND"

*#Both statements need to be true*

is_male = True

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

else:

print("Your are either not male or tall or both")

## IF Statement with "Else if" (elif)

*#Have more conditions*

is_male = False

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

elif is_male and not(is_tall):

print("You are a male, but not tall")

elif is_tall and not(is_male):

print("You are tall, but not male.")

else:

print("You are not a male and not tall")

## IF Statement inside a function

*#Using the def status as a function along with elif.*

def status(is_male,is_tall):

if is_male and is_tall:

return ("You are a male and tall ")

elif is_male and not (is_tall):

return ("Your are a male, but not tall")

elif is_tall and not (is_male):

return ("You are tall, but not male.")

else:

return ("You are not a male and not tall")

print(status(False,False))

## If Statement with Inputs

*#Define Variables*

*#Convert inptus to a float.*

num1 = float(input("Enter first number: "))

op = input("Enter operator: ")

num2 = float(input("Enter second number: "))

if op == "+":

print(num1 + num2)

elif op == "-":

print(num1 - num2)

elif op == "/":

print(num1/num2)

elif op == "*":

print(num1 * num2)

else:

print("Invalid operator")

# ## Dictionaries ##

*# Converting a Key into a value.*

*# Key : Values*

*# The keys need to be unique.*

*#Dictionaries do not retain any order.*

*#Dictionary Example*

*# Key : Values*

*# The keys need to be unique.*

*# Can be a number, or a string for the Key*

monthConversions = {

"Jan" : "January",

"Feb" : "February",

"Mar" : "March",

"Apr" : "April",

"May" : "May",

"Jun" : "June",

"Jul" : "July",

"Aug" : "August",

"Sep" : "September",

"Oct" : "October",

"Nov" : "November",

"Dec" : "December",

}

*#Doing it by Key*

print(monthConversions["Nov"])

*#Doing it by the get function*

*#Can use a default value.*

*#Default = "Not A Valid Key"*

print(monthConversions.get("Dec","Not A Valid Key"))

# ## Set##

{1,2,3}

*#all elements are unique, and unordered.*

# 

# ## While Loops ##

*# Allows us to loop through a block of code multiple times while the conditions are met.*

i = 1

while i <= 10:

print(i)

i += 1

print("Done With Loop")

# ## While Loop and If Statement ##

*#Variables*

secret_word = "giraffe"

guess = ""

guess_count = 0

guess_limit = 3

out_of_guesses = False

#While Loop with nested if.

while guess != secret_word and not(out_of_guesses):

if guess_count < guess_limit:

guess = input("Enter Guess: ")

guess_count += 1

print(guess_count)

else:

out_of_guesses = True

if out_of_guesses:

print("Out Of Guesses, You Lose")

else:

print("You Win!")

## Alternative Method:

name = "Ben"

guess = ""

number_tries = 3

tries = 0

while guess != name and tries < number_tries:

guess = input("name: ")

tries += 1

else:

if guess == name:

print("winner")

else:

print("Error")

# ## For Loops ##

*Looping around a set of values.*

## Prints the array in a list.

friends = ["Jim","Karen","John"]

for friend in friends:

print(friend)

## Prints each letter individual

for letter in "giraffe academy":

print(letter)

## Prints values 3 to 9 - Range

*#Stop is up to. Indexing starts at 0.*

for index in range(3,10):

print(index)

## another way to loop

friends = ["Jim","Karen","John"]

for index in range(len(friends)):

print(friends[index])

## 

## Manipulate the range.

for index in range(5):

if index == 0:

print("1st Iteration")

else:

print(index)

## 

## For loop print out list values

## 

seq = [1,2,3,4,5]

for item in seq:

print(item)

## List Comprehension:

*#Both produce the same result. #2 is slightly better performance, but not as readable!*

*#1:*

x = [1,2,3,4,5] #number list

out = [] #blank list

for num in x: #change x to name num

out.append(num**2) #to the power of

print(out)

*#2:*

*#List comprehension*

*#defined x as num in for loop*

x = [1,2,3,4,5] #number list

y = [num**2 for num in x]

print(y)

## Functions used with an if and a for:

def gender(is_male):

if is_male == "Boy":

friends = ["Jim","Tom","Harry"]

elif is_male == "Girl":

friends = ["Karen","Lucy"]

else:

friends = []

print("Incorrect Value")

for friend in friends:

print(friend)

print(len(friends))

# ## 2D List (Nested Lists) ##

*Number Grid, nested lists, using 2 criterias in the print, Row and Column*

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

# ## 2D For Loops (Nested For Loops)

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

*#Nested For Loop*

*#2D Array*

for row in number_grid:

for column in row:

print(column)

# ## For Loop and Nested If loop:

def translate(phrase):

translation = ""

for letter in phrase:

if letter in "AEIOUaeiou":

#Append the letter to the string

translation = translation + "g"

else:

#append the letter to the string

translation = translation + letter

return translation

print(translate(input("Enter Phrase: ")))

# ## Error Catching/Handling ##

*#Try Except, try the information given, if it fails (specific error), write a failure message*

*#All errors*

try:

number = int(input("Enter a number:"))

print(number)

except:

print('NO')

*#Specific error catch*

try:

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('NO')

## ## Multiple Error Catching

try:

#value = 10/0

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('Value Error')

except ZeroDivisionError:

print("Div by zero error")

# ## Reading from external files ##

*#Using the python read command*

*#Modes = r is read, w is write, a is append, r+ is read and write.*

## #Open the file and save as a variable:

employee_file = open("employees.txt","r")

## #check the file is readable

print(employee_file.readable())

## #Prints all the info

print(employee_file.read())

## #reads the first line.

print(employee_file.readline())

*#Moves down a line after the read line command.*

*#example this would read second line:*

print(employee_file.readline())

## #Read all the lines into an string list:

for each_employee in employee_file.readlines():

print(each_employee)

## #Read all lines into array:

print(employee_file.readlines())

## #Close the file at the end

employee_file.close()

# ##Writing and Appending To File ##

## 

## #Appending

*#Modes = r is read, w is write, a is append, r+ is read and write.*

employee_file = open("employees.txt","a")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

## #Write a new file (overwrite)

#Overwrites the file

#Modes = r is read, w is write, a is append, r+ is read and write.

employee_file = open("employees.txt","w")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

# ## Modules ##

## #Creating your own Modules

*#Importing a module into another python file*

*#Tools.py*

feet_in_mile = 5280

meters_in_kilometer = 1000

def hello_world(word):

return word

*#App.py*

import tools

print(tools.hello_world("Hello"))

print(tools.meters_in_kilometer)

## #Official Modules

[https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

## # How to use external modules

*# Available in the External Libraries > Lib Folder*

*# site-packages is the installed packages list.*

#Checking if pip is installed first!

pip --verison

*#example for python docx*

pip install python-docx

or can use the settings > python interpreter > click the "+" and Install package

# ##Classes & Objects

*#Classes and objects can be used to create own data types*

*#Class is used to define your own data types.*

## # Creating a Class (Modelling)

*#Class used to define something*

*#New File*

*#Student.py*

*#Created a class*

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

#Map out the attributes required..

*# Create the template.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## #Using the class to create an object

*#Is the item that has been defined using the class. What information is placed into the class*

*#Class used to define something*

*#New File*

*#Student.py*

## 

## #Created a class

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

*#Map out the attributes required..*

*# Create the template.*

*#The object values get passed (stored) to the init function.*

*#Defining the attributes that need to be assigned. Under the def __Init__ definition.*

*#Example the name of the student needs to be stored against the self.name container.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## # Created a Object using the class above.

*#1st student instance = File*

*#2nd Student instance = the class*

from student import Student

*#Using the class named "Student"*

student1 = Student("Jim","Business",3.1,False)

*#Print a specific part from the Student Data Type*

print(student1.name)

# ## Multiple Choice Quiz ##

## 

## #Using Classes, If Statements and Loops.

*#question.py*

class Question:

def __init__(self,prompt,answer):

self.prompt = prompt

self.answer = answer

*#app.py*

from Question import Question

*#Array of the questions which you want to prompt the user with*

question_prompts = [

"What colour are Apples\n(a) Red/Green\n (b) Purple\n(C) Orange\n \n",

"What colour are Bananas\n(a) Teal\n (b) Magenta\n(C) Yellow\n \n",

"What colour are Strawberries\n(a) Yellow\n (b) Red\n(C) Blue\n \n"

]

*#Array of questions, with the expected prompt and the answer.*

*#Link the question to the answer using the expected question_prompts class.*

questions = [

Question(question_prompts[0],"a"),

Question(question_prompts[1], "c"),

Question(question_prompts[2], "b"),

]

*#Create with a list of questions that want to be answered,and loop through questions*

def run_test(questions):

*#Reset score/set score to 0*

score = 0

#For each question in the array, what do we do..

for each_question in questions:

*#Assign the answer to the variable.*

answer = input(each_question.prompt).lower()

*#If the answer above is the same as the stored answer from the object above.*

if answer == each_question.answer:

score +=1

print("You got " + str(score)+"/" + str(len(questions))+" Correct")

*#run the definition*

run_test(questions)

# ## Second Class and Object Example

*#Question.py*

class Dog:

*#Given an attribute, Init = anything that is required for user to give.*

def __init__(self,name,age):

self.name = name

self.age = age

def get_name(self):

return self.name

def get_age(self):

return self.age

*#App.py*

from Question import Dog

d = Dog("Ben",27)

e = Dog("Dave",28)

print(str(d.get_name())+" - " + str(d.get_age()))

print(str(e.get_name())+" - " + str(e.get_age()))

# ## Giving each item a definition line - Classes and Objects

*#Question.py*

*#Give the class a name*

class Item:

#Given an attribute, Init = anything that is required for user to give.

def __init__(self,serial_no,item,price,in_stock):

self.serial_no = serial_no

self.item = item

self.price = price

self.in_stock = in_stock

*#Give each value required a definition line.*

def get_serial_no(self):

return self.serial_no,"Extra Return"

*#Use a comma if want to return more than one value*

def get_item(self):

return self.item

def get_price(self):

return self.price

def get_in_stock(self):

return self.in_stock

*#App.py*

*#Import the Class form external file*

from Question import Item

#def __init__(self,serial_no,item,price,in_stock):

*#Create an array to store multiple items.*

items =[

*#Give a value to the required Item attributes.*

Item("1234","Product A","3.50",False),

Item("5678","Product B","3.50",False)

]

*#Print out the serial number for each line of the above array.*

for each_line in items:

#Expected 5678

print(each_line.get_serial_no())

# # Inheritance of Classes

*#Inherit the classes from another class into a separate class*

*#Question.py*

class Chef:

def make_chicken(self):

print("The chef makes chicken")

def make_salad(self):

print("The chef makes a salad")

def make_special_dish(self):

print("The chef makes bbq ribs")

*# Inherit Chef*

*# Innehrit functions from another class by putting the inherited class in the ()*

class ChineseChef(Chef):

def make_fried_rice(self):

print("make fried rice")

def make_special_dish(self):

print("Make Orange Chicken")

*#App.py*

from Question import Chef

from Question import ChineseChef

myChef = Chef()

myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_special_dish()

myChineseChef.make_chicken()

# #Using Classes, Object and Writing to a file

*#Myclasses.py*

class Student:

def __init__(self,name,age,dob):

self.name = name

self.age = age

self.dob = dob

def get_info(self):

return self.name,self.age,self.dob

*#Main.py*

*#Import the class*

*from myClasses import Student*

*#Add the values to the required objects.*

#def __init__(self,name,age,dob):

students = [

Student("Bill",21,"27/05/1974"),

Student("Ben", 24, "28/05/1994")

]

*#Loop through the object class list.*

for each_student in students:

#Convert the Class list into a normal list.

all = list(each_student.get_info())

#print(all)

#Convert normal list to string values.

string = ','.join([str(item) for item in all])

#Open and write values to the file.]

f = open("students.txt", "a")

f.write(str(string)+"\n")

f.close()

## #Classes and Objects Examples

*#myClasses.py*

class Person:

def __init__(self, name, age):

self.name = name

self.age = age

class Vehicle:

def __init__(self, make, model, age):

self.make = make

self.model = model

self.age = age

# Instance method

def description(self):

return f"{self.make} {self.model}"

# Another instance method

def speak(self, sound):

return f"{self.make} says {sound}"

class PersonsDetails:

def __init__(self, name, age):

self.name = name

self.age = age

def myageis(self):

print("And My Age Is " + self.age)

def greetings(self):

print("Hello My Name Is " + self.name)

*#Main.py*

from myClasses import Person,Vehicle,PersonsDetails

print("Vehicle Example")

car1 = Vehicle("Honda", "Jazz", 4)

print(car1.description())

print(car1.make)

print(car1.speak("Beep"))

print("---------------")

print("Persons Details")

x = PersonsDetails("Ben", "28")

print(x.name)

print(x.age)

x.greetings()

x.myageis()

print("---------------")

print("Person")

p1 = Person("John", 36)

print(p1.name)

print(p1.age)

## #Example 2

*#myClasses.py*

class test:

def __init__(self):

pass

*#Main.py*

*#Create a class which will be a container of related object information*

*#Example, we create a class of "Car"*

class Car:

#We create a def and allocate under the init def the REQUIRED fields.

def __init__(self,registration):

self.registration = registration

#We create more behaviours as a def file.

def drive(self):

print("I can drive!")

*#Ford is an object, the 200 is allocating a value to the REQUIRED Registration value.*

*#Example every car requires a registration plate.*

ford = Car("AA12VHK")

honda = Car("BB17ABD")

audi = Car("CC20VDF")

*#We can define more attributes on the fly too.*

ford.speed = 200

honda.speed = 220

audi.speed = 250

*#Printing the values of the required object, and on-the-fly object.*

print(ford.registration)

print(ford.speed)

*#Using other defs and allocating them to the object.. No Print required just "call" the defined function*

ford.drive()

*#Trying a class with no definition and importing from another file.*

from myClasses import test

no_requirements = test()

test1 = no_requirements

test1.test = "Test"

print(test1.test)


# Python 🐍

Status: To read

Python

26 August 2021

09:30

# Recommended Tools:

[https://youtu.be/rfscVS0vtbw](https://youtu.be/rfscVS0vtbw)

https://www.youtube.com/watch?v=fWjsdhR3z3c&ab_channel=Indently

Python 3 (python.org)

Pycharm (community, jetbrains.com)

Install pip

Install selenium

# ## How to install Pip ##

*# Open a command prompt*

#check

pip --verison

# ## Setting Up Pycharm Project ##

Open Selenium >

File > New Project > Location

Make sure Virtual env Is selected and a location.

Tick Inherit global site-packages.

Click create.

Right click the folder at the left > File > New > Python file > Name (.py)

File should open.

Click Add Configuration > Click + > Python >

Select the file created in script path and make sure python interpreter is green.

Type in the script file print('Hello World') to test.

Click Run button.

# ## Basic Commands/Instructions ##

*The commands are printed in sequential order.*

*Print = send some information to show in the console.*

*\ is used as an escape character.*

*\n used to add a new line.*

## #Comment

# = Comment

## #Block Comment

'''

Comment goes here

'''

## #String

character_name = "Ben"

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

## #Converting number to a string:

*#String converting needs to be done when adding words to the number.*

my_num = 5

print(str(My_num))

## ## Using variables: ##

*#Define the variables at the top or before the variable is first used.*

Example:

character_name = "Ben"

character_age = "28"

print('his name is ' + character_name + '.')

print('he was ' + character_age + '.')

### #Update Variable

character_name = "Dave"

print('he liked the name ' + character_name + '.')

print('he did not like being ' + character_age + '.')

## ## Functions ##

def my_func():

print('hello')

myfunc()

### #Argument required function

#requires one argument to meet the name requirement.

def my_func(name):

print('hello ' + name)

my_func('Jose')

### #Using return function.

#Return is saved.

def square(x):

return x**2

result = square(2)

print(result)

### #Default Value function

#No Name is the default value.

def my_func(name='No Name'):

print('hello ' + name)

my_func() #Will use the default value as no name we defined when running the func.

### #upper, lower

phrase = "Giraffe Academy"

print(phrase.upper())

print(phrase.lower())

print(phrase.isupper())

print(phrase.islower())

### #multiple functions

print(phrase.upper().isupper())

### #length of string

print(len(phrase))

### #indexing used to grab part of the phrase:

# Starts at 0

print(phrase[6])

### #index function, find a specific value starting position.

print(phrase.index("G"))

*#Would expect "0"*

### #Replacing a character in a string

phrase = "Giraffe Academy"

print(phrase.replace("G","H"))

*#Expected Result = Hiraffe Academy*

*# Float = Decimal Number, Int = purely just whole number*

### #Adding Numbers together using int command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = int(num1) + int(num2)

### #Adding Numbers together using float command:

num1 = input("Enter a number:")

num2 = input("Enter another number:")

result = float(num1) + float(num2)

print(result)

### #Using .Format Sting Interpolation:

*#input variables into a string using the ".format and {}".*

print("First Name: {FirstName} Surname: {Surname}".format(FirstName="Ben",Surname="Britcliffe"))

### #Splitting by whitespace:

St = "Hello World"

St.split()

*#Converts to a list split at the whitespace.*

Result:

['Hello', 'World']

### Spit at a different character:

*#split a the # character.*

tw = "Hello #Sports"

tw.split('#')

['Hello ', 'Sports']

# ## User Input Commands ##

*#input is used to ask the user to enter some information*

input("Enter your name: ")

*#Store it in a variable*

name = input("Enter your name: ")

age = input("Enter your age: ")

print("Hello " + name + "! You are " + age)

colour = input("Enter Colour : ")

plural_noun = input("Enter Plural Noun : ")

celebrity = input("Enter Celebrity : ")

print("Roses are " + colour)

print( plural_noun + " are blue")

print("I love " + celebrity)

# ## Working With Lists and Indexing ##

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

## #Popping a value out of a list:

Mylist = [1,2,3]

Last = Mylist.pop()

*#Result would be store in the "Last" variable with a value of 3.*

Mylist = [1,2,3]

First = Mylist.pop(0)

*#Result would be stored in the "First" variable as 1*

## #Check if a value is in a list.

'x' in [1,2,3]

*#Will return false as "x" is not in the 1,2,3 list.*

1 in [1,2,3]

*#Will return true as it has found 1 in the list*

Mylist = [1,2,3]

2 in Mylist

*#Result will return true using the related variable name too.*

## #Printing a value from a list in a specific position

mylist = ['a','b','c']

print(mylist[1])

#Result is "b" as lists start at 0.

## #Backwards Counting list.

mylist = ['a','b','c']

print(mylist[-1])

#Result is "c" as lists go backwards on negatives.

## #Changing a value in a specific list position

mylist = ['a','b','c']

mylist[0] = "New"

print(mylist)

['New', 'b', 'c']

## #adding two lists together

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.extend(lucky_numbers)

#printing friends list.

print(friends)

## #Appending a value

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

#adding to the end

friends.append("Jon")

print(friends)

#Result = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie","Jon"]

## #adding to position

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.insert(1,"Kelly")

print(friends)

Result = ["Kevin","Kelly","Karen","Jim","Oscar","Teddy","Charlie"]

## #removing elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.remove("Kevin")

print(friends)

#Result = "Karen","Jim","Oscar","Teddy","Charlie"

## #removing all elements

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

friends.clear()

print(friends)

#expected result is [] (No values)

## #Finding if a value is in the list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Oscar","Teddy","Charlie"]

print(friends.index("Kevin"))

#Result = 0

## #Count how many times the word defined occurs in list.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

print(friends.count("Jim"))

#Result = 2

## #Sort List in ascending order.

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends.sort()

print(friends)

## #Copying a list

lucky_numbers = [4,8,15,16,23,42]

friends = ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

friends2 = friends.copy()

print(friends2)

#Expected Result = # ["Kevin","Karen","Jim","Jim","Oscar","Teddy","Charlie"]

## #Append, Remove and Insert List

names = ["Ben","Dave","Tom","Dick"]

names.append("Harry")

print(names)

names.remove("Dick")

print(names)

names.insert(3,"Richard")

print(names)

## #Tuples

*# A tuple is a data structure/container where different values can be stored.*

*# A () is used to store a tuple*

*# A tuple can not be changed or modified.*

*#A tuple ()*

coordinates = (4,5)

print(coordinates[1])

# ## Using Functions ##

#lambda function

*#Bunch of lines of code which can be called throughout the code*

#This is the function

def say_hi():

*#Anything in the indent = the function*

print("Hello User")

print("Top")

#This calls the function above.

say_hi()

print("Bottom")

*#Parameter is some information given to the function*

*#Name = the parameter, the data is passed along in the calling*

*#Recommended to be done to break up the code based on what its doing…*

def say_hi(name):

print("Hello! " + name)

say_hi("Ben")

## #Return Statement

*#Used to communicate back to user from a function*

*#Nothing can be printed after the return statement.*

*#Return statement breaks out the function.*

def cube(num):

*#expected a RETURN of 27.*

return num * num * num

print(cube(3))

# ## IF Statements

*#Allow programs to make decisions based on certain values/conditions*

is_male = True

is_tall = False

if is_male:

print("You are male")

else:

print("you are not male")

if is_tall:

print("You are tall")

else:

print("You are not tall")

## IF Statement with "OR"

*# Either of the statements need to be true.*

is_male = False

is_tall = True

if is_male or is_tall:

print("You are a male or tall or both")

else:

print("You are neither male or tall")

## IF Statement with "AND"

*#Both statements need to be true*

is_male = True

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

else:

print("Your are either not male or tall or both")

## IF Statement with "Else if" (elif)

*#Have more conditions*

is_male = False

is_tall = True

if is_male and is_tall:

print("You are a male and tall ")

elif is_male and not(is_tall):

print("You are a male, but not tall")

elif is_tall and not(is_male):

print("You are tall, but not male.")

else:

print("You are not a male and not tall")

## IF Statement inside a function

*#Using the def status as a function along with elif.*

def status(is_male,is_tall):

if is_male and is_tall:

return ("You are a male and tall ")

elif is_male and not (is_tall):

return ("Your are a male, but not tall")

elif is_tall and not (is_male):

return ("You are tall, but not male.")

else:

return ("You are not a male and not tall")

print(status(False,False))

## If Statement with Inputs

*#Define Variables*

*#Convert inptus to a float.*

num1 = float(input("Enter first number: "))

op = input("Enter operator: ")

num2 = float(input("Enter second number: "))

if op == "+":

print(num1 + num2)

elif op == "-":

print(num1 - num2)

elif op == "/":

print(num1/num2)

elif op == "*":

print(num1 * num2)

else:

print("Invalid operator")

# ## Dictionaries ##

*# Converting a Key into a value.*

*# Key : Values*

*# The keys need to be unique.*

*#Dictionaries do not retain any order.*

*#Dictionary Example*

*# Key : Values*

*# The keys need to be unique.*

*# Can be a number, or a string for the Key*

monthConversions = {

"Jan" : "January",

"Feb" : "February",

"Mar" : "March",

"Apr" : "April",

"May" : "May",

"Jun" : "June",

"Jul" : "July",

"Aug" : "August",

"Sep" : "September",

"Oct" : "October",

"Nov" : "November",

"Dec" : "December",

}

*#Doing it by Key*

print(monthConversions["Nov"])

*#Doing it by the get function*

*#Can use a default value.*

*#Default = "Not A Valid Key"*

print(monthConversions.get("Dec","Not A Valid Key"))

# ## Set##

{1,2,3}

*#all elements are unique, and unordered.*

# ## While Loops ##

*# Allows us to loop through a block of code multiple times while the conditions are met.*

i = 1

while i <= 10:

print(i)

i += 1

print("Done With Loop")

# ## While Loop and If Statement ##

*#Variables*

secret_word = "giraffe"

guess = ""

guess_count = 0

guess_limit = 3

out_of_guesses = False

#While Loop with nested if.

while guess != secret_word and not(out_of_guesses):

if guess_count < guess_limit:

guess = input("Enter Guess: ")

guess_count += 1

print(guess_count)

else:

out_of_guesses = True

if out_of_guesses:

print("Out Of Guesses, You Lose")

else:

print("You Win!")

## Alternative Method:

name = "Ben"

guess = ""

number_tries = 3

tries = 0

while guess != name and tries < number_tries:

guess = input("name: ")

tries += 1

else:

if guess == name:

print("winner")

else:

print("Error")

# ## For Loops ##

*Looping around a set of values.*

## Prints the array in a list.

friends = ["Jim","Karen","John"]

for friend in friends:

print(friend)

## Prints each letter individual

for letter in "giraffe academy":

print(letter)

## Prints values 3 to 9 - Range

*#Stop is up to. Indexing starts at 0.*

for index in range(3,10):

print(index)

## another way to loop

friends = ["Jim","Karen","John"]

for index in range(len(friends)):

print(friends[index])

## Manipulate the range.

for index in range(5):

if index == 0:

print("1st Iteration")

else:

print(index)

## For loop print out list values

## 

seq = [1,2,3,4,5]

for item in seq:

print(item)

## List Comprehension:

*#Both produce the same result. #2 is slightly better performance, but not as readable!*

*#1:*

x = [1,2,3,4,5] #number list

out = [] #blank list

for num in x: #change x to name num

out.append(num**2) #to the power of

print(out)

*#2:*

*#List comprehension*

*#defined x as num in for loop*

x = [1,2,3,4,5] #number list

y = [num**2 for num in x]

print(y)

## Functions used with an if and a for:

def gender(is_male):

if is_male == "Boy":

friends = ["Jim","Tom","Harry"]

elif is_male == "Girl":

friends = ["Karen","Lucy"]

else:

friends = []

print("Incorrect Value")

for friend in friends:

print(friend)

print(len(friends))

# ## 2D List (Nested Lists) ##

*Number Grid, nested lists, using 2 criterias in the print, Row and Column*

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

# ## 2D For Loops (Nested For Loops)

number_grid = [

[1,2,3],

[4,5,6],

[7,8,9],

[0]

]

*#Row and Column*

*#Result being 8.*

print(number_grid[2][1])

*#Nested For Loop*

*#2D Array*

for row in number_grid:

for column in row:

print(column)

# ## For Loop and Nested If loop:

def translate(phrase):

translation = ""

for letter in phrase:

if letter in "AEIOUaeiou":

#Append the letter to the string

translation = translation + "g"

else:

#append the letter to the string

translation = translation + letter

return translation

print(translate(input("Enter Phrase: ")))

# ## Error Catching/Handling ##

*#Try Except, try the information given, if it fails (specific error), write a failure message*

*#All errors*

try:

number = int(input("Enter a number:"))

print(number)

except:

print('NO')

*#Specific error catch*

try:

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('NO')

## ## Multiple Error Catching

try:

#value = 10/0

number = int(input("Enter a number:"))

print(number)

except ValueError:

print('Value Error')

except ZeroDivisionError:

print("Div by zero error")

# ## Reading from external files ##

*#Using the python read command*

*#Modes = r is read, w is write, a is append, r+ is read and write.*

## #Open the file and save as a variable:

employee_file = open("employees.txt","r")

## #check the file is readable

print(employee_file.readable())

## #Prints all the info

print(employee_file.read())

## #reads the first line.

print(employee_file.readline())

*#Moves down a line after the read line command.*

*#example this would read second line:*

print(employee_file.readline())

## #Read all the lines into an string list:

for each_employee in employee_file.readlines():

print(each_employee)

## #Read all lines into array:

print(employee_file.readlines())

## #Close the file at the end

employee_file.close()

# ##Writing and Appending To File ##

## #Appending

*#Modes = r is read, w is write, a is append, r+ is read and write.*

employee_file = open("employees.txt","a")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

## #Write a new file (overwrite)

#Overwrites the file

#Modes = r is read, w is write, a is append, r+ is read and write.

employee_file = open("employees.txt","w")

employee_file.write("\nToby - HR")

*#Close the file at the end*

employee_file.close()

# ## Modules ##

## #Creating your own Modules

*#Importing a module into another python file*

*#Tools.py*

feet_in_mile = 5280

meters_in_kilometer = 1000

def hello_world(word):

return word

*#App.py*

import tools

print(tools.hello_world("Hello"))

print(tools.meters_in_kilometer)

## #Official Modules

[https://docs.python.org/3/py-modindex.html](https://docs.python.org/3/py-modindex.html)

## # How to use external modules

*# Available in the External Libraries > Lib Folder*

*# site-packages is the installed packages list.*

#Checking if pip is installed first!

pip --verison

*#example for python docx*

pip install python-docx

or can use the settings > python interpreter > click the "+" and Install package

# ##Classes & Objects

*#Classes and objects can be used to create own data types*

*#Class is used to define your own data types.*

## # Creating a Class (Modelling)

*#Class used to define something*

*#New File*

*#Student.py*

*#Created a class*

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

#Map out the attributes required..

*# Create the template.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## #Using the class to create an object

*#Is the item that has been defined using the class. What information is placed into the class*

*#Class used to define something*

*#New File*

*#Student.py*

## #Created a class

class Student:

*#Anything indented is defined in the class*

*#Use attributes to map out the data types/data required.*

*#Map out the attributes required..*

*# Create the template.*

*#The object values get passed (stored) to the init function.*

*#Defining the attributes that need to be assigned. Under the def __Init__ definition.*

*#Example the name of the student needs to be stored against the self.name container.*

def __init__(self, name,course,grade,is_on_probation):

self.name = name

self.course = course

self.grade = grade

self.is_on_probation = is_on_probation

## # Created a Object using the class above.

*#1st student instance = File*

*#2nd Student instance = the class*

from student import Student

*#Using the class named "Student"*

student1 = Student("Jim","Business",3.1,False)

*#Print a specific part from the Student Data Type*

print(student1.name)

# ## Multiple Choice Quiz ##

## #Using Classes, If Statements and Loops.

*#question.py*

class Question:

def __init__(self,prompt,answer):

self.prompt = prompt

self.answer = answer

*#app.py*

from Question import Question

*#Array of the questions which you want to prompt the user with*

question_prompts = [

"What colour are Apples\n(a) Red/Green\n (b) Purple\n(C) Orange\n \n",

"What colour are Bananas\n(a) Teal\n (b) Magenta\n(C) Yellow\n \n",

"What colour are Strawberries\n(a) Yellow\n (b) Red\n(C) Blue\n \n"

]

*#Array of questions, with the expected prompt and the answer.*

*#Link the question to the answer using the expected question_prompts class.*

questions = [

Question(question_prompts[0],"a"),

Question(question_prompts[1], "c"),

Question(question_prompts[2], "b"),

]

*#Create with a list of questions that want to be answered,and loop through questions*

def run_test(questions):

*#Reset score/set score to 0*

score = 0

#For each question in the array, what do we do..

for each_question in questions:

*#Assign the answer to the variable.*

answer = input(each_question.prompt).lower()

*#If the answer above is the same as the stored answer from the object above.*

if answer == each_question.answer:

score +=1

print("You got " + str(score)+"/" + str(len(questions))+" Correct")

*#run the definition*

run_test(questions)

# ## Second Class and Object Example

*#Question.py*

class Dog:

*#Given an attribute, Init = anything that is required for user to give.*

def __init__(self,name,age):

self.name = name

self.age = age

def get_name(self):

return self.name

def get_age(self):

return self.age

*#App.py*

from Question import Dog

d = Dog("Ben",27)

e = Dog("Dave",28)

print(str(d.get_name())+" - " + str(d.get_age()))

print(str(e.get_name())+" - " + str(e.get_age()))

# ## Giving each item a definition line - Classes and Objects

*#Question.py*

*#Give the class a name*

class Item:

#Given an attribute, Init = anything that is required for user to give.

def __init__(self,serial_no,item,price,in_stock):

self.serial_no = serial_no

self.item = item

self.price = price

self.in_stock = in_stock

*#Give each value required a definition line.*

def get_serial_no(self):

return self.serial_no,"Extra Return"

*#Use a comma if want to return more than one value*

def get_item(self):

return self.item

def get_price(self):

return self.price

def get_in_stock(self):

return self.in_stock

*#App.py*

*#Import the Class form external file*

from Question import Item

#def __init__(self,serial_no,item,price,in_stock):

*#Create an array to store multiple items.*

items =[

*#Give a value to the required Item attributes.*

Item("1234","Product A","3.50",False),

Item("5678","Product B","3.50",False)

]

*#Print out the serial number for each line of the above array.*

for each_line in items:

#Expected 5678

print(each_line.get_serial_no())

# # Inheritance of Classes

*#Inherit the classes from another class into a separate class*

*#Question.py*

class Chef:

def make_chicken(self):

print("The chef makes chicken")

def make_salad(self):

print("The chef makes a salad")

def make_special_dish(self):

print("The chef makes bbq ribs")

*# Inherit Chef*

*# Innehrit functions from another class by putting the inherited class in the ()*

class ChineseChef(Chef):

def make_fried_rice(self):

print("make fried rice")

def make_special_dish(self):

print("Make Orange Chicken")

*#App.py*

from Question import Chef

from Question import ChineseChef

myChef = Chef()

myChef.make_special_dish()

myChineseChef = ChineseChef()

myChineseChef.make_special_dish()

myChineseChef.make_chicken()

# #Using Classes, Object and Writing to a file

*#Myclasses.py*

class Student:

def __init__(self,name,age,dob):

self.name = name

self.age = age

self.dob = dob

def get_info(self):

return self.name,self.age,self.dob

*#Main.py*

*#Import the class*

*from myClasses import Student*

*#Add the values to the required objects.*

#def __init__(self,name,age,dob):

students = [

Student("Bill",21,"27/05/1974"),

Student("Ben", 24, "28/05/1994")

]

*#Loop through the object class list.*

for each_student in students:

#Convert the Class list into a normal list.

all = list(each_student.get_info())

#print(all)

#Convert normal list to string values.

string = ','.join([str(item) for item in all])

#Open and write values to the file.]

f = open("students.txt", "a")

f.write(str(string)+"\n")

f.close()

## #Classes and Objects Examples

*#myClasses.py*

class Person:

def __init__(self, name, age):

self.name = name

self.age = age

class Vehicle:

def __init__(self, make, model, age):

self.make = make

self.model = model

self.age = age

# Instance method

def description(self):

return f"{self.make} {self.model}"

# Another instance method

def speak(self, sound):

return f"{self.make} says {sound}"

class PersonsDetails:

def __init__(self, name, age):

self.name = name

self.age = age

def myageis(self):

print("And My Age Is " + self.age)

def greetings(self):

print("Hello My Name Is " + self.name)

*#Main.py*

from myClasses import Person,Vehicle,PersonsDetails

print("Vehicle Example")

car1 = Vehicle("Honda", "Jazz", 4)

print(car1.description())

print(car1.make)

print(car1.speak("Beep"))

print("---------------")

print("Persons Details")

x = PersonsDetails("Ben", "28")

print(x.name)

print(x.age)

x.greetings()

x.myageis()

print("---------------")

print("Person")

p1 = Person("John", 36)

print(p1.name)

print(p1.age)

## #Example 2

*#myClasses.py*

class test:

def __init__(self):

pass

*#Main.py*

*#Create a class which will be a container of related object information*

*#Example, we create a class of "Car"*

class Car:

#We create a def and allocate under the init def the REQUIRED fields.

def __init__(self,registration):

self.registration = registration

#We create more behaviours as a def file.

def drive(self):

print("I can drive!")

*#Ford is an object, the 200 is allocating a value to the REQUIRED Registration value.*

*#Example every car requires a registration plate.*

ford = Car("AA12VHK")

honda = Car("BB17ABD")

audi = Car("CC20VDF")

*#We can define more attributes on the fly too.*

ford.speed = 200

honda.speed = 220

audi.speed = 250

*#Printing the values of the required object, and on-the-fly object.*

print(ford.registration)

print(ford.speed)

*#Using other defs and allocating them to the object.. No Print required just "call" the defined function*

ford.drive()

*#Trying a class with no definition and importing from another file.*

from myClasses import test

no_requirements = test()

test1 = no_requirements

test1.test = "Test"

print(test1.test)