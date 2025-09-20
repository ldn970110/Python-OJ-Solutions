a=[[1],[2,3]]
n=1
for x in range(len(a)):
    if n in a[x]:
        print(x)
        print(a[x].index(n))
    break
