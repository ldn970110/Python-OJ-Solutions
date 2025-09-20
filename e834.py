a=int(input())
b=list(map(int,input().split()))
c=[]
for x in b:
    if x%a==0:
        c.append(int(x/a))
    else:
        c.append(a-(x%a))
c.pop()
for y in range(len(c)):
    print(c[y])
