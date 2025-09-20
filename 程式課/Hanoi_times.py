def n(x):
    if x==1:
        return 1
    else:
        return n(x-1)*2+1
x=64
print(n(x),"天後世界毀滅")