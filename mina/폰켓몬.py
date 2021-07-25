def solution(nums):
    N = len(nums)
    answer = 0
    if len(set(nums)) <= N/2 :
        answer = len(set(nums))
    else :
        answer = N/2
    return answer