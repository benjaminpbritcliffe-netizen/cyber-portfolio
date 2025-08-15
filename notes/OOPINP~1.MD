# OOP In Python

Created: 22 April 2025 16:23
Is Completed: Yes

# 🐍 Object-Oriented Programming in Python

## 🧱 1. Classes

A class is a blueprint for creating objects (instances).

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound."
```

**Explanation:**

The `Animal` class defines a constructor (`__init__`) and a method `speak()` which can be shared by all animal types.

```python
class Animal:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

        if self.gender == 'Male':
            self.pronouns = 'He'
        else:
            self.pronouns = 'She'

    def speak(self):
        return f"{self.name} makes a sound."
    def find_age(self):
        return f" and {self.pronouns} is {self.age} years old"

My_animal = Animal('Bob',21,'Male')

print(My_animal.speak())

print(My_animal.find_age())
```

---

## 🧬 2. Inheritance

A class can inherit methods and attributes from another class.

```python
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
```

**Explanation:**

`Dog` and `Cat` inherit from `Animal`. They override the `speak()` method to provide specialized behavior.

---

## 🔄 3. Polymorphism

Different classes can be treated the same if they share the same interface (method names).

```python
def animal_sound(animal):
    print(animal.speak())
dog = Dog("Rex")
cat = Cat("Whiskers")
animal_sound(dog)     # Rex barks.animal_sound(cat)     # Whiskers meows.
```

**Explanation:**

The `animal_sound()` function works on any object that implements `speak()`. This is polymorphism—same interface, different behavior.

---

## 🔒 4. Encapsulation

Encapsulation hides the internal state and allows interaction through controlled methods.

```python
class Zoo:
    def __init__(self):
        self.__animals = []  # private attribute    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals.append(animal)
    def show_all_animals(self):
        for animal in self.__animals:
            print(animal.speak())
```

**Usage Example:**

```python
zoo = Zoo()
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.show_all_animals()
```

**Explanation:**

`__animals` is a private list. The Zoo class provides public methods to safely interact with it.