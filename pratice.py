class employee:
    count = 0
    def __init__(self, name, des,sal):
        self.name  = name
        self.des  =  des
        self.sal  =  sal
        employee.count = employee.count +1


    def displayCount(self):
        print("The total number of employees: ",self.count)

    def displayEmp(self):
        print("Name : ",self.name)
        print("Designation:",self.des)
        print("Salary:",self.sal)


e1 = employee("kiran","Trainee",5)
e1.displayEmp()

