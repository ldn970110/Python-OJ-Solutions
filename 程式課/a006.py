n=input()
n=n.split()
a=(int(n[0]))
b=(int(n[1]))
c=(int(n[2]))
if (b**2-(4*a*c))<0:
    print("No real root")
elif (b**2-(4*a*c))==0:
    print("Two same roots x={}".format(int((-b)/(2*a))))
else:
    x1=int(((-b)+(b**2-4*a*c)**0.5)/(a*2))
    x2=int(((-b)-(b**2-4*a*c)**0.5)/(a*2))
    print("Two different roots x1={} , x2={}".format((x1),(x2)))