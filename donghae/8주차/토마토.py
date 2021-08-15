from collections import deque

def bfs(queue, box):    
    global days 
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]  
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: 
                if box[nx][ny] == 0:  
                    box[nx][ny] = box[x][y] + 1
                    days = box[x][y]
                    queue.append((nx,ny))
    for b in box:  
        if 0 in b:
            return -1
    return days

m, n = map(int, input().split())
box = [[0] * m for _ in range(n)]  

days = 0
queue = deque()
for i in range(n):
    box[i] = list(map(int, input().split()))
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))
print(bfs(queue, box))

# for i in range(n):
#     print(box[i])