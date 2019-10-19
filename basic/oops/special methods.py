class Emp1:
    def __init__(self, first, last, pay):
        self.first = first  # instances represnted with self
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

    def __repr__(self):
        return "Emp1('{}','{})".format(self.first,self.last)

    def __str__(self):
        return '{}-{}'.format(self.first,self.last)

    def __add__(self, other):
        return self.pay + other.pay
    def __sub__(self, other):
        return self.pay - other.pay

    def  __len__(self):
        return len(self.first)

emp=Emp1('rama','devi',50000)
emp1=Emp1('sai','a',60000)

print(emp.email)
print(emp)
print(repr(emp))
print(str(emp))
print(emp.__repr__())
print(emp.__str__())
print(emp+emp1)
print(emp-emp1)
print('rama'.__len__())
print(emp.__len__())