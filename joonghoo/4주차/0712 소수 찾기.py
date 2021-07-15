# 프로그래머스_소수 찾기_수학_레벨 1
# n의 최댓값이 100만이므로 에라토스테네스의 체를 사용해야한다.

def solution(n):
    nums = [0 for _ in range(n+1)]
    count = 0
    for i in range(2, n+1):
        if nums[i] == 1:  # 합성수일경우 continue
            continue
        else:  # 소수일경우 count += 1
            count += 1
        for j in range(i, n+1, i):  # i의 배수를 전부 합성수 처리
            nums[j] = 1
    return count
