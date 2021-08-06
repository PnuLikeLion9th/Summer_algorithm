import sys
sys.stdin = open("input.txt","r")   #입력 예시 담긴 input.txt 가져오기

from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]  
visited = [[0]*m for _ in range(n)] #최소 지나는 칸 수 출력할 리스트

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]   #지나갈 곳을 확인하기 위해(좌우상하)

queue = deque()
queue.append((0,0)) #시작점 넣기
visited[0][0] = 1   #시작점 지나는 최소 칸수는 1

while queue:    #queue가 없어질 때 까지
    x, y = queue.popleft()
    if x == n-1 and y == m-1:   #(N,M) 위치로 이동하면 종료
        break
    for i in range(4):  #좌우상하 확인
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: #미로 벗어나지 않게 조건문 설정
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:    #방문하지 않았고 이동할 수 있는 칸인 경우
                visited[nx][ny] = visited[x][y] + 1 #현재의 최소 지나는 칸수 = 직전까지 지나온 칸수 + 1
                queue.append((nx, ny))  #queue에 현재 지점 넣기
print(visited[x][y])
