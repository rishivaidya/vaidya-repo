
# variables
var = 10 #int
v2 = 10.1 #float
name = 'rishi' #string
is_published = True #boolean

# Exercise - John Smith, new, 20 year old patient
patient = "John Smith"
age = 20
new_patient = True

# Receiving user input
n = input('What is your name? ')
print('Hi ' + n)

# Type conversion
birth_year = input('Birth Year: ')
age = 2022 - int(birth_year) #cast the str to int
print(age)
print(type(age))
# float()
# int()
# bool()

# Strings
course = "Python for Beginners"
mult = ''' Hi Rishi 
This is how to write a string on multiple lines'''
print(course[0]) #Index into the first character of the string
print(course[-1]) #Index into the last character of the string
print(course[0:3]) #Index into characters up to but not including end index
print(course[5:] + course[0:5])
copy = course[:] #Copying a string

# Formatted strings
first = "Rishi"
last = "Vaidya"
msg  = f'{first} [{last}] is a coder'

