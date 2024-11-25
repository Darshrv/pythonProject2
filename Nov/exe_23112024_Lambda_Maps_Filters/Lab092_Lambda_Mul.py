#Write a program to calculate even or odd

def finf_even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
n=int(input("Enter the number: "))
check_even_odd=lambda num:"Even" if num %2 ==0 else "odd"
print(check_even_odd(n))
print(check_even_odd(n))