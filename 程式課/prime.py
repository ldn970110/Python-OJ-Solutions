a=int(input())
b=[]
for x in range(1,a+1):
    if a%x==0:
        b.append(x)
if len(b) ==2:
    print("True")
else:
    print("False")