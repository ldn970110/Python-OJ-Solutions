def n(x):
    if x==1:
        return 1
    else:
        return n(x-1)+2**x
a=n(int(input()))
print(a)