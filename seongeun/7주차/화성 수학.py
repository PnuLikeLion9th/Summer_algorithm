#백준 파이썬 50제- 화성 수학

t = int(input())

for i in range(t):
    a = list(map(str,input().split()))
    num = float(a.pop(0))
    for j in range(len(a)):
        if a[j] == '@':
            num *= 3
        elif a[j] == '%':
            num += 5
        elif a[j] == '#':
            num -= 7
    
    print("%0.2f" % num)