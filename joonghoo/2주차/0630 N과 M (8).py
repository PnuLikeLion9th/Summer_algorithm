# 백준_15657_N과 M (8)_백트래킹_실버 3
# 첫번째 시도, itertools 사용하여 중복순열 구해서 풀이진행 ==> 메모리 초과
# 두번째 시도, dfs로 풀이

def dfs(depth, index, n, m):
    if depth == m:
        print(*solve)
        return
    for i in range(index, n):
        solve.append(nums[i])
        dfs(depth+1, i, n, m)
        solve.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
solve = []
dfs(0, 0, n, m)
