num=int(input("enter any num:"))
i=1
a=[]
while i<=num:
    j=1
    b=[]
    a.append(i)
    while j<=10:
        d=j*i
        b.append(d)
        j=j+1
    i=i+1
    a.append(b)
print(a)