def solution(nums):
    n = len(nums)/2
    nums = set(nums)    #중복 제거하기
    return n if len(nums) >= n else len(nums)