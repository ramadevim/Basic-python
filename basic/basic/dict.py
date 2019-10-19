d={1:'rama',2:'sai',3:'rama'}
print(d[1])
print(d.get(2))
d['name']='sairama'
print(d)
d[1]='hello'
print(d)
d.update({'name':'ramasai'})
print(d)
del d[3]
print(d)
print(d.pop(1))
print(d.keys())
print(d.values())
print(d.items())
for key,value in d.items():
    print(key)
