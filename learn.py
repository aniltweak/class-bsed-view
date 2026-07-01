
# 1. Classes and Objects
# Definition:

# A class is a blueprint for creating objects.
# An object (instance) is a specific realization of that class with its own data.
# Python
class Dog:
    def __init__(self, name):
        self.name = name  # instance attribute

    def bark(self):
        print(f"{self.name} says woof!")

# creating objects (instances)
d1 = Dog("Buddy")
d2 = Dog("Luna")

d1.bark()  # Buddy says woof!
d2.bark()  # Luna says woof!

# 2. Attributes and Methods
# Definition:

# Attributes: data associated with a class or instance (variables).
# Methods: functions defined inside a class, operating on that data.
Python
class Circle:
    pi = 3.14159  # class attribute

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):          # instance method
        return Circle.pi * (self.radius ** 2)

c = Circle(5)
print(c.radius)  # 5
print(c.area())  # 78.53975

# 3. __init__ and Constructors
# Definition:
# __init__ is the initializer (often called constructor) that runs automatically after an object is created, to initialize its state.

# Python
class Person:
    def __init__(self, name, age):
        # constructor initializes attributes
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name, p.age)  # Alice 30
# 4. Encapsulation
# Definition:
# Encapsulation means bundling data and methods that operate on that data inside a class and hiding internal details from outside code.
# Python doesn’t have true private fields, but uses naming conventions and name‑mangling.

# Single underscore _var → “internal use” (convention).
# Double underscore __var → name‑mangled (harder to access accidentally).
# Python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # "private" attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = BankAccount("Bob", 100)
acct.deposit(50)
print(acct.get_balance())   # 150
# print(acct.__balance)     # AttributeError (name-mangled)
# 5. Abstraction
# Definition:
# Abstraction means exposing only the necessary interface and hiding implementation details. In Python, we often use abstract base classes (abc module).

# Python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # subclasses must implement

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

# s = Shape()         # TypeError: Can't instantiate abstract class
r = Rectangle(3, 4)
print(r.area())       # 12
# 6. Inheritance
# Definition:
# Inheritance lets a class (child/subclass) reuse and extend the behavior of another class (parent/base).

# 6.1 Single Inheritance
# Python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

d = Dog()
d.speak()  # Woof
# 6.2 Multilevel Inheritance
# Python
class Animal:
    def move(self):
        print("I can move")

class Mammal(Animal):
    def feed_baby(self):
        print("Feeding baby milk")

class Dog(Mammal):
    def bark(self):
        print("Woof")

dog = Dog()
dog.move()       # from Animal
dog.feed_baby()  # from Mammal
dog.bark()       # own method
# 6.3 Multiple Inheritance
# Python
class WalkMixin:
    def walk(self):
        print("Walking")

class SwimMixin:
    def swim(self):
        print("Swimming")

class Duck(WalkMixin, SwimMixin):
    pass

d = Duck()
d.walk()
d.swim()
# 7. Method Overriding and super()
# Definition:

# Overriding: child class provides its own implementation of a method already defined in the parent.
# super() lets you call the parent implementation from the child.
# Python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()     # optional
        print("Woof!")

dog = Dog()
dog.speak()
# Animal sound
# Woof!
# 8. Polymorphism
# Definition:
# Polymorphism means using a common interface for objects of different types. The same method name behaves differently depending on the object.

# Python
class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_says(animal):
    # works for any object that has speak()
    print(animal.speak())

animal_says(Cat())  # Meow
animal_says(Dog())  # Woof
# Duck typing: “If it quacks like a duck…” – only behavior (methods) matters, not the class type.

# 9. Class Variables vs Instance Variables
# Definition:

# Class variable: shared by all instances of a class.
# Instance variable: unique to each object.
# Python
class Employee:
    company = "ACME Corp"  # class variable

    def __init__(self, name):
        self.name = name   # instance variable

e1 = Employee("Alice")
e2 = Employee("Bob")

print(e1.company, e2.company)  # ACME Corp ACME Corp
Employee.company = "New Corp"
print(e1.company, e2.company)  # New Corp New Corp
# 10. Class Methods & Static Methods
# 10.1 Class Method (@classmethod)
# Definition:
# Receives the class (cls) as first argument, not the instance. Used for alternative constructors or actions affecting the class as a whole.

# Python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def from_fullname(cls, fullname):
        first, last = fullname.split()
        return cls(first + " " + last)

    @classmethod
    def get_population(cls):
        return cls.population

p = Person.from_fullname("John Doe")
print(p.name)
print(Person.get_population())
# 10.2 Static Method (@staticmethod)
# Definition:
# A function inside the class that doesn’t need self or cls; logically grouped with the class.

# Python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  # 8
# 11. Special / Magic Methods
# Definition:
# “Dunder” methods (__name__) give Python objects special behaviors (operator overloading, string representation, etc.).

# Common ones:

# __str__(self) – user‑friendly string (print(obj)).
# __repr__(self) – unambiguous representation (for debugging).
# __len__(self) – used by len(obj).
# __eq__, __lt__, etc. – comparison operators.
# __add__, __sub__, etc. – arithmetic operators.
# Python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)           # Vector(1, 2)
print(v1 + v2)      # Vector(4, 6)
# 12. Properties (@property)
# Definition:
# @property allows you to access methods like attributes, enabling controlled access (getters/setters) while keeping a simple attribute syntax.

# Python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0
t.celsius = 30        # validates via setter
# 13. Composition (Has‑a Relationship)
# Definition:
# Composition builds complex objects by containing other objects (has‑a), instead of inheriting (is‑a). Often better than deep inheritance trees.

# Python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def drive(self):
        self.engine.start()
        print("Car is moving")

c = Car()
c.drive()
# Engine started
# Car is moving
