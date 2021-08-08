# 백준2178_미로 탐색_bfs_실버 1

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, str(input()))))
dn = [1,-1,0,0]
dm = [0,0,-1,1]
move = [[0,0]]

while move:
    a,b = move[0][0], move[0][1] # 이동한 x좌표와 y좌표 a,b에 입력
    del move[0]
    for i in range(4):
        x = a + dn[i] # 아래위로 이동
        y = b + dm[i] # 왼쪽, 오른쪽 이동
        if 0<=x<n and 0<=y<m and maze[x][y] == 1: # n,m 범위안에서 상하좌우에 1 거리에 길이 존재할때 실행
            move.append([x,y]) # 이동한 좌표 move로 입력
            maze[x][y] = maze[a][b] + 1 # 이동거리 입력

print(maze[-1][-1]) # 도착지점 이동거리 출력