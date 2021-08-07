# bfs를 이용한 풀이

from sys import stdin
N, M = map(int, stdin.readline().split())
matrix = [stdin.readline().rstrip() for _ in range(N)]          # matrix 배열
visited = [[0]*M for _ in range(N)]                             # 방문경로 배열
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]                           # 좌/우/위/아래 방향 이동

queue = [(0,0)]                                                 # queue 방식 사용
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:                                   # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))