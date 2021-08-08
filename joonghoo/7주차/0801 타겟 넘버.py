# 프로그래머스_타겟 넘버_dfs/bfs_레벨 2
# 중복순열 문제이다
# product 함수를 통해서 +,-를 길이가 n만큼 반복하여 나타나는 모든 순열들을 구해준다
# 구한 중복순열을 이용하여 연산을 하고 계산을 통해 나온 숫자가 target과 같을때 count++ 해준다

import itertools


def solution(nums, target):
    n = len(nums)
    result = 0
    # +,- 연산자로 이루어져있고, 길이가 n인 모든 중복순열을 구한다
    cmds = itertools.product(['+', '-'], repeat=n)
    for cmd in cmds:
        number = 0
        for i in range(n):
            if cmd[i] == '+':  # + 연산자일 경우 +
                number += nums[i]
            else:  # - 연산자일 경우 -
                number -= nums[i]
        if number == target:  # 계산을 통해 나온 숫자가 target과 같을 경우 +1
            result += 1
    return result


print(solution([1, 1, 1, 1, 1], 3))
