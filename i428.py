a=int(input())
b=[]
for _ in range(a):
    b.append(list(map(int,input().split())))
maxx=-111111111
minn=100000000000

for i in range(a-1):
    j=i+1
    x1=b[i][0]
    y1=b[i][1]
    x2=b[j][0]
    y2=b[j][1]
    t=abs(x1-x2)+abs(y1-y2)
    if t>maxx:maxx=t
    if t<minn:minn=t
print(maxx,minn)