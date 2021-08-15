def calMin(n):
    lst = [0] * (n+1)
    for i in range(2, n+1): 
        lst[i] = lst[i-1] + 1   # 2와 3으로 나누어 떨어지지 않는 경우
        if i % 3 == 0: 
            lst[i] = min(lst[i], lst[i//3]+1)
        if i % 2 == 0:
            lst[i] = min(lst[i], lst[i//2]+1)
    return lst[n]
n = int(input())
print(calMin(n))