class Stud:
    def __init__(self,name,roll,mark):
        self.name=name
        self.roll=roll
        self.mark=mark
    def display(self):
        self.name
        self.mark
        self.roll
        print("Name",self.name)
        print("roll no.",self.roll)
        print("Mark",self.mark)
    def avg_mark(self):
        self.mark
        avg=sum(self.mark)/len(self.mark)
        print(avg)
    def input(self):
        
        print("---Menu----")
        print("1.display")
        print("2.avg")
        print("3.exit")
        c=int(input("enter th ecchoice:"))
        while(c):
            if c==1:
                self.display()
            elif c==2:
                self.avg_mark()
            elif c ==3:
                print("byy")
                return self.input()
            else:
                print("invalid choice")
                
stud=Stud('rafeq',23,73)
stud.input()
stud.display()
stud.avg_mark()
