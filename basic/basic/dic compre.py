d=['alluarjun','varun','nivin','vijay','tej']
m=['arya','kothabangarulokam','banglore days','police','new']
c=[(name,movie) for name,movie in zip(d,m)]
print(c)

my={}
for name,movie in zip(d,m):
    my[name]=movie
print(my)

x=[{name:movie} for name,movie in zip(d,m)]
print(x)
x={name:movie for name,movie in zip(d,m)}
print(x)