#variabel
site_name = 'Fandi Online'
print (site_name)

#change value
site_name = 'Alpha is online'
print (site_name)

#conversion
integer_number = 123
float_number = 54.232

new_number = integer_number * float_number

print("Value:", new_number)
print("Data type:", type(new_number))

#explisit
num_string = '12'
num_integer = 15

print ("Data type of num_string before type casting:", type(num_string))

#Explisit type conversion
num_string = int(num_string)

print ("Data type of num_string after type casting:", type(num_string))

num_sum = num_string + num_integer

print ("Sum of num_string and num_integer:", num_sum)
print ("Data type of num_sum:", type(num_sum))

#Input dan Output
nama = input("Masukkan nama Anda: ")
nim = input("Masukkan NIM Anda: ")

print("Nama Anda:", nama)
print("NIM Anda:", nim)

#print with parameter
print('Good Morning!', end= ' ')

print('It is rainy today')

#print with separator
print('New Year', 2023, 'See you soon!', sep= '. ')

#Aritmatic operators
x = 15
y = 4
print('x + y = ',x+y)
print('x - y = ',x-y)
print('x * y = ',x*y)
print('x / y = ',x/y)
print('x // y = ',x//y)
print('x ** y = ',x**y)

#Logical operators
x = True
y = False
print('x and y is',x and y)
print('x or y is',x or y)
print('not x is',not x)

#Bitwise operators
x = 10
y = 4
print('x & y = ',x&y)
print('x | y = ',x|y)
print('x ^ y = ',x^y)
print('~x = ',~x)
print('x << 1 = ',x<<1)
print('x >> 1 = ',x>>1)

#Assignment operators
x = 15
print('x =', x)
x += 5
print('x += 5 ->', x)
x -= 3
print('x -= 3 ->', x)
x *= 2
print('x *= 2 ->', x)
x /= 4
print('x /= 4 ->', x)

#identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

#membership operators
x = 'Hello world'
y = {1:'a',2:'b'}
print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)

#Boolean operators lebih dari dan kurang dari
x = int(input("Enter x: "))
y = int(input("Enter y: "))

result = (x < y)
print(f"x < y ---> {result}")
result = (x <= y)
print(f"x <= y ---> {result}")
result = (x < 10)
print(f"x < 10 ---> {result}")
result = (x <= 10)
print(f"x <= 10 ---> {result}")

result = (x > y)
print(f"x > y ---> {result}")
result = (x >= y)
print(f"x >= y ---> {result}")
result = (x > 10)
print(f"x > 10 ---> {result}")
result = (x >= 10)
print(f"x >= 10 ---> {result}")

#Boolean if else
age = int(input("Enter your age: "))

if age >= 18:
    print("Grant access to the website.")
else:
    print("Deny access.")
print("Program complete.")

#for loop
models = ["Fable", "ChatGPT", "Gemini"]

    # Access items of the list one by one
for model in models:
    print(model)
    print("---")

#while loop
number = float(input("Enter a number: "))

while number >= 0.0:
    print(number)


#break and continue
    #break statement
number = int(input("Enter a number: "))
for i in range(1, 6):

    if i == number:
        break
    print(i)
    #continue statement
for i in range(1, 11):

    if i % 2 == 0:
        continue
    print(i)

#Pass statement
is_valid = True

if is_valid:
    pass
else:
    print("Login invalid. Redirect to form.")

#Python numbers data type
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))

#Python List
cart = ["T-shirt", "Lamp", "Pen"]
print(cart)

    # A list of mixed data types
my_list = [1, "Python", 3.14]
print(my_list)

    # Empty list
my_list = []
print(my_list)

#Python Tuple
    # empty tuple
my_tuple = ()

    # tuple having integers
my_tuple = (1, 2, 3)

    # tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

    # nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

    # tuple can be created without parentheses
    # also called tuple packing
my_tuple = 3, 4.6, "dog"
    # tuple unpacking is also possible
a, b, c = my_tuple

#Python string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)
print(message, 'tipe datanya adalah', type(message))

#Python set
    # create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

    # create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

    # create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

#Python dictionary
    # creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

    # printing the dictionary
print(country_capitals)