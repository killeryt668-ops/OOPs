class Bank:
    def __init__(self,tol=0):
        self.tol=tol
        
    def detail_collect(self):
        
        self.name=input("enter your name:")
        self.salary=int(input("enter yoyr basic salary:"))
        self.year=int(input("enter your experience of emplooyment:"))
        self.req=int(input("enter yout loan amount:"))
        
    def show(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("year of experience:",self.year)
        
    
    def loan_approval(self):
        self.year
        self.salary
        self.req
        self.tol
        if self.salary>=15000 and self.year<1:
            self.rafeeq=self.salary*5
            print("name:",self.name)
            print("loan approved:")
            print("loan amount:",self.req)
            
            
        else:
            print("name:",self.name)
            print("salary:",self.salary)
            print("year",self.year)
            print("loan amount",self.req)
            print("you are not eligible for th loan!!!.")

    def input(self):
        print("----menu----")
        print("1.enter your details:")
        print("2.see the eligibility:")
        print("3.show details")
        print("4.Exit")
        choice=int(input("enter your choice:"))
        while(choice):
            if choice ==1:
                self.detail_collect()
                return self.input()
            elif choice==2:
                self.loan_approval()
                return self.input()
            elif choice==3:
                self.show()
                return self.input()
            elif choice==4:
                print("thenak you for collect loan amount:")
                return self.input() 
            else:
                print("invalid choice!!!!")
                
bank=Bank()

bank.input()
bank=delatil_collect()
bank.show()

bank.loan_approval()

            
            