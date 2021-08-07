from collections import deque

N,M,V = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)] #(N+1 x N+1) 행렬

for _ in range(M):
    m1, m2= map(int,input().split())   #간선 입력되는 수를 받아서
    graph[m1][m2] = graph[m2][m1] = 1   #행렬에 1을 입력해준다 (노드 연결을 행렬로 표시)

visited=[]
def dfs(graph,v,visited):
    visited.append(v)
    print(v, end=' ')
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and i not in visited:
            dfs(graph,i,visited)

visited=[]
def bfs(start):
    queue=deque([start])
    visited.append(start)
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in range(len(graph[v])):
            if graph[v][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)

dfs(graph,V,visited)
print()
bfs(V)
