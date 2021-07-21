# 문제: https://leetcode.com/problems/number-of-islands/
#난이도: Medium

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = '#'  # 이미 탐색 된 섬은 #로 표시

            # 인접 영역 탐색
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # 현재 위치가 섬이면
                    dfs(i, j)  # dfs로 상하좌우도 섬인지 탐색
                    cnt += 1
        return cnt
