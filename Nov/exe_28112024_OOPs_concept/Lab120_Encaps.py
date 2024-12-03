#web Automation -Selenium
#page-You are going automate

class VWOLoginpage:
    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirm(self):
        if self.email=="darshiramesh96@gmail.com" and self.password=="pass123":
            print("Allowed, login success")
        else:
            print("Login Failed")
email=input("Enter the email\n")
password=input("Enter the password\n")

vwo_obj=VWOLoginpage(email,password)
vwo_obj.login_confirm()