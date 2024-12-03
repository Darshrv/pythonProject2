class Person:
    def __init__(self,name):
        self.name=name
    def walk(self):
        return self.name

amit=Person("amit")
pramod=Person("pramod")

print("Who is walking",amit.walk())
print("who is walking",pramod.walk())

