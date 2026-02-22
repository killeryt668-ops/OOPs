class Bank:
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self):
        #self.amount=amount
        am=int(input("Enter amount to deposit:"))
        self.balance +=am
        print("Balance:",self.balance)
    def withd(self):
       #self.amount=amount
        an=int(input("Enter amonut to withdraw:"))
        self.balance -= an
        print("balance:",self.balance)

name=input("enter your name:")
accno=int(input("Enter your account number:"))
balance=500
bank=Bank(name,accno,balance)
bank.deposit()
bank.withd()

