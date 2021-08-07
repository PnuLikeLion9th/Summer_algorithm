# pythonic
from itertools import product
def solution(numbers, target):
    temp = [(i, -i) for i in numbers]
    answer = [sum(i) for i in product(*temp)]
    return answer.count(target)


# dfs
def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret
def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
