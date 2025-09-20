#線分割平面遞迴關係a(n)=a(n-1)+n,n>=2
#an=(n**2+n+2)/2
#平面分割空間 b(n)=a
def line(n):
    if n==0:
        return (n**2+n+2)/2 #等於2
    else:
        return line(n-1)+n
def space(n):
    if n==1:
        return (n**3+5*n+6)/6 #等於2
    else:
        return space(n-1)+line(n-1)
print(int(space(int(input()))))













#看這兩個文章現學現賣 https://reurl.cc/3epoDV
#有錯請多指教 https://reurl.cc/gap27p