#Write a Python program to calulate the
#area of the circle given its radius using the formula
#.....area=pi*r^2.....(Take pi as 3.14)


#Logic Building Formula

#Step 1 Figure out the inputs and output
#input-->r--> data type--> float
#pi=3.14
#power--> pow or **--> any
#o/p--> float- area, print area

#// Step 2 //
#rough logic= area=3.14*pow(r,2)

#//Step 3//
import math
radius=float(input("Enter the radius of the circle\n"))
area=3.14*(radius**2)

print(radius)
print("Area of the circle is -->",area)
print(f"Area of the circle is ((Area)): {area:.3f}")


#*--> mul
#**--> power
print(math.pi)
print(math.pow(radius,2))

