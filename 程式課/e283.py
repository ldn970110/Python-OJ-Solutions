d={'0 1 0 1':"A",'0 1 1 1':"B",'0 0 1 0':"C",'1 1 0 1':"D",'1 0 0 0':"E",'1 1 0 0':"F"}
while True:
    try:
        a=int(input())
        b=[]
        for x in range(a):
            c=str(input())
            b.append(d[c])
        print(*b,sep="")
    except:
        break