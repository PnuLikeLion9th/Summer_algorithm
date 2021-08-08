n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)] #인접 행렬 생성

m = int(input())
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b]=graph[b][a]=1

def dfs(start, visited):    #모든 경우를 탐색해야 하기 때문에 dfs선택
    visited += [start]
    for c in range(len(graph[start])):
        if graph[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited 

print(len(dfs(1, []))-1)    #시작 컴퓨터를 제외하기 위해 -1
