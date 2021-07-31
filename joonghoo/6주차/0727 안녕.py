# 백준_1535_안녕_DP_실버 2
# 배낭 알고리즘을 사용하는 문제

import sys
input = sys.stdin.readline

n = int(input())
hp = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(100)]for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(100):
        if hp[i] > j:  # j 보다 큰 hp 일 경우 전항의 값을 넣는다
            dp[i][j] = dp[i-1][j]
        # j 보다 작은 hp 일 경우 전항의 값과 (이번항의 happy + 이번항의 hp를 뺀값 중 넣을 수 있는 happy의 값) 중 큰값을 넣는다
        else:
            dp[i][j] = max(happy[i] + dp[i-1][j - hp[i]], dp[i-1][j])

print(dp[n][99])  # dp의 마지막 값을 출력
