# i=1
# a=1
# while i<=100:
#     if ((a%3 and a%5)==0) :
#         a=a+1
#     else:
#         print(a)
#         a=a+1
#     i=i+1

for c in range(1,10):
    if not (c%3 and c%5)==0:
        print(c)


from array import *

val=array('i',[1,5,6,7,4])
print(val)