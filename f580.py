dice=[1,4,2]#上前右
r=[]
n,m=map(int,input().split())
for x in range(n):
    r.append([1,4,2])
for y in range(m):
    a,b=map(int,input().split())
    if a>0 and b>0:
        temp=r[a-1]
        r[a-1]=r[b-1]
        r[b-1]=temp
    elif b==-1:
        temp=r[a-1][0]
        r[a-1][0]=7-r[a-1][1]
        r[a-1][1]=temp
    elif b==-2:
        temp=r[a-1][0]
        r[a-1][0]=7-r[a-1][2]
        r[a-1][2]=temp
for z in range(n):
    print(r[z][0],end=" ")
