n, m = map(int, input().split())
matrix= []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    matrix.append(list(input()))
queue = [[0, 0]]
matrix[0][0] = 1

while queue:
    x, y = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == "1":
            queue.append([nx, ny])
            matrix[nx][ny] = matrix[x][y] + 1
print(matrix[n - 1][m - 1])