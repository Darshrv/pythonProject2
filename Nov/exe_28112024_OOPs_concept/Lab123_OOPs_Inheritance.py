#How to create a class


#Single inheritance---> 85% of the time you will use SI in API, Web automation


class Father:
    key="2BHK"

    def car(self):
        print("Father has a Car-->Alto")
        print(self.key)

class Son(Father):#Single Inheritance
    key2="3BHK"

    def SUV(self):
        print("MG HECTOR , BLack")
        print(self.key2)

Father_obj=Father()
Father_obj.car()

Son_obj=Son()
Son_obj.SUV()