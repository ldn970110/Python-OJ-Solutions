time =int(input())
for x in range(time):
    a,b,c=map(int,input().split())
    n=0
    for y in range(a+1,b):
        if y%c!=0:
            print(y,end=" ")
            n=1
    if n==0:
        print("No free parking spaces.")
    else:
        print()