#User Defined
#1. The can't return -->non return
#2.They can return something
#3.No Return type and with default argument
#4.They don't parameters/arguments
from Nov.ex_07112024_Keywords_identifiers_varriables.Lab014_Mtah_Functions import result


#1. The can't return-->non return
#No Return type and no parameter/Argument--NRNP

def greet():
    print("Hello")
greet()


#2.They can return something
def greet_by_name(name):
    print("Hello,",name)
greet_by_name("Darshan")

#3.No Return type and with default argument
def say_hello_default_arg(name="Darshan"):
    print("Hello,",name.upper())
say_hello_default_arg("Ramesh")
say_hello_default_arg()


def multiple_args(name1="A",name2="B"):
    print("Mul-->",name1,name2)

multiple_args()
multiple_args(name1="Pramod")
multiple_args(name1="Dutta",name2="Amit")
multiple_args(name2="Amit")


#4.Argument +return type

def sum_of_two(a,b):
    return a+b
result=sum_of_two(4,56)
print(result)


def sum_of_two_number_default(num1=100,num2=200):
    return num1+num2
result=sum_of_two_number_default(200,200)
print(result)