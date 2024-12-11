from pyexpat.errors import messages  #Custome Exce
class lowbalanceExceptionCustom(Exception):
    def __init__(self):
        self.message=message
        super().__init__(message)

balance=100
withdraw=int((input("Enter the amount you want to withdraw"))
if withdraw>balance:
    raise LowBalanceExceptionCustom("Balance is low ")
else:
    print("Remain Bal",(balance-withdraw))
