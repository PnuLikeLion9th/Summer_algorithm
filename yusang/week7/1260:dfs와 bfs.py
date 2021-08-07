n, m, v = map(int, input().split())
#편의를 위해 0을 빈 칸으로
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    #연결 여부를 담은 리스트
    matrix[a][b] = matrix[b][a] = 1
visited = [0]*(n+1)

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        #개행을 막음
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)
