x=int(input("請輸入一個正整數"))
for n in range(x+1):
    if n*n==x:
        print(n)
        break
else:
    print("沒有整數平方根")