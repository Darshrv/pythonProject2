#Match statement--> #Switch in java
#match the op and execute
#python>3.10

#match variable:
#       case pattern1:
#          #code block
#case pattern2:
#          #code block


#Write a program to ask the user which browser he want to run automation

browser_name=input("Enter the browser Name\n")
match browser_name:
    case"firefox":
        print("Starting Firefox!!!")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the EDge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found!")




