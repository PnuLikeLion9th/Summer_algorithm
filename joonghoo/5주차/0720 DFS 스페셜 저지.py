# 백준_16964_DFS 스페셜 저지_DFS_골드 5
# 입력된 그래프를 DFS로 탐색할때 입력된 순서로 탐색할 경우 1 출력, 아닐시 0 출력
# 이때 정점을 탐색하는 순서를 입력된 방문순서로 정렬하는것이 중요하다

import sys
input = sys.stdin.readline


def dfs(now):
    global count
    if now != lst[count]:  # 입력된 방문순서의 정점과 현재 정점이 다른 경우
        print(0)  # 0을 출력하고 종료한다
        exit(0)

    for i in range(len(graph[now])):  # DFS 계속 진행
        next = graph[now][i]
        if visited[next] == 0:
            visited[next] = 1
            count += 1
            dfs(next)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):  # 트리 형태로 그래프를 입력받는다
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

lst = list(map(int, input().split()))
order = [0]*(n+1)
for i in range(n):  # 방문 순서를 나타내는 order 리스트
    order[lst[i]] = i+1

for i in range(1, n+1):  # 입력된 방문 순서에 따라 그래프를 정렬함
    graph[i].sort(key=lambda x: order[x])

visited = [0]*(n+1)
visited[1] = 1
count = 0
dfs(1)

print(1)
