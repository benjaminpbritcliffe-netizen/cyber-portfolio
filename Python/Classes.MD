# Classes

What is a class? My favorite analogy is a cookie cutter.

Think of Python's built-in data types (integers, strings) as pre-made cookie cutters. When you create a class, you're making your own custom data type.

For our example, we'll create a class called Cookie.

When you create a new cookie, you'll want Python to do specific things. This is done with a constructor, which has a particular syntax: it starts with "def" followed by double underscores, "init" (short for initialize), and more double underscores.

One key difference between a method and a function is the "self" keyword. When a method has "self" as a parameter, it indicates that the method belongs to a class.

Let's explore this "self" keyword more through our example.

In this case, we have a parameter called "color".

When you pass a color like "green," the "self.color" applies to the specific instance being created.

To create a new cookie, we write: cookie_one = Cookie(color="green").

Here, cookie_one is the variable name. Just like assigning an integer or string to a variable, we're assigning a Cookie object and passing it the color green.

This information goes to the constructor, which creates a green cookie.

Now we can better understand the "self" keyword.

This specific instance of Cookie, cookie_one, is green.

This concept becomes clearer when we create another cookie.

Let's create cookie_two and make it blue.

cookie_two is a different variable representing a different cookie. When we pass it the color blue, that instance becomes blue.

That's how our constructor creates new cookies.

Beyond the constructor, we can create other methods to interact with these cookies.

Let's make a get_color method.

It uses the "self" keyword, and since it has no other parameters, it takes no arguments. It simply returns the color of the specific cookie you're checking.

We'll also create a set_color method.

This method takes a color parameter and changes the color of that particular cookie.

Let's run this code in VS Code to see it in action.

We'll create our two cookies.

Here's our Cookie class and the print statements to verify the colors of cookie_one and cookie_two.

When we run this, the output shows: Cookie one is green, cookie two is blue.

Now let's try set_color.

We'll use cookie_one.set_color and add print statements to verify the color change.

Running this shows that cookie_one is now yellow while cookie_two remains blue.

Let's switch back—cookie_one is now yellow.

How will we apply this in the course? We'll use classes for all our data structures.

Let's look at how we'd use this for a linked list.

We'd create a class called LinkedList (notice the capital letters), with its own constructor.

I'll show you the header line here. While I won't write all the method code now, we'll create methods to append items, pop items from the end, prepend items to the beginning, insert items, and remove items.

We'll implement all these LinkedList methods and more throughout the course.

That's how we'll use classes.

Based on the context, I'll write a complete example of the Cookie class that was discussed:

```python
class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

# Example usage
cookie_one = Cookie(color="green")
cookie_two = Cookie(color="blue")

print(f"Cookie one is {cookie_one.get_color()}")
print(f"Cookie two is {cookie_two.get_color()}")

# Change cookie_one's color
cookie_one.set_color("yellow")
print(f"Cookie one is now {cookie_one.get_color()}")
print(f"Cookie two is still {cookie_two.get_color()}")

```

This code implements the Cookie class example with a constructor that takes a color parameter, a get_color method to retrieve the color, and a set_color method to change the color. The example usage shows how to create instances and modify their colors.
