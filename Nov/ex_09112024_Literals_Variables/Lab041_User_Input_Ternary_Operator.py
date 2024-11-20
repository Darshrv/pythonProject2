#Program - if age >18-- allowed to vote
#else--> not allowed too

user_age=int(input("Enter your age\n"))

if user_age>18:
    print("Yes You can go to Goa and vote")
else:
    print("No You can't go to Goa and vote")

print("Yes You can go to Goa and Vte" if user_age>18 else "No You can't go to Goa and vote")