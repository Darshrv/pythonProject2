


class Parent:
    def home(self):
        print("2BHK")

class Son(Parent):
    def home(self):
        print("3BHK")

obj_Ref=Son()
obj_Ref.home()