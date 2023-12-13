# Demonstrate polymorphism among class Shape, class Rectangle, class Circle. Fuction name is draw()

class roobot:
    def mining(self):
        print("assemblying")


    def train(self):
        print("fly")


    def aeroplane(self):
        print("transport")



c=roobot()
c.mining()
c.train()
c.aeroplane()




class shape:
    def draw(self):
        print("Drawing a shape")




class triangle:
        def draw(self):
            print("drawing a triangle")

class circle:
    def draw(self):
        print("size of the circle ")




s=shape()
s.draw()

t=triangle()
t.draw()

c=circle()
c.draw()


class Person:
    def __init__(self,name, age ):
        self.name=name
        self.age=age

    def details(self):
        print("My name is ", self.name, ".I am ", self.age, "years old")

class Teacher(Person):
    def details(self):
        print("My name is ", self.name, ".I am ", self.age, "years old")

class Accoutant(Teacher):

    def details(self):
        print("My name is ", self.name, ".I am ", self.age, "years old")

p=Person("Glory", 67)
p.details()

teach=Teacher("eMobilis", 13)
teach.details()

a=Accoutant("Peter", 78)
a.details()
