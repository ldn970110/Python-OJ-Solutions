n,d=map(int,input().split())
item=[]
for _ in range(n):
    item.append(list(map(int,input().split())))
total_num=0
total=0
for i in item:
    t=max(i)-min(i)
    if t>=d:
        total_num+=1
        total+=sum(i)//3
print(total_num,total)