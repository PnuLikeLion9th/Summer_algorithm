def solution(nums):
    answer = 1
    n = int(len(nums)/2)
    nums = set(nums)  # 집합set으로 변환
    nums = list(nums)  # list로 변환

    i = len(nums)
    if i <= n:
        return i
    else:
        return n
