#Hierarchical Inheritance:

class Father:
    def BHK1(self):
        print("1BHK")
class Darshan(Father):
    def BHK2(self):
        print("2BHK")
class Amit(Father):
    def BHK3(self):
        print("3BHK")
class Lucky:
    def No_House(self):
        print("No House")

D=Darshan()
D.BHK1()
D.BHK2()

A=Amit()
A.BHK1()
A.BHK3()

L=Lucky()
L.No_House()