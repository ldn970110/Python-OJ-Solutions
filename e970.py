a=int(input())
b=list(map(int,input().split()))
B=b[-1]
c=[]
for x in range(1,a+1):
    if x%B==1:
        c.append(x)
t=0
for y in c:
    t+=b[y-1]
M=t%a
if M==0:
    print(a,b[-1])
else:
    print(M,b[M-1])