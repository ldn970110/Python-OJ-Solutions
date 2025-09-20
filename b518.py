N = int(input())
for __ in range(N):
    dict_C2P = {}
    dict_P2C = {}
    m = int(input())
    root = -1
    for _ in range(m):
        c,p = input().strip().split(",")
        dict_C2P[c] = p
        if p in dict_P2C.keys():
            dict_P2C[p].append(c)
        else:
            dict_P2C[p] = [c]
        if p == "99" : root = c
    leaf = sorted(list(set(dict_C2P.keys()) - set(dict_P2C.keys()) ))
    for l in leaf: