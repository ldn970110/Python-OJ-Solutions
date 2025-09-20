a=list(map(int, input().split()))
b=[]
n=0
a.pop()
for _ in range(10):
  if a[n]==10:
    b.append(10+a[n+1]+a[n+2])
    n+=1
  elif a[n]+a[n+1]==10:
    b.append(10+a[n+2])
    n+=2
  else:
    b.append(a[n]+a[n+1])
    n+=2
total=0
for x in b:
    total+=x
    print(total,end=" ")