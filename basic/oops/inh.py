class Managers:
    def __init__(self, first, last, pay):
        self.first = first  # instances represnted with self
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'
        # Managers.num_of_emp += 1
class Candidates(Managers):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Emp(Managers):
    def __init__(self,first,last,pay,prog_lang,employees=None):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self,emp):
        for emp in self.employees:
            print(emp.fullname())

obj=Managers('rama','devi',30000)
obj1=Candidates('sai','rama',20000,'python')
obj3=Emp('mr','rm',40000,[obj1],'django')
print(obj1.first)
print(obj1.prog_lang)
print(obj3.email)
# obj3.add(obj1)
# obj3.print_emp()
print(isinstance(Managers,Candidates))
print(issubclass(Managers,Candidates))