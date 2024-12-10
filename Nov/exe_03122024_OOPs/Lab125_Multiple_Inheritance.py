#MUltiple Inheritance

class Father:
    def father_money(self):
        return 5

class Mother:
    def mother_money(self):
        return 2

class Son(Mother,Father):
    def print_info(self):
        print("Son")

s=Son()
print(s.father_money())
print(s.mother_money())