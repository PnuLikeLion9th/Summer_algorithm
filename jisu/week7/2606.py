n = int(input())
m = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0]*(n+1)

result = []


def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            result.append(i)
            dfs(i)
    return len(result)


print(dfs(1))
