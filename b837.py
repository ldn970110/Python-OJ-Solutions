def F(n):
    if n==0:return 0
    if n==1:return 1
    return F(n-1)+F(n-2)
i=[]
for x in range(1000000):
    i.append(F(x))
print(i)