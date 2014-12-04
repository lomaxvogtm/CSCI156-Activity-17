__author__ = 'Madeleine'


from ss import *

class Employee:
    def __init__(self, last=None, first=None, start=None, pay_rate=None, social=None):
        if (last is None) and (first is None) and (start is None) and (pay_rate is None) and (social is None):
            self.last = input('Last name: ').title()
            self.first = input('First name: ').title()
            self.start = input('Start: ').title()
            self.pay_rate= float(input("Pay rate: "))
            self.social = SS()
        else:
            self.first = first
            self.last = last
            self.start = start
            self.pay_rate = pay_rate
            self.social = social


    def __str__(self):
        return "Last name: " + self.last + "\n" + "First name: " + (self.first) +\
               "\n" + "Start: " + (self.start) + "\n" + "Pay rate: " + str(self.pay_rate)\
               + "\n" + "Social Security number: " + str(self.social)


employeeprint = Employee()
print(employeeprint)
