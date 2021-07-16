
#백준 미로탐색 bfs
from collections import deque

n,m = map(int,input().split())#입력받기
matrix = []
for i in range(n):
    matrix.append(list(map(int,input())))

dx = [1,-1,0,0]#다음 이동할 위치 경우의 수
dy = [0,0,1,-1]

queue = deque()
queue.append((0,0))#시작점 큐에 넣기

while queue:#큐가 있는동안 반복
    x,y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=m or nx<0 or ny>=n or ny<0:
            continue
        elif matrix[ny][nx] == 0:
            continue
        elif matrix[ny][nx] == 1:
            matrix[ny][nx] =matrix[y][x]+1
            queue.append(nx,ny)

print(matrix[n-1][m-1])



    