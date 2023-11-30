"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
class Employee:
    def __init__(self, name, commision, contract):
        self.name = name
        self.commision = commision
        self.contract = contract

    def get_pay(self):
        pass

    def __str__(self):
        return self.name
    
class Salary(Employee):
    def __init__(self, name, salary, commision, contract):
        super().__init__(name, commision, contract)
        self.salary = salary
        

    def get_pay(self):
        if self.commision == 0 and self.contract == 0:
            return self.salary
        else:
            return self.salary + (self.contract*self.commision)
    
    def __str__(self):
        total = self.salary + (self.commision * self.contract)
        if self.commision == 0 and self.contract == 0:
            return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.salary}"
        elif self.contract == 1:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commision of {self.commision}.  Their total pay is {total}" 
        else:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commision for {self.contract} contract(s) at {self.commision}/contract.  Their total pay is {total}"

class Contract(Employee):
    def __init__(self, name, rate, hours, commision, contract):
        super().__init__(name, commision, contract)
        self.rate = rate
        self.hours = hours

    def get_pay(self):
        if self.commision == 0 and self.contract == 0:
            return self.rate*self.hours
        else:
            return self.rate*self.hours + self.commision*self.contract
    
    def __str__(self):
        total = (self.rate*self.hours + self.commision*self.contract)
        if self.commision == 0 and self.contract == 0:
            return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour.  Their total pay is {total}"
        elif self.contract == 1:
            return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.commision}.  Their total pay is {total}"
        else:
            return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.contract} contract(s) at {self.commision}/contract.  Their total pay is {total}"
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary('Billie', 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Contract('Charlie', 25, 100, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Contract('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary('Robbie', 2000, 1500, 1)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Contract('Ariel', 30, 120, 600, 1)


test = str(robbie)
print(test)