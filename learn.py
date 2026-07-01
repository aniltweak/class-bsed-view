
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



#####
import copy

orginalData = [1,2,3]
copiedData = copy.copy(orginalData)

copiedData[0] = 99
print("orginalData", orginalData)
print("copiedData", copiedData)

# copyDeep = copy.deepcopy(orginalData)

# print(orginalData)
# print(copiedData)
# print("deepcopy", copyDeep)

#import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99  # Modify INNER element

print("Original:", original)  # [[99, 2], [3, 4]]
print("Shallow:", shallow)    # [[99, 2], [3, 4]]

######


class Test:
    
    def __init__(self, Clientname, age):
        self.Clientname = Clientname
        self.age = age
        print(Clientname, age)
        
    def get_name_age(self):
        print(self.Clientname, self.age)
        
    def update_details(self):
        print(self.Clientname, self.age)
        
testobj = Test("maha rana prathap", 32)
testobj.get_name_age()
testobj.update_details()

class AreaCircumference:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def cal_area(self):
        result = AreaCircumference.pi * self.radius**2         
        return result
    
    def circumference(self):
        result = 2 * AreaCircumference.pi * self.radius
        return result

objarecir = AreaCircumference(5)
print(objarecir.pi)
objarecir.cal_area()
print("02", objarecir.cal_area())
objarecir.circumference()
print("03", objarecir.cal_area())
        
## encapsulation  = hiding internal details accesing through methods
#Encapsulation is hiding an object’s data and allowing it to be accessed or
# changed only through controlled methods/properties (so the data stays safe and valid).
class ClassMarks:    
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
        
    def get_result(self, total):
        if total > self.__marks:
            print(f'{self.name} and {self.__marks} are less than total')
    
    def get_marks(self):
        print(self.__marks)
 
objclasmark = ClassMarks("solar", 99)
print(objclasmark.name)
#print(objclasmark.__marks)  # we will get error[not avialable] due to it is private only called in side class 
objclasmark.get_result(100)
objclasmark.get_marks()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = 0
        self.salary = salary  # uses the setter below

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value


e = Employee("Anil", 50000)
print(e.salary)     # OK (getter)
e.salary = 60000    # OK (setter with validation)
# e.salary = -10    # ValueError

#decorator in python is a function that given extra behaviour to another function
# decorator in Python is a function that adds extra behavior to another function (or method) 
# without changing its original code.
#It “wraps” the function and runs code before/after (or modifies) it.
def testdecorator(func):
    def checkingexecutionprocess():
        print("start initial")
        func()
        print("end of function")
    return checkingexecutionprocess

@testdecorator
def calldeco():
    print("checking this func when called")
    
objtestdeco = calldeco()
objtestdeco

