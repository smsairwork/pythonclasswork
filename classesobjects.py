class Car:

    name="Toyota"
    color="black"

    def speed(self):
        print("The max speed is 100 km/hr")


class Person:
    height=7
    skintone="light"

    def eat(self):
        print("Eating")

    def walk(self):
        print("Walking")



c=Car()
c.speed()


teacher=Person()
print(teacher.skintone)
teacher.walk()
