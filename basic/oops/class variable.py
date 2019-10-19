class Emp:
    num_of_emp=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first#instances represnted with self
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@comapny.com'
        Emp.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.email)

    def apply_pay(self):
        self.pay=int(self.pay * Emp.raise_amount)#self.pay*1.04 or global variable raise_amount we can use

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls,e_str):
        first, last, pay = e_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday==5 or  day.weekday==6:
            return False
        return True



#instances
# obj=Emp('rama','devi',5000)
# # print(obj.first,obj.last,obj.email,obj.pay)
# print(obj.pay)
# obj.apply_pay()
# print(obj.pay)
# print(obj.num_of_emp)
# print(obj.set_raise_amt(1.05))

#string class methods
# emp_str1='rama-devi-30000'
# emp_str2='sai-rama-50000'
# first,last,pay=emp_str1.split('-')
# emp=Emp.from_str(emp_str2)#Emp(first,last,pay)
# print(emp.first)
# print(emp.last)
#
# static methods
import datetime
my=datetime.datetime.now()
print(Emp.is_workday(my))