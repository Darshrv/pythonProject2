#Write a program that prints numbers from 1 to 100
#However, for the multiples of 3, print "Fizz" instead of the number
#and for multiples of 5, print"Buzz". for numbers that are
#multiples of both 3 and 5, print "FizzBuzz".(for if)

for number in range(1,101):
    if number %3==0:
        print("Fizz")
    elif number %5==0:
        print("Buzz")
    elif number%3 and number%5:
        print("FizzBuzz")
    else:
        print(number)