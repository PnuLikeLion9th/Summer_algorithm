from collections import deque

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]    #지도 입력
visited = [[0]*n for _ in range(n)] # 방문 표시용

def bfs(start, visited):
    cnt = 0 #집 개수 카운트
    dx, dy = [-1, 1, 0, 0, 0], [0, 0, 1, -1, 0] #집이 하나인 경우까지 고려
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for i in range(5):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: #범위 벗어나지 않도록 조건문 설정
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1: 
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1   
    return cnt  #카운트 변수 반환

lst = []    #단지별 집 개수 담을 리스트 생성
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and matrix[i][j] == 1:    #방문하지 않은 곳만 방문하도록 설정
            lst.append(bfs([i,j], visited)) #집 개수 리스트에 추가
            
print(len(lst)) #리스트 길이 = 단지수
lst = sorted(lst)   #문제 조건: 오름차순 정렬
for i in lst:
    print(i)