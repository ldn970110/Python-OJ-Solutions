a=int(input())
b=list(map(int,input().split()))
cost_min_list=[]
cost_list_all=[]
for y in range(a-1):
    cost_list=[]
    cost_min=99999999999999999
    for x in range(len(b)-1):
        n=abs(b[x]-b[x+1])
        cost_list.append(n)
        if n<cost_min:
            cost_min=n
    cost_min_list.append(cost_min)
    cost_list_all.append(cost_list)
    t=cost_list.index(cost_min)
    temp1=b[t]
    temp2=b.pop(t+1)
    b[t]=temp1+temp2
    print(b)
print(cost_list_all)
print(cost_min_list)
