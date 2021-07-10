n, x = map(int, input().split())
Arr = list(map(int, input().split()))
for i in Arr:
    if i < x:
        print(i, end=" ")