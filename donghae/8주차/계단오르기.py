def calMax(n):
    if n == 1:  # n이 1인 경우 첫번째 계단 반환
        return stairs[1]
    lst = [0 for _ in range(n+1)]
    # 첫번째 계단, 두 번째 계단 max값 계산   
    lst[1] = stairs[1]  
    lst[2] = stairs[1] + stairs[2]
    # 계단 수가 3개 이상인 경우 마지막 계단 기준으로 2경우로 나누기
    for i in range(3, n+1):
        lst[i] = max(stairs[i] + stairs[i-1] + lst[i-3], stairs[i] + lst[i-2])
    return lst[n]

n = int(input())
stairs = [0 for _ in range(n+1)]
for i in range(1, n+1):
    stairs[i] = int(input())
print(calMax(n))