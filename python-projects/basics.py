import math

# variables
var = 10  # int
v2 = 10.1  # float
name = 'rishi'  # string
is_published = True  # boolean

# Exercise - John Smith, new, 20 year old patient
patient = "John Smith"
age = 20
new_patient = True

# Receiving user input
n = input('What is your name? ')
print('Hi ' + n)

# Type conversion
birth_year = input('Birth Year: ')
age = 2022 - int(birth_year)  # cast the str to int
print(age)
print(type(age))
# float()
# int()
# bool()

# Strings
course = "Python for Beginners"
mult = ''' Hi Rishi 
This is how to write a string on multiple lines'''
print(course[0])  # Index into the first character of the string
print(course[-1])  # Index into the last character of the string
print(course[0:3])  # Index into characters up to but not including end index
print(course[5:] + course[0:5])
copy = course[:]  # Copying a string

# Formatted strings
first = "Rishi"
last = "Vaidya"
msg = f'{first} [{last}] is a coder'

# String Methods
length = len(course)  # length of variable - general purpose
    # course. - will show all methods for strings
    # Method - functions that belong to objects
    # upper, lower, find, replace
    # in operator produces boolean response

# Arithmetic Operators
    # + - * / // % **
    # +=
x = -5.5
y = abs(x)
    # Import math module to write complex arithmetic functions
    # This makes math an object, so we can access using math.

# If Statements
price = 100000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
elif not has_good_credit:
    down_payment = 0.2 * price
else:
    print('Have a good day')

# Logical operators
    # and, not, or, in
# Comparison operators
    # <, >, ==, !=

# Exercise
name = "Rishi Vaidya"
if len(name) < 3:
    print('Name is too short')
elif len(name) > 50:
    print('Name is too long')
else:
    print('Name looks good')


# While Loops
i = 1
while i <= 5:
    print(i)
    i += 1


# For Loops
for item in 'Python':
    # Iterartes through string
    print(item)
for item in [1, 2, 3]:  # List is defined by []
    print(item)
    # range(10) creates an object of numbers from 0 - 9
    # range(lower, upper, step)

# Nested For Loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

# Lists
names = ['Rishi', 'Steve', 'Jeff', 'Mike']
# names[0] accesses Rishi
# names[2:] accesses Jeff and Mike

# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 ,9]
]
# matrix[0][2] accesses 3

# List Methods
L = [5, 2, 1, 7, 4]
# access using .method()
L.append(20)
L.insert(3, 20)
# 50 in L - in operator checks for existence in list
# .sort() .reverse() .index() .copy() .remove() .clear() .pop()

# Tuples - used to store list of items - cannot be modified (immutable)
T = (1, 2, 3)
x, y, z = T  # Unpacking Tuple









