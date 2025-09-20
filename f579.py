a,b=map(int,input().split())
n=int(input())
car=[]
total=0
for i in range(n):
    temp=list(map(int,input().split()))
    j=0
    while(temp[j]!=0):
        if temp[j]<0:
            try:
                i=temp.index(-temp[j])
                temp[i]=0
            except:
                j+=1
                continue
        j+=1
    car.append(temp)
for i in car:
    if (a in i) and (b in i):
        total+=1
print(total)