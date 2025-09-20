def roman_to_int(a):
    total = 0
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    i = 0
    while i < len(a):
        if i + 1 < len(a) and roman_map[a[i]] < roman_map[a[i+1]]:
            total += roman_map[a[i+1]] - roman_map[a[i]]
            i += 2
        else:
            total += roman_map[a[i]]
            i += 1
    return total

def int_to_roman(num):
    val_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    roman_num = []
    for val, roman_word in val_map:
        count = num // val
        if count>0:
            roman_num.append(roman_word * count)
        num %= val
    return "".join(roman_num)


while True:
    s = input().strip()
    if s == "#":
        break

    a, b = s.split()
    
    n = abs(roman_to_int(a) - roman_to_int(b))
    
    if n == 0:
        print("ZERO")
    else:
        print(int_to_roman(n))
