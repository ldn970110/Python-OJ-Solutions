while True:
    try:
        a=int(input())
        b=list(map(int,input().split()))
        b.sort()
        print(*b)
    except EOFError:
        break