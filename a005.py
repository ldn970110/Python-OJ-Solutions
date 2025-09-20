for x in range(int(input())):
    a=list(map(int,input().split()))
    if a[1]-a[0]==a[2]-a[1]:
        n=a[1]-a[0]
        a.append(a[-1]+n)
        print(*a)
    else:
        n=a[1]/a[0]
        a.append(int(a[-1]*n))
        print(*a)