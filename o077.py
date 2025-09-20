h,w,n=map(int,input().split())
p=[]
for i in range(h):
    p.append([0 for j in range(w)])


for i in range(n):
    r,c,t,x=map(int,input().split())
    for j in range(len(p)):
        for k in range(len(p[j])):
            z=abs(j-r)+abs(k-c)
            if z<=t:
                p[j][k]+=x
for i in p:
    print(*i)
