#i213
n=int(input())
s=[]
for x in range(n):
    a=list(map(int,input().split()))
    if a[0]==1:
        
        s.append(a[1])
    elif a[0]==2:
        try:
            print(s[-1])
        except:
            print(-1)
    elif a[0]==3:
        try:
            s.pop()
        except:
            continue