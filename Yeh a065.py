b=[-1]
while True:
    try:
        a=list(input().split())
        case=a[0]
        if case=="C":
            if -1 in b:
                m=b.index(-1)
                b[m]=int(a[1])
            else:
                b.append(int(a[1]))
        elif case=="R":
            print("第{}筆資料為{}".format(int(a[1]),b[int(a[1])-1]))
        elif case=="U":
            b[int(a[1])-1]=a[2]
        elif case=="D":
            b[int(a[1])-1]=-1
        elif case=="F":
            if int(a[1]) in b:
                u=b.index(int(a[1]))+1
                print(str(a[1])+"在第"+str(u)+"項")
            else:
                print("找不到"+str(a[1]))
    except EOFError:
        break
for x in b:
    if x==-1:
        print("已刪除")
    else:
        print(x,end=" ")