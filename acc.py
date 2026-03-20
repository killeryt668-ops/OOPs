from abc import ABC, abstractmethod

class Account(ABC):
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    
    def calculate_interest(self):
        interest = self.get_balance() * 0.04
        print("Savings Interest:", interest)
        return interest


class CurrentAccount(Account):
    
    def calculate_interest(self):
        interest = self.get_balance() * 0.02
        print("Current Account Interest:", interest)
        return interest


class LoanAccount(Account):
    
    def calculate_interest(self):
        interest = self.get_balance() * 0.10
        print("Loan Interest:", interest)
        return interest


print("----- Savings Account -----")
s1 = SavingsAccount("Rafeeq", 10000)
s1.deposit(2000)
s1.withdraw(1500)
print("Balance:", s1.get_balance())
s1.calculate_interest()

print("\n----- Current Account -----")
c1 = CurrentAccount("Ahmed", 20000)
c1.deposit(3000)
c1.withdraw(5000)
print("Balance:", c1.get_balance())
c1.calculate_interest()

print("\n----- Loan Account -----")
l1 = LoanAccount("Faisal", 50000)
print("Loan Amount:", l1.get_balance())
l1.calculate_interest()

