#c123
while True:
    a=int(input())
    if a==0:
        break
    while True:
        A=[]    
        for x in range(1,a+1):
            A.append(x)
        b=list(map(int,input().split()))
        n=0
        B=[]
        station=[]
        if b[0]==0:
            print()
            break
        for x in range(a):
            station.append(A.pop(0))
            while True:
                if station[-1]==b[n]:
                    n+=1
                    station.pop()
                    if len(station)==0:
                        break
                elif station[-1]!=b[n]:
                    break
        if len(station)==0:
            print("Yes")
        else:
            print("No")