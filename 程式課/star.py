n=(int(input("請輸入數字")))
for x in range(1,n+1):
        for y in range(1,4):
            for z in range(1,x+1):
                print(y*'*'+(3-y)*" ",end="")
            print()