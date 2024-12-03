class Person:
#Attribute --What you have?
    id=None
    name=None
    age=None
    height=None
    email=None
    gender=None
    phone_no=None
    address=None

#Behaviour-- What you can do?
    def sleep(self,name):
        print("I am a method!!")
        print("Sleep",name)
    def sleep2(self,name):
        print("I am a method!!")
        return None
    def walk(self):
        print("I am walking")
    def walk_return(self):
        return "I am walking"

#create an object of the class
#objectref=Classname()--> Object
geeta=person()
geeta.name"Geeta Sharma"
geeta.gender="Female"

