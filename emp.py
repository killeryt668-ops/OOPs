class Emp:
    def read(self):
        self.name=input("enter employee name:")
        self.emp_no=int(input("enter employee number:"))
        self.basic=float(input("enter the basic salary of the employee:"))
        self.ta=float(input("enter your traval expences:"))
        self.pf=float(input("enter your pf:"))
    def salry(self):
        self.total=(self.basic*self.ta)-self.pf
    def dis(self):
        print("name:",self.name)
        print("employee number:",self.emp_no)
        print("basic salry:",self.basic)
        print("total salary:",self.total)
emp=Emp()
emp.read()
emp.salary()
emp.dis()