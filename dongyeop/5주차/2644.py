from collections import deque
n = int(input())
matrix = [[] for i in range(n+1)]
result = [0]*(n+1)
a,b= map(int,input().split())
relation_n = int(input())
for i in range(relation_n):
    x,y = map(int,input().split())
    matrix[x].append(y)
    matrix[y].append(x)
def bfs(start,end):
    q = deque()
    q.append(start)
    visited = []
    while q:
        s = q.popleft()
        visited.append(s)
        if s == end:
            break
        for i in matrix[s]:
            if i not in visited:
                result[i] = result[s]+1
                q.append(i)
    if result[end] == 0:
        print(-1)
    else:
        print(result[end])

bfs(a,b)

