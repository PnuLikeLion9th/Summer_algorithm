#최단 경로? -> bfs
#내가 잘 이해하지 못한 거 : bfs로 어떻게 '최단'을 다루는지
#일단 ... queue를 쓴다는 것 자체가 최단을 의미하는 것이고 이 '최단'을 어떻게 다룰것인가 함음
#딛는 곳마다 이전의 수 +1 씩 한다.

from collections import deque

n,m = map(int,input().split()) # n: 세로, m: 가로
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    dx=[-1,1,0,0]   #이동 단위벡터
    dy=[0,0,-1,1]
    queue=deque()   #최단 파악하기 위해 큐 자료구조
    queue.append((x,y)) #위치를 다루기 위해 튜플로 넣어준다
    while queue:
        x,y=queue.popleft()   #x와y 하나씩 꺼낼 수 있다, 현재 위치 의미
        for i in range(4):
            nx=x+dx[i]
            ny=y=dy[i]
            if nx>=0 and nx<=n and ny>=0 and ny<=m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y]+1
                    queue.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])