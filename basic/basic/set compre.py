n=[1,1,2,1,3,4,5,6,6,4,5,6,1]
x={num for num in n}
print(x)
y={num*num for num in n}
print(y)


#generators
x=[1,1,2,1,3,4,5,6,6,4,5,6,1]
# def gen_fun(x):
#     for n in x:
#         yield n*n
# b=gen_fun(x)
b=[n*n for n in x]
for i in b:
    print(i)

#string formating
L={'name':'rama','edu':'btech'}
x='my name is {0[name]} and i am completed {0[edu]}'.format(L)
print(x)

l=['sai','btech']
x='my name is {0[0]} and i am completed {0[1]}'.format(l)
print(x)


class person:
    def __init__(self,name,edu):
        self.name=name
        self.edu=edu
p=person('rama','btech')
x='my name is {0.name} and i am completed {0.edu}'.format(p)
print(x)

#keyword arguments
x='my name is {name} and i am completed {edu}'.format(name='ramasai',edu='btech')
print(x)


x='my name is {name} and i am completed {edu}'.format(**L)
print(x)

for i in range(1,10):
    y='the value is {:}'.format(i)
    print(y)