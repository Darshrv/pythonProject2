import os

print(os.getcwd())


files=os.listdir('/Users/darshrv/PycharmProjects/CoffeeMachine/pythonProject')
print(f"Files in current directory:{files}")

os.mkdir("Test2")

file_exist=os.path.exists("Testdata.txt")
print(file_exist)