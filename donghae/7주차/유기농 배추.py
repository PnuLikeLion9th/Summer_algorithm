import sys
sys.stdin = open("input.txt","r")   

from collections import deque

num = int(input())

def bfs(start, visited):
    queue = deque()
    queue.append(start)
    dx, dy = [-1, 1, 0, 0, 0], [0, 0, 1, -1, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    return visited

for _ in range(num):    #테스트 수 만큼 반복
    m, n, k = map(int, input().split())
    matrix = [([0] * m) for _ in range(n)]
    visited = [([0] * m) for _ in range(n)]

    for _ in range(k):  #입력 개수만큼 간선 연결
        a, b = map(int, input().split())
        matrix[b][a] = 1

    cnt = 0 # 출력할 카운트 변수 생성
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visited[i][j] == 0: 
                cnt += 1
                bfs((i,j), visited)
    print(cnt)
    
