class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s=Student(m1,m2)
        return s


obj=Student(10,20)
obj1=Student(1,2)

s=obj+obj1
print(s.m1)