for a in range(100,1000):
    b = a//100
    c = a//10
    d = c%10
    e = a%10
    if a == b**3 + d**3 + e**3:
        print(a)
