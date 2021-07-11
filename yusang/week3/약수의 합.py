def solution(n):

    nums = list(range(n+1))
    answer = 0

    for num in nums[1:]:
        if n % num == 0:
            answer = answer + num

    return answer


print(solution(12))
