n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0]*(n+1)

# dfs: 하나의 정점에서 시작하여 그 정점의 인접한 정점 중 아직 방문하지 않은 정점이 없다면 탐색 종료
# 있다면 방문하여 그 정점으로 부터 다시 dfs를 진행하는 재귀적인 방법
# 스택, 재귀 사용


def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and matrix[v][i] == 1:
            dfs(i)


# bfs: 시작 정점으로부터 가까운 정점을 먼저 방문, 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법
# 큐 사용
def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 1 and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)
