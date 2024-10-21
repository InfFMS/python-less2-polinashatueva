a = int(input())
b = a % 10
if a <= 120:
    if b == 0 or b >= 5:
        print("лет")
    elif b == 1:
        print("год")
    else:
        print("года")