def testdecoratoradd(func):
    def checkaddresult(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        print(func.__name__, "result is", result)
        return result
    return checkaddresult

@testdecoratoradd
def add(a,b):
    return a+b

add(4,5) # we are passing 2 arguments like wise in line  102 we should pass arguments other wise it will be error

class Animal:
    def anspeak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()
d.anspeak()


##########
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
#import data
reviews = pd.read_csv("reviews.csv") 
#print column names
print(reviews.columns) 
#print(reviews.dtype)
#print .info
print(reviews.info)
#look at the counts of recommended
print(reviews['recommended'].value_counts()) 
#create binary dictionary
binary_dict = {"True":1,"False":0} 
#transform column
reviews['recommended'] = reviews['recommended'].map(binary_dict)
#print your transformed column 
print(reviews['recommended'].value_counts()) 
#look at the counts of rating
print(reviews['rating'].value_counts()) 
#create dictionary
rating_dict = {"Loved it":5, "Liked it": 4, "Was okay" : 3, 
"Not great": 2, "Hated it": 1}
#transform rating column
reviews['rating'] = reviews['rating'].map(rating_dict) 
#print your transformed column values
print(reviews['rating'].value_counts()) 
#get the number of categories in a feature
print(reviews['department_name'].value_counts())  
#perform get_dummies
one_hot = pd.get_dummies(reviews['department_name']) 
#join the new columns back onto the original
reviews = reviews.join(one_hot)
#print column names
print(reviews.columns)
#transform review_date to date-time data
reviews['review_date'] = pd.to_datetime(reviews['review_date'])
#print review_date data type 
print(reviews['review_date'].dtype)
#get numerical columns
reviews = reviews[['clothing_id', 'age', 'recommended', 
                   'rating', 'Bottoms', 'Dresses', 
                   'Intimate', 'Jackets', 'Tops', 'Trend']].copy() 
#reset index
reviews = reviews.set_index(reviews['clothing_id'])
#instantiate standard scaler
scaler = StandardScaler()
#fit transform data
scaler.fit_transform(reviews) 

############################################

## encapsulation
class Animal:
    def __init__(self, bird, carnivorus, herbivorus):
        self.bird = bird
        self.__carnivorus = carnivorus
        self.__herbivorus = herbivorus
        
    def call_carnivorus(self):
        print(self.__carnivorus)
        
    def call_herbivorus(self):
        print(self.__herbivorus)
        
test = Animal("sparrow","lion","horse")
#print(test.__herbivorus) 
#AttributeError: 'Animal' object has no attribute '__herbivorus'. 
# Did you mean: 'call_herbivorus'?
# print(test.bird) #sparrow
# test.call_carnivorus() #lion
# test.call_herbivorus() #horse
##inheritance
class Vehical:
    def __init__(self, brand):
        self.brand = brand    
    def call_brand(self):
        print(self.brand)
        
class Car(Vehical):
    def __init__(self, model, price, brand):
        self.model = model
        self.price = price
        super().__init__(brand) # calling from parent class
        
    def info(self):
        print(self.model, "brand is ", self.brand, "price is", self.price)    
    def add_info(self, data):
        print("additional data on",self.model, data)

# test = Car("prototype",1000000,"bmw")
# test.info() #prototype brand is  bmw price is 1000000
# test.add_info("currently in testing phase level 3") #additional data on prototype currently in testing phase level 3

#polymorphism - same method name different behaviour
class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")

def make_sound(animal):
    animal.sound()

# make_sound(Dog()) #bark 
# #make sure with dog use () otherwise it wont work
# make_sound(Cat()) #meow

#abstraction : show only the important features (what to do) and hide the internal details (how it works).
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        raise NotImplementedError("cj=hild class must create send method")
    
class Email(Notification):
    def send(self, message):
        return f'my message is {message}'
    
# test = Email()
# print(test.send("hi how are you?")) #my message is hi how are you?
# print(test.send()) # no arg passed o/p is Email.send() missing 1 required positional argument: 'message'

#
"""
Method Overriding (runtime polymorphism)
Definition (simple):
- Parent class has a method.
- Child class defines the SAME method name (same purpose),
  and the child's method REPLACES (overrides) the parent version.
When you call the method using a child object, Python uses the child's method.
"""
class Bank:
    def interest(self):
        return "bank interest is 5%"     
class sbi(Bank):
    def interest(self):
        return "sbi bank interest rate is 4%"
class hdfc(Bank):
    def interest(self):
        return "hdfc bank interest rate is 6%"

# b1 = Bank() 
# b2= sbi()
# b3 = hdfc()
# print(b1.interest(), "sbi", b2.interest(), "hdfc", b3.interest())
# #bank interest is 5% sbi sbi bank interest rate is 4% hdfc hdfc bank interest rate is 6%

#method overloading : 
'unlike java/c python does not support method overloading'
'alternative is use default parameter with value'

class MathAdd:
    def add(self, a, b, c=0):
        return a+b+c
    
test = MathAdd()
print(test.add(1,2)) #3
print(test.add(1,2,3)) #6



s = "python"
rev = ""
for i in s:
    rev = i + rev
    print(rev)
print(rev)


a = "madam"
d = s[::-1]
print(a is d)
print(a==d)

f = [1,2,2,3,3,4,4,5,5,6,7,8]

d = []
z = []
s = {}
for i in f:
    if f.count(i)>1:
        pass
    else:
        d.append(i)
        
for i in f:
    if i not in z:
        z.append(i)
    
print(d)
print(z)

#fibnocci

a = 0
b = 1
n = 7
result = []
for _ in range (7):
    result.append(a)
    a, b = b, a+b
    
print(result)


# extract integers and count
stringData = "10abcd2efg8hijklbsb30"
total = 0
result = ""
for i in stringData:
    if i.isdigit():
        result += i
        print("result1",result)
    else:
        if result:
            total += int(result)
            result = ""
            print("result2",result)
            print("total1",total)
if result:
    total += int(result)
print("result3",result)
print("total2", total) # 50

# result1 1  # result1 10 # result2 # total1 10 # result1 2 # result2 # total1 12 
# # result1 8 # result2 # total1 20 # result1 3 # result1 30 # result3 30 # total2 50

import re
s = "10abcd2werf30dgxf8"
total = sum(map(int, re.findall(r"\d+", s)))

print(total) #50

import re

s = "10abcd2werf30dgxf8"
matches = re.findall(r"\d+", s)
nums = list(map(int, matches))
total = sum(nums)

print("matches:", matches) # matches: ['10', '2', '30', '8']
print("nums:", nums)  # nums: [10, 2, 30, 8]
print("total:", total) #total: 50


teststr = "abc def hij/klm"
rev = ""

for i in teststr:
    rev = i + rev
print("202 :",rev)



str1 = " a b c d e "
print("strip", str1.strip())  #strip a b c d e
print("split()",str1.split()) #split() ['a', 'b', 'c', 'd', 'e']
print("split(' ')",str1.split(" ")) # split(' ') ['', 'a', 'b', 'c', 'd', 'e', '']
#print("split('')",str1.split("")) #ValueError: empty separator

#strip() removes whitespace only from start/end
#split() without argument collapses consecutive whitespace
# split(" ") splits on single-space exactly, so it includes empty strings




