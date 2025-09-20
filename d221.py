while True:
    a=int(input())
    if a==0:
        break
    else:
        b=list(map(int,input().split()))
        b.sort()
        cost=0
        total=0
        x=0
        for n in range(len(b)-1):
            total=b.pop(x+1)+b.pop(x)
            cost+=total
            b.append(total)
            b.sort()
        print(cost)