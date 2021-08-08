
import collections
n,m,v = map(int,input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
visitied = []
for _ in range(m):
    a,b = map(int,input().split())
    matrix[a][b] =matrix[b][a] = 1

def dfs(start,visitied):
    visitied += [start]
    for i in range(1,n+1):
        if matrix[start][i] == 1 and (i not in visitied):
            dfs(i,visitied)
    return visitied

def bfs(start):
    visitied = [start]
    queue = collections.deque([start])
    while queue:
        n = queue.popleft()
        for i in range(len(matrix[n])):
            if matrix[n][i] == 1 and (i not in visitied):
                visitied.append(i)
                queue.append(i)
    return visitied

print(' '.join(map(str,dfs(v,visitied))))
print(' '.join(map(str,bfs(v))))

