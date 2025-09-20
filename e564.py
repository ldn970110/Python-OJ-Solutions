def ENQUEUE(n,m):
    team=0
    for x in range(b):
        if n in b[x]:
            team=x
            

        

while True:
    a=int(input())
    b=[]
    if a==0:
        break
    for x in range(a):
        temp=list(map(int,input().split()))
        temp.pop(0)
        b.append(temp)
    queue=[]
    while True:
        c=list(input().split())
        if c[0]=="ENQUEUE":
            ENQUEUE(int(c[0]),queue)



