try:
    while True:
        num = int(input())
        b = []
        while num > 0:
            b.append(num%2)
            num //= 2
        for i in range(len(b)-1,-1,-1):
            print(b[i],end="")
        print()

except:
    pass