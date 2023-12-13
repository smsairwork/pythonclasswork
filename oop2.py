class person:
    def __init__(self,name, gender,age):
        self.name=name
        self.gender=gender
        self.age=age

    def show(self):
        print("My name is",self.name, "i am a ", self.gender, "who is ", self.age)


p=person("Glory","female", 56)
p.show()

t=person("teacher", "male",78)
t.show()

print(p.name)
print(t.name)


