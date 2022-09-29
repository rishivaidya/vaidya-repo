
# Defining an example class
# Class - to help define new types to model real concepts
# Contain methods that belong to that type
# Object - instance of a class
# can have attributes object.attribute

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print('move')


    def draw(self):
        print('draw')


class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def talk(self):
        print(f'Hi, I am {self.name}')

class Jeff(Person):
    # Inheritance
    # Inherits talk method from Person

    def jeff_specific_method(self):
        print('Jeff doing Jeff things')
        pass


point1 = Point(10, 20)
point1.y = 30
point1.draw()

person1 = Person('Rishi', 22)
person1.talk()
