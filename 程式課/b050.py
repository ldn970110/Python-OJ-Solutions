while True:
    try:
        t=1
        A=set()
        B=set()
        n=input()
        A.add(input())
        B.add(input())
        print("Test Case",str(t)+":")
        print("A+B :",A|B)
        print("A*B :",A&B)
        print("A-B :",A-B)
        print("B-A :",B-A)
        if A in B:
            print("A contains B")
        else:
            print("A does not contain B")
        if B in A:
            print("B contains A")
        else:
            print("B does not contain A")
        t+=11
    except:
        break