def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4    #(1,1,1), (1,2), (2,1), (3)
    return count(n-1) + count(n-2) + count(n-3)
case = int(input())
for _ in range(case):
    print(count(int(input())))