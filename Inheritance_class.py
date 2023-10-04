class Employee:
    count = 0

    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        try:
            self.salary = float(salary)
        except ValueError:
            raise ValueError("Salary should be a numeric value")
        Employee.count += 1

    def display_count(self):
        print("The total number of employees:", Employee.count)

    def display_details(self):
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, designation, salary, team_size):
        super().__init__(name, designation, salary)
        try:
            self.team_size = int(team_size)
        except ValueError:
            raise ValueError("Team size should be an integer")

    def display_details(self):
        super().display_details()
        print("Team Size:", self.team_size)


class Developer(Employee):
    def __init__(self, name, designation, salary, programming_language):
        super().__init__(name, designation, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print("Programming Language:", self.programming_language)

while True:
    print("\nSelect an option:")
    print("1. Add Employee")
    print("2. Display Employee Details")
    print("3. Exit")
    option = input("Enter your choice: ")

    if option == "1":

        try:
            name = input("Enter employee name: ")
            designation = input("Enter designation: ")
            salary = input("Enter salary: ")

            role = input("Enter role (Manager/Developer): ")
            if role.lower() == "manager":
                team_size = input("Enter team size: ")
                employee = Manager(name, designation, salary, team_size)
            elif role.lower() == "developer":
                programming_language = input("Enter programming language: ")
                employee = Developer(name, designation, salary, programming_language)
            else:
                raise ValueError("Invalid role. Use 'Manager' or 'Developer'.")


            employee.display_count()

        except ValueError as e:
            print("Error:", e)

    elif option == "2":
        employee.display_details()

    elif option == "3":
        break
    else:
        print("Invalid option. Please try again.")
