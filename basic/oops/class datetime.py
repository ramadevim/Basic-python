import time
import datetime


class Emp:
    @classmethod
    def fromdate(cls,t):
        y,m,d,mm,sec,days=time.localtime(t)
        return cls(y , m , d)
    @classmethod
    def datetime(cls):
        t=time.time()
        return cls.fromdate(t)

obj2=Emp()
a=Emp.fromdate()
print()