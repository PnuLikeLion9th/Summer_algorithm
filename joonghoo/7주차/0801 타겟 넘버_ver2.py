# 프로그래머스_타겟 넘버_dfs/bfs_레벨 2
# DFS를 활용한 풀이

cmds = ['+', '-']
lst = []
result = 0


def dfs(nums, target):
    global result
    if len(nums) == len(lst):  # 연산자 list가 nums의 길이와 같을떄
        number = 0
        for i in range(len(nums)):
            if lst[i] == '+':  # + 연산자일 경우 +
                number += nums[i]
            else:  # - 연산자일 경우 -
                number -= nums[i]
        if target == number:  # 계산 결과가 target 과 같다면 +1
            result += 1
        return
    for cmd in cmds:
        lst.append(cmd)
        dfs(nums, target)
        lst.pop()


def solution(nums, target):
    dfs(nums, target)
    return result


print(solution([1, 1, 1, 1, 1], 3))
