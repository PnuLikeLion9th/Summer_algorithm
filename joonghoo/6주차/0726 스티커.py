# 백준_9465_스티커_DP_실버 2
# 대각선 한칸 (아래, 위), 대각선 두칸 (아래, 위) 중에서 더 큰 값을 더해가면 되는 DP 문제
# 2차원 list를 형성하여 첫번째 줄의 스티커를 처음선택 할때는 dp[0][i] 에 저장, 두번째 줄의 스티커를 처음선택 할때는 dp[1][i] 에 저장한다

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = []
    dp.append(list(map(int, input().split())))  # 첫번째 줄의 스티커를 입력받는다
    dp.append(list(map(int, input().split())))  # 두번째 줄의 스티커를 입력받는다

    for i in range(1, n):
        if i == 1:  # n이 2인 경우를 고려
            dp[0][1] += dp[1][0]
            dp[1][1] += dp[0][0]
        else:
            # 첫번째 줄에서 대각선 한칸 아래와 대각선 두칸 아래의 스티커 값을 비교
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            # 두번째 줄에서 대각선 한칸 위와 대각선 두칸 위의 스티커 값을 비교
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
