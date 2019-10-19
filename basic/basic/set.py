s={'rama','sai','rm','ram'}
s1={'rama','sai','mr'}

print(type(s))
print(len(s))
a=','.join(s)
print(a)
print(a.split())
print('rama' in s)
print(s.intersection(s1))
print(s.difference(s1))
print(s.union(s1))