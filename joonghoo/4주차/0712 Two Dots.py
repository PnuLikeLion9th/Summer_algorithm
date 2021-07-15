# 백준_16929_Two Dots_DFS_골드 4
# dfs로 그래프를 탐색하다가 사이클의 길이가 4이상이고 다음 탐색할 좌표가 시작했던 좌표라는 조건을 만족시
# Yes를 출력하고 끝까지 탐색해도 조건을 만족하지 못하면 No를 출력한다

import sys
input = sys.stdin.readline


def dfs(now_x, now_y, cnt):
    global start_x, start_y

    if cnt >= 4:  # 조건 만족시 Yes 출력하고 프로그램 종료
        for i in range(4):
            if now_x + dx[i] == start_x and now_y + dy[i] == start_y:
                print("Yes")
                exit(0)

    for i in range(4):  # 현재좌표의 상하좌우 좌표 중 탐색하지 않았고 색이 같은 좌표를 탐색한다
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m and visited[next_x][next_y] == 0 and graph[next_x][next_y] == graph[start_x][start_y]:
            visited[next_x][next_y] = 1
            dfs(next_x, next_y, cnt+1)


n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        start_x = i  # 시작 x 좌표값 저장
        start_y = j  # 시작 y 좌표값 저장

        # 시작하는 좌표값을 다르게 탐색해 봐야하므로 dfs시작할때마다 초기화
        visited = [[0]*m for _ in range(n)]
        visited[i][j] = 1
        dfs(i, j, 1)

print("No")
