while True:
    try:
        a=int(input())
        b=list(map(int,input().split()))
        b.sort(key=lambda x:(x%10,-x//10))
        print(*b)
    except:
        break