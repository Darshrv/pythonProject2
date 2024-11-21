#Grade calculator:
#Write a program that calculates and displays the letters grade
#for a given numerical score(eg.,A,B,C,D or F)
#based on the following scale

#A:90-100
#B:80-89
#C:70-79
#D:60-69
#E:0-59

#Logic Building Formula

#1-->User Inputs-->score or Marks-->int
#2--> o/p-->str--> A or B....
score=int(input("Enter your score\n"))

#score>=90 and score<=100-->"A"
#score>=80 and score<=89-->"B"

if score>=90 and score<=100:
    print("Your grade is","A")
elif score>=80 and score<=89:
    print("Your grade is","B")
elif score>=70 and score<=79:
    print("Your grade is","C")
elif score>=60 and score<=69:
    print("Your grade is","D")
elif score>=100:
    print("You are superman!!,You can't get a grade!! 0:)")
else:
    print("Your grade is","F")