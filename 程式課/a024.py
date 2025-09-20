def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

m, n = map(int, input().split())
print(gcd(m, n))