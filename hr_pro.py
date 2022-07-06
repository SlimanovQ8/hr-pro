from datetime import date


class Employee:
   #Employee class here
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age =  age
        self.salary = salary
        self.employment_year = employment_year
    def get_working_years(self):
        return  date.today().year - self.employment_year


    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years()}'



class Manager(Employee):
    #Manager class here
    def __init__(self, name , age, salary , employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
    def  get_working_years(self):
         return super(Manager, self).get_working_years()
    def get_bonus(self):
        return self.bonus_percentage * self.salary
    def __str__(self):
        return f'{super(Manager, self).__str__()}  Bonus: {self.get_bonus()}'

def main():
    # main code here
    EmployeeList = []
    emp1 = Employee("Sliman", 23, 1500, 2017)
    emp2 = Employee("Yousef", 28, 1700, 2016)
    emp3 = Employee("Ali", 24, 1500, 2018)
    ManagerList = []
    # m1 = Manager("Khalid",40, 2500, 2010, .3)
    # print(m1.__str__())
    # EmployeeList.append(emp1)
    # EmployeeList.append(emp2)
    # EmployeeList.append(emp3)
    # ManagerList.append(m1)
    # print(EmployeeList[0].get_working_years())

    choose = int(-1)
    print("Welcome to HR Pro 2022")
    while choose != 5:
        print("Options:")
        print("        1. Show Employees")
        print("        2. Show Managers")
        print("        3. Add An Employee")
        print("        4. Add A Manager")
        print("        5. Exit")
        choose = int(input("What would like to do? "))
        print("-----------------")
        if choose == 1:
            print("Employees \n")
            for i in range(len(EmployeeList)):
                print(EmployeeList[i].__str__())
            print("----------------- \n")
        elif choose == 2:
            print("Managers \n")
            for i in range(len(ManagerList)):
                print(ManagerList[i].__str__())
            print("----------------- \n")
        elif choose == 3:
            name = input("Name: ")
            age = int(input("Age: "))
            salary = int(input("Salary: "))
            EmpYear = int(input("Employment Year: "))
            emp = Employee(name, age, salary, EmpYear)
            EmployeeList.append(emp)
            print("Employee added successfully \n")
        elif choose == 4:
            name = input("Name: ")
            age = int(input("Age: "))
            salary = int(input("Salary: "))
            EmpYear = int(input("Employment Year: "))
            bonusPercentage = float(input("Bonus Percentage: "))
            Mngr = Manager(name, age, salary, EmpYear, bonusPercentage)
            ManagerList.append(Mngr)
            print("Manager added successfully \n")

if __name__ == '__main__':
    main()
