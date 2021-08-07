import sys
from collections import deque

def bfs(x, y, cnt = 1):
    maze[x][y] = 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    while q:
        now_x, now_y, cnt = q.popleft()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0 or not maze[nx][ny]:
                continue
            maze[nx][ny] = 0
            q.append((nx, ny, cnt+1))
            if nx == end[0] and ny == end[1]:
                return cnt+1
                break
    return -1

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int,input().split())
    maze = [list(map(int,input()[:-1])) for _ in range(N)]
    start, end = (0, 0, 1), (N-1, M-1)
    q = deque([])
    q.append(start)
    print(bfs(start[0],start[1],start[2]))