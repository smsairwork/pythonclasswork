
#parent class/super class/base
class Animal:
    color="white"

    def walk(self):
        print("walking")


#child class/sub class/derived class
class Dog(Animal):
    def sound(self):
        print("Barking")




class Cat(Dog):
    def mysound(self):
        print("Mewowing")


a=Animal()
a.walk()


d=Dog()
d.sound()

c=Cat()
c.walk()
