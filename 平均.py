e=0
def ave(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))    
while True:
        
        x=input("請輸入數字(輸入完畢請輸入:結束)")
        if x =="結束":
             break
        else :
              x=int(x)
              abc=[0]
              abc[e]=x
              e=e+1
ave(abc(0,len(abc)))