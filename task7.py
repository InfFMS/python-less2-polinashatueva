n = int(input())
x = 0
for i in range(2,n+1):
    x=0
    for t in range(2,i):
        if i%t==0:
            x=x+1
    if x==0:
        print(i)