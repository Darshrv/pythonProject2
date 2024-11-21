#Logic building formula
#step 1
#user input i/p--data type-->int
#o/pstring--> user if he can go or not.


#step 2 . Rough logic
#age >21-->print can go
#age<21-->print can't go

#step 3. write the logic
age=input("Enter your age")
age=int(age)
if age>=21:
    print("Can go to the club")
else:
    print("Can't go with this age")


#Ste4.  Check for the edge cases
#We should consider edge cases such as:
#Negative ages or extremely high values--> program will break
#Non-numeric input --ABC
#Age which is valid.>130


#Step 5. optimize the code
#Handle all the edges