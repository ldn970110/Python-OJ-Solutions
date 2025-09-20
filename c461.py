a,b,output=map(int,input().split())
if a>0:
    a=1
if b>0:
    b=1
t=0
if((a and b)==output):
    print("AND")
    t=1
if((a or b)==output):
    print("OR")
    t=1
if(a^b)==output:
    print("XOR")
    t=1
if not t:
    print("IMPOSSIBLE")