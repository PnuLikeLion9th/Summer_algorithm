n = int(input())
m = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0]*(n+1)

answer = []

def dfs(i):
    
    visited[i] = 1
    for j in range(1, n+1):
        #갈 수 있다면
        if matrix[i][j] == 1 and visited[j] == 0:
            answer.append(1)
            dfs(j)
    return 0
            
dfs(1)
print(len(answer))
