# 백준_16940_BFS 스페셜 저지_BFS_골드 4
# DFS 스페셜 저지에서 탐색 방법을 BFS로 바꿔주기만 하면 되는 문제
# 입력된 그래프를 BFS로 탐색할때 입력된 순서로 탐색할 경우 1 출력, 아닐시 0 출력
# 이때 정점을 탐색하는 순서를 입력된 방문순서로 정렬하는것이 중요하다

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

lst = list(map(int, input().split()))
order = [0]*(n+1)
for i in range(n):
    order[lst[i]] = i + 1

for i in range(1, n+1):  # 입력된 방문 순서에 따라 그래프를 정렬함
    graph[i].sort(key=lambda x: order[x])

visited = [0]*(n+1)
visited[1] = 1
result = []
move = deque([1])
while move:  # BFS 진행
    now = move.popleft()
    result.append(now)

    for i in range(len(graph[now])):
        next = graph[now][i]
        if visited[next] == 0:
            visited[next] = 1
            move.append(next)

if lst == result:  # 탐색순서와 문제에서 입력된 방문순서와 같을 경우 1 출력, 아닐 경우 0 출력
    print(1)
else:
    print(0)
