# 백준_12865_평범한 배낭_DP_골드 5
# 배낭 알고리즘을 사용하는 문제이며 백준_1535_안녕 문제와 상당히 유사하다

import sys
input = sys.stdin.readline


n, k = map(int, input().split())
weight = [0]
value = [0]
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0 for _ in range(k+1)]for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if weight[i] > j:  # j 보다 큰 무게일 경우 전항의 값을 넣는다
            dp[i][j] = dp[i-1][j]
        # j 보다 작은 무게일 경우 전항의 값과 (이번항의 value + 이번항의 무게를 뺀값 중 넣을 수 있는 value의 값) 중 큰값을 넣는다
        else:
            dp[i][j] = max(value[i] + dp[i-1][j - weight[i]], dp[i-1][j])

print(dp[n][k])  # dp의 마지막 값을 출력
