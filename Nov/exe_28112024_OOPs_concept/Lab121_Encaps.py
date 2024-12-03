class Bank:
    def __init__(self,account_number,balance):
        self.balance=balance #Public
        self.__account_number=account_number#Private
    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount

    def show_me_account_number(self):
        print(self.__account_number)

HDFC = Bank(8847,120000)
HDFC.deposit(1000)
HDFC.check_balance()

HDFC.show_me_account_number()