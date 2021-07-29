N,M,V = map(int,input().split())   # 정점, 간선, 탐색을 시작할 정점의 번호
matrix = [[0]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())    # 간선이 연결하는 두 정점의 번호 입력받기
    matrix[a][b] = matrix[b][a] = 1   # 연결되어있는 곳은 1로 두기
visit_list = [0] * (N+1)              # 이미 방문한 곳을 나타내줄 리스트

def dfs(V):  # 깊이 우선 탐색
    visit_list[V] = 1
    print(V, end=' ')
    for i in range(1,N+1):
        if visit_list[i] == 0 and matrix[V][i] ==1 : 
            dfs(i)

def bfs(V):  # 너비 우선 탐색
    queue = [V]
    visit_list[V] = 0
    while queue:
        V = queue.pop(0)
        print(V,end=' ')
        for i in range(1,N+1):
            if visit_list[i] ==1 and matrix[V][i] == 1:
                queue.append(i)
                visit_list[i] = 0

dfs(V)
print()
bfs(V)