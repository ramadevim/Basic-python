def hello():
   return 'hello'
print(hello().upper())


x='rama'
def f1():
    global x
    z='ramasai'

    y='sai'
    print(y)
    print(x)
    print(z)
print(f1())
print(x)

def x(a):
    x='rama'
    print(a)
x('hello')

import builtins
print(dir(builtins))
m=min(1,2,3,4,5,6)
print(m)


def outer():
    x='outer x'
    def inner():
        x='inner x'
        print(x)
    inner()
    print(x)
outer()



def m(greeting,name='sai'):
    return '{},{}'.format(greeting,name)
print(m('hi'))


def my(*args,**kwargs):
    print(args)
    print(kwargs)
my('ram','sai',name='rama',edu='btech')
def my(*args,**kwargs):
    print(args)
    print(kwargs)
c=('ram', 'sai')
d={'name': 'rama', 'edu': 'btech'}

my(*c,**d)



months=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def day_in_month(year,month):
    if not 1<=month<=12:
        return 'Invalid month'
    if month==2 and is_leap(year):
        return 29
    return months[month]
print(months[5])




