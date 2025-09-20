A=[[1,2],[3,4],[5,6]]
B=[[1,3],[2,5],[9,8]]
C=[]
D=[]
for x in range(len(A)):
    for i in range(len(A[x])):
        total=A[x][i]+B[x][i] 
        print(total)
        C.append(total)
print(C)