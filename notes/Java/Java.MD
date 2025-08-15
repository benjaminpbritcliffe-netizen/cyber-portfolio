# Java

Primitive data types specify the size and type of variable values. They are the building blocks of data manipulation and cannot be further divided into simpler data types.

- Boolean
- Character
- Integer
- Float

Non Primitive

Non-primitive data types or reference data types refer to instances or objects. They cannot store the value of a variable directly in memory. They store a memory address of the variable. Unlike primitive data types we define by Java, non-primitive data types are user-defined. Programmers create them and can be assigned with null. All non-primitive data types are of equal size.

- Array
- String
- Class
- Interface
- Enum

A Method

[W3Schools.com](https://www.w3schools.com/java/java_methods.asp)

A **method** is a block of code which only runs when it is called.

You can pass data, known as parameters, into a method.

Methods are used to perform certain actions, and they are also known as **functions**.

Why use methods? To reuse code: define the code once, and use it many times.

Keeping attributes private is a fundamental aspect of encapsulation in object-oriented programming (OOP). Here’s why it’s so important:

- **Data Protection:**
    
    When attributes are private, they can’t be directly accessed or modified from outside the class. This prevents unintended changes and protects the internal state of an object.
    
- **Controlled Access:**
    
    By using public getter and setter methods, you have full control over how the attributes are read or updated. This allows you to enforce rules or validation checks whenever the data is accessed or changed.
    
- **Modularity and Maintenance:**
    
    Hiding the internal implementation details means you can change them later without affecting other parts of your code. This separation between the internal state and the external interface makes your code more flexible and easier to maintain.
    
- **Encapsulation:**
    
    Encapsulation helps bundle the data (attributes) and methods (behaviors) into a single unit (class), ensuring that the object’s internal workings are hidden from the outside world. This leads to more robust, secure, and reliable code.
