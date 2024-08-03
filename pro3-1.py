class Employee:
    def __init__(self, name, date_of_join, designation, salary):
        self.name = name
        self.date_of_join = date_of_join
        self.designation = designation
        self.salary = salary

    def display_details(self):

        print(f"Name: {self.name}")
        print(f"Date of Join: {self.date_of_join}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}")

emp1 = Employee("anil", "01-01-2022", "Software Engineer", 75000.0)

print("Employee Details:")
emp1.display_details()