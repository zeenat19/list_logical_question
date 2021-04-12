ar=[1,2,3,4,5,6,7,8,9]
num=int(input("enter a any number--"))
x=0
i=0
count=0
length=len(ar)-1
while i<len(ar):
    x=i
    j=0
    while j<num:
        print(ar[x],end="")
        j=j+1
        x=x+1
        count=count+1
        if count==num:
            break

    i=i+1
    print()
        
