# 백준17404_RGB거리 2_DP_골드 4

import sys
input = sys.stdin.readline

n = int(input())
rgb = []
result = sys.maxsize
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for index in range(3):
    dp = [[0]*3 for _ in range(n)]
    for i in range(3):
        if i == index:
            dp[0][i] = rgb[0][i]
        else:
            dp[0][i] = sys.maxsize

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

    for i in range(3):
        if i == index:
            continue
        else:
            result = min(result, dp[n-1][i])

print(result)
