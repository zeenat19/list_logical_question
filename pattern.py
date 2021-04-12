num=int(input("enter the num:"))
num1=int(input("enter the num1:"))
i=0
b=1
s=[]
while i<num:
    j=0
    a=[]
    while j<num1:
        a.append(b)
        j=j+1
        b=b+1
    i=i+1
    s.append(a)
print(s)
