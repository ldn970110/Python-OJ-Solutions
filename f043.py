while True:
    try:
        a,b=map(int,input().split())
        if a==b:
            b-=3
        if a>=3 and a<2147483648:
            c=a-b
            if c>b:
                temp=c
                c=b
                b=temp
            print("{}+{}={}".format(c,b,a))
    except EOFError:
        break