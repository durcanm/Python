w="aaaaa"
q=[1,2]
t=(3,4)
d={'c':3,'d':4}

def f(x):
     w=x
     q.append(x)
     t=x
     d[x]=99
     



f('a')
print(w)
print(q)
print(t)
print(d)
