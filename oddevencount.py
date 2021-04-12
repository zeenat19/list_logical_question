elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
count=0
count1=0
while i<len(elements):
    if elements[i] % 2==0:
        print(elements[i],"even num")
        count=count+elements[i]
    else:
        print(elements[i],"odd num")
        count1=count1+elements[i]
    i=i+1
print(count,"even num")
print(count1,"odd num")