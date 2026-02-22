#salary of employee
class Salary:
    def __init__(self,name,id,basic=2777):
        self.name=name
        self.id=id
        self.basic=basic
    def increse_salary(self):
        self.basic
        sal=float(input("Enter your basic salary:"))
        self.basic +=sal
        print("Increased salary=",self.basic)
    def display(self):
        print(self.name)
        print(self.id)
        print(self.basic)
salary=Salary('rafeeq',8389)
salary.increse_salary()
salary.display()
