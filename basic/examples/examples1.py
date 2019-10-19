#fibonacci
num=int(input('enter a num:'))
a,b=0,1
for i in range(num+1):
    print(a)
    a,b=b,a+b

#fact
num=int(input('enter a num:'))
fac=1
while num>0:
    fac=fac*num
    num=num-1
print(fac)

#prime num
num=int(input('enter a num:'))
for j in range(2,num):
    if j%2==0:
        print('not a prime num')
        break
else:
    print('prime num')

#armstrong
num=int(input('enter a num:'))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if num==sum:
    print('armstrong')
else:
    print('not a armstrong')


#palindrome
num=int(input('enter a num:'))
sum=0
temp=num
while num>0:
    digit=num%10
    sum=sum*10+digit
    num//=10

if temp==sum:
    print('palindrome')
else:
    print('not a palindrome')

#even odd
num=int(input('enter a num:'))
if num%2==0:
    print('even')
else:
    print('odd')

#+-0
num=int(input('enter a num:'))
if num>0:
    print('positive')
elif num==0:
    print('zero')
else:
    print('negative')

#check leap year
num=int(input('enter a num:'))
if num%4==0:
    print('leap')
else:
    print('not a leap')

#intervals b/w prime
num1=int(input('enter a prime num'))
num2=int(input('enter a prime num'))
for i in range(num1,num2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(num,'not a prime')
                break
        else:
            print('prime num',i)