class ProductivitySystem:
    def track(self, employees, hours):
        print()
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")

class ManagerRole():
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")

class SecretaryRole():
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")

class FactoryRole():
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours.")

class SalesRole():
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone.")