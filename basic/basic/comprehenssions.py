num=[10,20,30,40,50,60]
n=[i for i in num]
print(n)


n=[10,20,30,40]
s=[10,20]
n1=[i for i in n]
print(n1)

n2=[j*j for j in n]
print(n2)

n3=[s+s for s in n ]
print(n3)


for m in n:
    s.append(m*m)
print(s)

#using lambda
l=[1,2,3,4]
p=list(map(lambda a:a*a ,l))
print(p)

l=list(filter(lambda x:x%2==0,l))
print(l)

v=[i for i in l if i%2==0]
print(v)

my=[]
for letter in 'abcd':
    for num in range(4):
        my.append((letter,num))
print(my)



x=[(letter,num)for letter in 'abcd' for num in range(4)]
print(x)