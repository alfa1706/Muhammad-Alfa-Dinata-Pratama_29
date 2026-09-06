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

