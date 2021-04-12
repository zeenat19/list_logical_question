ar=[1,2,3,4,5,6,7,8,9]
num=int(input("enter a any number--"))
i=0
count=0
x=0
length=len(ar)-1
while i<len(ar):
    j=0
    while j<num:
        print(ar[x],end=" ")
        count+=1
        if count==num:
            break
        j=j+1
        x=x+1
    i=i+1
    print()