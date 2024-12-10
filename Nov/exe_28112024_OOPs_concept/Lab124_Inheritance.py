class Parent:
    gold="2kg"

    def BHK2(self):
        print("2BHK")

class Child(Parent):
    diamond="Diamond"

    def BHK3(self):
        print("3BHK")

Child_obj=Child()
print(Child_obj.diamond)
print(Child_obj.gold)