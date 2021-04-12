
name=["n","i","t","i","n"]
i=0
i=len(name)-1
a = []
while i >= 0:
    print(name[i])
    a.append(name[i])
    i = i - 1
print(a)
if name == a:
    print("its a palindrome")
else:
    print("its not palindrome")