# 백준9095_1,2,3 더하기_DP_실버 3
# n을 하나씩 대입해 가며 dp[n] = dp[n-3] + dp[n-2] + dp[n-1] 라는 점화식을 세운다
# 테스트 케이스를 받는 문제라서 미리 n의 모든 값을 넣어 nums에 저장한다.

nums = [0, 1, 2, 4]
for i in range(4, 12):
    nums.append(nums[i-3] + nums[i-2] + nums[i-1])
for _ in range(int(input())):
    print(nums[int(input())])
