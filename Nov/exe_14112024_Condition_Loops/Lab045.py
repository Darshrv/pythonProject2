#1. User inputs-->two integers
#2. o/p--> int 1 Which ever is greater max number it will return
#31.4 or 45.34--float

num1= float(input("Enter the num1\n"))
num2=float(input("Enter the num2\n"))

if num1>=num2:
    print("Max is",num1)
else:
    print("Max is",num2)

#Edge cases --num1 ==num2--> Handled.
#String--> ABC, ten -->try and except
#-ve value --> we will learn this in future