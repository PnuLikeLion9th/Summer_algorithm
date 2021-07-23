def solution(nums):
    n=int(len(nums)/2)
    if len(set(nums))<=n:
        return len(set(nums))
    elif len(set(nums))>n:
        return n