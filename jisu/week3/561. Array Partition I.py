# 문제: https://leetcode.com/problems/array-partition-i/
#난이도: Easy

# Solution 1)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()  # 오름차순

        for idx, val in enumerate(nums):
            if idx % 2 == 0:  # 짝수번째 값이면 sum에 누적
                sum += val
        return sum


# Solution 2)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])  # [::2]는 짝수 번째만 계산
