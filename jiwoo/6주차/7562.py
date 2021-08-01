from collections import deque
import sys

def bfs():   # bfs 방법으로 구현
    q = deque()
    q.append((a,b))     # 처음 나이트의 위치

    while q :
        x,y = q.popleft()
        if x == c and y == d :  # 원하는 위치로 나이트가 이동한 경우        
            print(visit[x][y])  # 횟수 출력
            break
        
        dx = [2,-2,2,-2,1,-1,1,-1]   # 나이트의 이동 가능 범위
        dy = [1,-1,-1,1,2,-2,-2,2]  

        for i in range(8):
          nx = x + dx[i]
          ny = y + dy[i]

          if 0 <= nx < L and 0 <= ny < L:
             if visit[nx][ny] == 0:
                 visit[nx][ny] = visit[x][y] + 1   # 나이트가 이동한 횟수 1 추가
                 q.append((nx,ny))
     
n = int(sys.stdin.readline())  # 테스트 케이스 개수 입력 받기

for i in range(n):
    L = int(sys.stdin.readline())   # 체스판 한 변의 길이
    visit = [[0] * (L+1) for i in range(L+1)]   
    a,b = map(int,sys.stdin.readline().split())   # 현재 나이트의 위치
    c,d = map(int,sys.stdin.readline(). split())  # 이동하려고 하는 위치
    bfs()