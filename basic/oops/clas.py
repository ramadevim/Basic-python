class Emp:
    def __init__(self,first,last,pay):
        self.first=first#instances represnted with self
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@comapny.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.email)


obj=Emp('rama','devi',5000)
print(obj.first,obj.last,obj.email,obj.pay)
print('{} {}'.format(obj.first,obj.last))
print(obj.fullname())
# obj.first='rama'
# obj.last='devi'
# obj.pay=50000
# obj.email='ramadevi@company.com'
# print(obj.email)