# 백준2579_계단 오르기_DP_실버 3
# 연속해서 2번 밟는 것과 두 계단을 한꺼번에 오르는 경우의 값 중에 큰 값을 dp에 저장한다
# 이때 연속해서 2번 밟을때는 3번을 연속해서 밟을수 없다는 규칙 때문에 dp[i-3]의 값을 더해준다

import sys

input = sys.stdin.readline
n = int(input())
nums = []
dp = []
for _ in range(n):
    nums.append(int(input()))
# n이 1,2,3 일때는 점화식의 범위를 벗어나므로 직접 dp에 저장한다
if n > 3:
    dp.append(nums[0])
    dp.append(max(nums[1], nums[0] + nums[1]))
    dp.append(max(nums[0] + nums[2], nums[1] + nums[2]))
    # n이 3보다 크면 점화식을 통해서 dp에 저장
    for i in range(3, n):
        dp.append(max(nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2]))
elif n == 3:
    dp.append(nums[0])
    dp.append(max(nums[1], nums[0] + nums[1]))
    dp.append(max(nums[0] + nums[2], nums[1] + nums[2]))
elif n == 2:
    dp.append(nums[0])
    dp.append(max(nums[1], nums[0] + nums[1]))
elif n == 1:
    dp.append(nums[0])

print(dp[-1])
