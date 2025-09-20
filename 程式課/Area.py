x=(input().split())
a=int(x[0])
b=int(x[1])
c=int(x[2])
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    total=(((s-a)+(s-b)+(s-c))*s)**0.5
    print(total)
else:
    raise Warning("錯誤")
    
    


