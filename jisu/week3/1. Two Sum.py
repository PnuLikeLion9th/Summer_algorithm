# 문제: https://leetcode.com/problems/two-sum
#난이도: Easy


# Solution 1) Brute Force로 구현
# 시간 복잡도 O(n^2)
# 무차별 대입 방식이라서 비효율적
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution 2) 첫 번째 수를 뺀 결과로 키 조회
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # 키와 값의 자리 change
        for idx, val in enumerate(nums):
            nums_map[val] = idx

        # target에서 첫 번째 수를 뺀 결과를 키로 조회
        for idx, val in enumerate(nums):
            if target - val in nums_map and idx != nums_map[target-val]:
                return [idx, nums_map[target-val]]
