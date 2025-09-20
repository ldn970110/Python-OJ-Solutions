t=sorted(list(map(int,input().split())))
a=t[0]
b=t[1]
c=t[2]
print(*t)
if(a+b<c):
    print("No")
elif (a**2+b**2<c**2):
    print("Obtuse")
elif (a**2+b**2==c**2):
    print("Right")
elif (a**2+b**2>c**2):
    print("Acute")
