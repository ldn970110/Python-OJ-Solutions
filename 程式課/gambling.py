print("""遊戲說明
你現在有100元籌碼,每次遊戲你可以押骰子點數為
1、2、3、4、5、6其中一個,及賭資多少錢。
押中可以獲得押金的5倍,押輸則沒收賭資。
____________________________________________""")
totalchips=100
import random
while totalchips!=0:
    print("你現在有",totalchips,"元")
    R=random.randint(1,6)
    inputchips=int(input("請輸入賭資"))
    if inputchips>totalchips:
        print("你沒有足夠的金錢")
        continue
    r=int(input("請輸入骰子點數"))
    if r>6:
        print("點數超出範圍")
        totalchips-=inputchips
        continue
    if R==r:
        print('你贏了')
        totalchips+=inputchips*5
    else:
        print("你輸了")
        totalchips-=inputchips
print('遊戲結束')