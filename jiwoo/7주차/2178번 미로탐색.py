n,m = map(int,input().split())
matrix = [input() for i in range(n)]
visited = [[0]*(m+1) for i in range(n+1)]

dx = [1,-1,0,0]   # 좌우 이동범위
dy = [0,0,-1,1]   # 상하 이동범위

queue = [(0,0)]
visited[0][0] = 1

# bfs 탐색방법 사용
while queue:
    x,y = queue.pop(0)

    if x == n-1 and y == m-1 :    # (N,M)위치에 도착한 경우
        print(visited[x][y])      # 지나야하는 최소 칸 수 출력
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':    # '1'이고, 이미 방문한 곳이 아닐 경우
                visited[nx][ny] = visited[x][y] + 1      # 지나온 칸 수 1 추가하기
                queue.append((nx,ny))