n=int(input())
m=int(input())
graph= [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    m1, m2=map(int,input().split())
    graph[m1][m2] = graph[m2][m1] = 1

visited=[]
def dfs(v):
    visited.append(v)
    for i in range(len(graph[v])):  #0,1,2,3,4,5,6,7
        if graph[v][i] == 1 and i not in visited:
            dfs(i)

dfs(1)
print(len(visited)-1)
