a=[12,14,57,34,39]
b=[]   
for c in a:
    if c%2==0:
        b.append(c)
print(b)
d=[e for e in a if e%2==0]
print(d)