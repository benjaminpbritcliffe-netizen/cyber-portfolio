# Java Tutorial

Tags: Idea
Language: Java

## Basic Java Program Structure: Step-by-Step

## 1. Decide on Your Blueprint (Class)

- **Concept:**

    Create a class that acts as a blueprint for your objects.

- **Code Example:**

    ```java
    
    // This class acts as a blueprint for creating Person objects.
    public class Person {
        // Attributes and methods will be added in the following steps.
    }
    
    ```

---

## 2. Identify the Attributes

- **Concept:**

    Determine the key data you want each object to have.

    For example, attributes like `name` and `age` (keep them private for encapsulation).

- **Code Example:**

    ```java
    
    public class Person {
        // Private attributes: only accessible within this class.
        private String name;
        private int age;
    }
    
    ```

---

## 3. Set Up Your Constructor

- **Concept:**

    Write a constructor that initializes the attributes.

    Use the `this` keyword to differentiate between class variables and constructor parameters.

- **Code Example:**

    ```java
    
    public class Person {
        private String name;
        private int age;
    
        // Constructor that initializes the attributes
        public Person(String name, int age) {
            this.name = name; // 'this.name' refers to the class attribute
            this.age = age;
        }
    }
    
    ```

---

## 4. Create Accessor and Mutator Methods (Getters and Setters)

- **Concept:**

    Keep attributes private and provide public methods to access (get) and modify (set) them.

- **Code Example:**

    ```java
    
    public class Person {
        private String name;
        private int age;
    
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
    
        // Getter for name
        public String getName() {
            return name;
        }
    
        // Setter for name
        public void setName(String name) {
            this.name = name;
        }
    
        // Getter for age
        public int getAge() {
            return age;
        }
    
        // Setter for age
        public void setAge(int age) {
            this.age = age;
        }
    }
    
    ```

---

## 5. Add Additional Methods

- **Concept:**

    Include methods to perform actions on the object, such as printing its state.

- **Code Example:**

    ```java
    
    public class Person {
        private String name;
        private int age;
    
        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }
    
        // Method to print the Person's information.
        public void printInfo() {
            System.out.println("Name: " + name + ", Age: " + age);
        }
    }
    
    ```

---

## 6. Create a Collection (ArrayList) to Manage Your Objects

- **Concept:**

    In your main method, initialize an `ArrayList` to store multiple `Person` objects dynamically.

- **Code Example:**

    ```java
    
    import java.util.ArrayList;
    
    public class Main {
        public static void main(String[] args) {
            // Create an ArrayList to hold Person objects.
            ArrayList<Person> people = new ArrayList<>();
    
            // Next steps will involve adding objects to this list.
        }
    }
    
    ```

---

## 7. Instantiate Your Objects and Add Them to the ArrayList

- **Concept:**

    Create new instances of the `Person` class and add them to your collection.

- **Code Example:**

    ```java
    
    public class Main {
        public static void main(String[] args) {
            ArrayList<Person> people = new ArrayList<>();
    
            // Creating Person objects using the constructor.
            Person person1 = new Person("Alice", 30);
            Person person2 = new Person("Bob", 25);
    
            // Adding the Person objects to the ArrayList.
            people.add(person1);
            people.add(person2);
        }
    }
    
    ```

---

## 8. Access and Manipulate Your Objects

- **Concept:**

    Iterate over the ArrayList to access and use methods like `printInfo()` for each object.

- **Code Example:**

    ```java
    
    public class Main {
        public static void main(String[] args) {
            ArrayList<Person> people = new ArrayList<>();
    
            Person person1 = new Person("Alice", 30);
            Person person2 = new Person("Bob", 25);
            people.add(person1);
            people.add(person2);
    
            // Loop through the list and print each Person's information.
            for (Person p : people) {
                p.printInfo();
            }
        }
    }
    
    ```
