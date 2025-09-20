a,b=map(int,input().split())
place=[]
tallest=0

for x in range(b):
    place.append(0)
tree=list(map(int,input().split()))
tree_high=list(map(int,input().split()))
n=0
for x in tree:
    place[x-1]=tree_high[n]
    n+=1
for x in range(len(place)):
    if place[x]!=0:
        torf=1
        for y in range(place[x]):#向右找
            if place[x+y]!=0:
                continue
            else:
                torf=0
                break
        if x-place[x]<0:
            torf=0
        else:
            for y in range(place[x]):#向左找
                if place[x+y]!=0:
                    continue
                else:
                    torf=0
                    break
        if torf:
            if place[x]>tallest:
                tallest=place[x]
            place[x]=0

        
            
        


