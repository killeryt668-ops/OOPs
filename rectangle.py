class Rectangle():
    def __init__(self,wid,bre):
        self.wid=wid
        self.bre=bre
    def calculate_area(self):
        a=self.wid*self.bre
        print("area of rectangle=",a)
    def update_dimensions(self,new_wid,new_bre):
        self.wid=new_wid
        self.bre=new_bre
b=Rectangle(10,6)
print("old:")
b.calculate_area()
b.update_dimensions(12,7)
print("new:")
b.calculate_area()


