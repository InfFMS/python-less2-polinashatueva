a = int(input())
b = a % 10
if a<= 120 and b == 0 or b >= 5:
    print("лет")
elif a<= 120 and b == 1:
    print("год")
elif a<= 120:
    print("года")