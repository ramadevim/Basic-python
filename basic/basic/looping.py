num=[1,2,3,4,5,6]
for i in num:
    if i==3:
        print('found')
        break
    if i==5:
        print('continue')
        continue
    print(i)

for i in num:
    for letter in 'abc':
        print(num,letter)

i=1
while i<5:
    if i==4:
        continue
        # break
    print(i)
    i+=1