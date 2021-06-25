# 백준15990_1,2,3 더하기 5_DP_실버 3

div = 1000000009
dp = [[0]*4 for _ in range(100001)]
dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % div
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % div
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % div

for _ in range(int(input())):
    n = int(input())
    result = (dp[n][1] + dp[n][2] + dp[n][3]) % div
    print(result)
