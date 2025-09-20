n = int(input())

a = []

i = 2 
while i*i <= n:
    if n % i == 0:
        count = 0

        while n % i == 0:
            n = n // i
            count += 1
        a.append([i, count])
    i += 1
if n > 1:
    a.append([n, 1])


output_parts = []

for p, c in a:
        if c > 1:
            output_parts.append(f"{p}^{c}")
        else:
            output_parts.append(str(p))
    
print(" * ".join(output_parts))