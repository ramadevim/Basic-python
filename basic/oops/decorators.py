class Managers:
    def __init__(self, first, last):
        self.first = first  # instances represnted with self
        self.last = last
        # self.pay = pay
        # self.email = first + '.' + last + '@email.com'
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # @fullname.setter
    # def fullname(self,name):
    #     first,last=name.split(' ')
    #     self.first=first
    #     self.last=last
    #
    # @fullname.deleter
    # def fullname(self):
    #     print('deleted')
    #     self.first=first
    #     self.last=last

dec=Managers('rama','devi')
dec1=Managers('sai','a')

# dec.fullname='ramasai'
print(dec.first)
print(dec.fullname())
print(dec.email())