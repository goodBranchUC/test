from calendar import week, weekday
from datetime import datetime


class Employee:

    raiseAmount = 1.04
    numOfEmployees = 0

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@' + 'comp.com'
        self.pay = pay

        Employee.numOfEmployees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raiseAmount)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmt = amount

    @classmethod
    def fromString(cls, empStr):
        first, last, pay = empStr.split('-')
        return cls(first, last, pay)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5: 
            return False
        elif day.weekday() == 6:
            return True

emp1 = Employee('George', 'Fanter', 50000)
emp2 = Employee('Glen', 'Sanl', 67890) 

#emp1.raiseAmount = 500
#emp1.applyRaise()
#print(emp1.pay) 

#print(Employee.numOfEmployees)

empStr1 = 'John-Doe-70000'
empStr2 = 'Ben-boe-90000'
empStr3 = 'ken-yue-80000'

newEmp1 = Employee.fromString(empStr1)
newEmp2 = Employee.fromString(empStr2)

print(newEmp1.email)
print(newEmp1.pay)
print(newEmp2.email)
print(newEmp2.pay)

myDate = datetime(2022, 9, 5)

print(Employee.isWorkday(myDate))