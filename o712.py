m,n,k,r,c=map(int,input().split())#處理題目給的輸入
map_=[]
for i in range(m):#輸入地圖
    map_.append(list(map(int,input().split())))
score=0#分數
stone=0#寶石
now=0 #0右1下2左3上
while map_[r][c]>0:#跑圖直到現在位置等於0
    score+=map_[r][c]
    stone+=1
    map_[r][c]-=1#跑過地方都會少一顆寶石
    if score%k==0:#分數為k倍數時要向右轉一次
        now+=1
    t=0
    while t<4:#因為每個都要轉一圈才能確定沒有路所以加個迴圈，最多跑4次0123
        if now>3:#方向如果從上轉到右要調整
            now=0
        if now==0:#右
            if c+1>n-1 or map_[r][c+1]==-1:
                now+=1
                t+=1
            else:
                c+=1
                break
        if now==1:#下
            if r+1>m-1 or map_[r+1][c]==-1:
                now+=1
                t+=1
            else:
                r+=1
                break
        if now==2:#左
            if c-1<0 or map_[r][c-1]==-1:
                now+=1
                t+=1
            else:
                c-=1
                break
        if now==3:#上
            if r-1<0 or map_[r-1][c]==-1:
                now+=1
                t+=1
            else:
                r-=1
                break

print(stone)#上面跑那麼多結果最終輸出就一個數字