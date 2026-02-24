class Obj:
    def __init__(self,price=45,count=100):
        self.price=price
        self.count=count
    def ticket(self):
        self.count
        self.price
        t=int(input("enter ticket count:"))
        self.count-=t
        self.price*=t
        print("total bill=",self.price)
        print("ticket bookig successfull:",self.price)
    def cancleticket(self):
        self.count
        p=int(input("enter count to cancle ticket:"))

        self.count+=p
        print("available ticket :",self.count)
        print("canciation success.refund soon!!")

    def input(self):

        
        print("-----Menu-----")
        print("1.book tichet")
        print("2.Cancle ticket")
        print("3.Exit")
        c=int(input("enter your choice:"))
        while(c):
            if c==1:
                self.ticket()
                return self.input()
            elif c==2:
                self.cancleticket()
                return self.input()
            elif c==3:
                print("Thank you fo booking our ticket&**")
                return self.input()
            else:
                print("Inavlid choice!!!.try again.")
                return self.input()+
obj=Obj()
obj.input()
obj.ticke()
obj.cancleticket()

    
