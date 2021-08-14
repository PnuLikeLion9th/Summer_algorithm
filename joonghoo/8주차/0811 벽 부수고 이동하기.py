# 백준_2206_벽 부수고 이동하기_bfs_골드 4
# 미로탐색 문제에서 벽 1개를 부수는 조건을 추가한 문제이다.
# 벽 하나를 부수고 방문했는지 부수지 않고 방문했는지를 나타내기 위해서 visited 리스트를 3차원으로 선언하여 풀이를 진행했다.
# https://hoovely0805.tistory.com/21 자세한 풀이는 블로그에 올렸습니다!

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    move = deque()
    move.append([0, 0, 0])
    while move:
        # z는 벽을 부쉈는지, 안부쉈는지 나타내는 값이다, 0일때 안부숨, 1일때 부숨
        x, y, z = move.popleft()

       # 그래프의 마지막 좌표에 도달하면 마지막 좌표의 값 출력
        if x == n-1 and y == m-1:
            return visited[z][x][y]

        # 현재 좌표의 4방향 탐색
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and visited[z][xx][yy] == 0:
                # 다음 좌표가 0 일때 해당 좌표 탐색
                if graph[xx][yy] == 0:
                    visited[z][xx][yy] = visited[z][x][y] + 1
                    move.append([xx, yy, z])
                # 벽을 아직 부수지 않았고, 다음 좌표가 1일때 해당 좌표의 4방향 탐색
                elif graph[xx][yy] == 1 and z == 0:
                    for j in range(4):
                        xxx = xx + dx[j]
                        yyy = yy + dy[j]
                        if 0 <= xxx < n and 0 <= yyy < m:
                            if graph[xxx][yyy] == 1:
                                continue
                            # 다음 좌표의 값이 0 이고 방문하지 않았다면 z=1로 바꾸고 queue에 좌표 추가
                            if visited[1][xxx][yyy] == 0:
                                visited[1][xxx][yyy] = visited[0][x][y] + 2
                                move.append([xxx, yyy, 1])

    # 마지막 좌표에 도달하지 않았을 경우 -1 출력
    return -1


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 벽을 부수고 방문했는지 알 수 있게 하기위해 visited를 3차원으로 선언한다.
visited = [[[0]*m for _ in range(n)] for _ in range(2)]
visited[0][0][0] = 1

# bfs 실행
print(bfs())
