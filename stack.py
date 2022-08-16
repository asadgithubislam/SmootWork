class Employee:
    company = "Goggle"

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Asslamu Alikum,Sir")

harry = Employee()
harry.salary = 10000
harry.getSalary("Thanks!")
harry.greet()
