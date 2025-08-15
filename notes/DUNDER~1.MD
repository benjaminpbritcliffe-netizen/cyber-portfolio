# Dunder Method

Created: 4 April 2025 08:40
Class: 4
Is Completed: Yes

https://www.youtube.com/watch?v=NwjSP1_WEfE

Double Underscore Methods

Tip: When you hear Dunder think “Under The Hood”

automatically code by using pythons built in operations.

allow developers to define or customise the behaviour of objects

```python
class Car:
    def __init__(self,make,model,mileage,year,MOTFailure):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.year = year
        self.MOTFailure = MOTFailure

    def GetMake(self):
        print(self.make)

    def GetModel(self):
        print(self.model)

    def MileageStatus(self):
        if self.mileage > 30000:
            
            if self.MOTFailure == True:
                print('Car is old and has had an MOT Failure')
            else:
                print("Car is old, but hasn't had an MOT Failure")
                print('But the Car is Old')
        else:
            print('Car is new')
            if self.MOTFailure == True:
                print('MOT Failure')
            else:
                print('No MOT Failure')

Car1 = Car('Honda','Jazz',29000,'2006',False)

Car1.GetMake()

Car1.GetModel()

Car1.MileageStatus()

```

```python
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def GetName(self):
        return('My name is ' + self.name)

    def GetAge(self):
        return('My age is ' + str(self.age))

Person1 = Person('Ben',23)

print(Person1.GetName())

print(Person1.GetAge())

```