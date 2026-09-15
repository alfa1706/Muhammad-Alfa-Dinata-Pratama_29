#function call
from tkinter import Message
from tokenize import Name
from turtle import back


def greet():
    print("Hello, welcome to the program!")

greet()

print("This is a simple function call example.")

#function arguments
def greet(nama):
    print("Hello", nama)
    # pass argument
greet("ALFA")

#argument function
def add_numbers(a, b):
    tambah = a + b
    print("hasilnya:", tambah)

add_numbers(5, 3)

def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)
    
    # function call with two arguments
add_numbers(2, 3)

    #  function call with one argument
add_numbers(a = 2)

    # function call with no arguments
add_numbers()

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Cartman', first_name = 'Eric')

#Python variable scope
     #local variable
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
print(Message)

    #Global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

    #non-lokal variable
# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

#Python Global Keyword
c = 1 

def add():
    # use of global keyword
    global c
    # increment c by 2
    c = c + 2 
    print(c)
add()

#Python Recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))

#Python module
    # import standard math module 
import math

    # use math.pi to get value of pi
print("The value of pi is", math.pi)

    # import all names from the standard module math
from math import *

print("The value of pi is", pi)

#python main
def main():
    print("Hello World")

if __name__=="__main__":
    main()

#Python Directory and Files
import os

print(os.getcwd())
print(r'D:\Coding\Kuliah Semester 3')

# list all sub-directories
os.listdir()
['DLLs',
'Doc',
'include',
'Lib',
'libs',
'LICENSE.txt',
'NEWS.txt',
'python.exe',
'pythonw.exe',
'README.txt',
'Scripts',
'tcl',
'Tools']

os.listdir('D:\\')
['$RECYCLE.BIN',
'Movies',
'Music',
'Photos',
'Series',
'System Volume Information']

#Python read and write files
import csv
with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

#Python reading CSV files
#import csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Python writing CSV files
import csv
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

#Python exception
#divide_numbers = 7 / 0
# print(divide_numbers)

#Python exception handling
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

#Python Custom Exception
    # define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

    # you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

#Python class and object
    # define a class
class Bike:
    name = ""
    gear = 0

    # create object of class
bike1 = Bike()

    # access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

#Pyhon inheritance
class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

    # inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

    # create an object of the subclass
labrador = Dog()

    # access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

    #   call subclass method 
labrador.display()

#Python multiple inheritance
class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

    # create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()

#Python Polymorphism
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

#Python operator overloading
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def add_points(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = p1.add_points(p2)

print((p3.x, p3.y))

#Python list comprehension
numbers = [1, 2, 3, 4]

doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

#python lambda function
    # declare a lambda function
greet = lambda : print('Hello World')

    # call lambda function
greet()

#Python iterators
    # define a list
my_list = [4, 7, 0]

    # create an iterator from the list
iterator = iter(my_list)

    # get the first element of the iterator
print(next(iterator))  

    # get the second element of the iterator
print(next(iterator))  

    # get the third element of the iterator
print(next(iterator))  

#Python generator
def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

#Python namespaces and scope
# global_var is in the global namespace
global_var = 10

def outer_function():
    #  outer_var is in the local namespace 
    outer_var = 20

    def inner_function():
        #  inner_var is in the nested local namespace 
        inner_var = 30

        print(inner_var)

    print(outer_var)

    inner_function()

# print the value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()

#Python closures
def greet():
    # variable defined outside the inner function
    name = "John"
    
    # return a nested anonymous function
    return lambda: "Hi " + name

# call the outer function
message = greet()

# call the inner function
print(message())

#Python Decorators
def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()

#Python @property decorator
# Basic method of setting and getting attributes in Python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# Create a new object
human = Celsius()

# Set the temperature
human.temperature = 37

# Get the temperature attribute
print(human.temperature)

# Get the to_fahrenheit method
print(human.to_fahrenheit())

#Python RegEx
import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

#Python DateTime
import datetime

# get the current date and time
now = datetime.datetime.now()

print(now)

#Python strftime
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

#Python strptime
from datetime import datetime

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

#how to get current date and time in Python
from datetime import date

today = date.today()
print("Today's date:", today)

#Python get current time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#Python timestamo to datetime and vice versa
from datetime import datetime

    # timestamp is number of seconds since 1970-01-01 
timestamp = 1545730073

    # convert the timestamp to a datetime object in the local timezone
dt_object = datetime.fromtimestamp(timestamp)

    # print the datetime object and its type
print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

#python time module
import time

seconds = time.time()

print("Seconds since epoch =", seconds)	

#python sleep()
import time

time.sleep(2)
print("Wait until 2 seconds.")

#Python Precedence and Associativity of Operators in Python
    # Precedence of or & and
meal = "fruit"

money = 0

if meal == "fruit" or meal == "sandwich" and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")

    # Left-right associativity
print(5 * 2 // 3)

    # Shows left-right associativity
print(5 * (2 // 3))

#Python keyword and identifier
language = 'Python'
continues = 'Python'

#Python Asserts
#def avg(marks):
 #   assert len(marks) != 0
  #  return sum(marks)/len(marks)

#mark1 = []
#print("Average of mark1:",avg(mark1))

#python Json
import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)

print( person_dict)
print(person_dict['languages'])

#Python arg and kwargs
def adder(x,y,z):
    print("sum:",x+y+z)

adder(10,12,13)
