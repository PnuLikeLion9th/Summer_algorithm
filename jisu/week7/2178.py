from collections import deque

N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input())))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 현재 위치에서 상하좌우 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 위치 벗어나면 안됨
                continue

            if matrix[nx][ny] == 0:  # 벽이므로 진행 불가
                continue

            if matrix[nx][ny] == 1:  # 벽 아니면 이동
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))
    return matrix[N-1][M-1]


print(bfs(0, 0))
