#mobile shop system
class Mobile:
    def __init__(self,brand,price,model):
        self.brand=brand
        self.price=price
        self.model=model
        print("total price of the phone",self.price)
    def descount(self,amount):
        self.price-=amount
        print("after dicount",self.price)
    def total(self):
        print("total amountt of the phone=",self.price)
a=Mobile('samsung',23000,'s24')
a.descount(2000)

a.total()
    



         

         
         


        