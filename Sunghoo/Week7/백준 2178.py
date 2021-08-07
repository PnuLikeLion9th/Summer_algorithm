from collections import deque


n,m= map(int,input().split())
world=[]

for i in range(n):
  world.append(list(map(int,input())))

def bfs(x,y):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  queue=deque()
  queue.append((x,y))
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if world[nx][ny]==1:
          world[nx][ny]=world[x][y]+1
          queue.append((nx,ny))

bfs(0,0)
print(world[n-1][m-1])