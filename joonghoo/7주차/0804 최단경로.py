# 백준_1753_최단경로_다익스트라_골드 5
# 다익스트라 알고리즘의 기본문제
# 우선순위 큐를 사용하여 문제를 풀면된다.

import sys
import heapq
input = sys.stdin.readline
INF_num = sys.maxsize  # 경로가 없음을 나타내는 INF 값

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 출발하는 정점을 제외한 거리들을 INF값으로 초기화 한다.
dist = [INF_num]*(v+1)
dist[k] = 0

# 우선순위 큐에 거리와 시작점을 담아준다.
heap = []
heapq.heappush(heap, (0, k))
while heap:
    now_d, now_v = heapq.heappop(heap)  # 출발점에서의 거리와 현재의 정점을 초기화 한다

    # 다음 정점(next_v)과 현재 정점에서 다음 정점까지의 거리(next_d)를 불러온다
    for next_v, next_d in graph[now_v]:
        # 최단 경로를 구해야 하므로 기존의 거리보다 작을 경우 작은 거리를 갱신한다.
        if dist[next_v] > now_d + next_d:
            dist[next_v] = now_d + next_d
            heapq.heappush(heap, (dist[next_v], next_v))

for i in range(1, v+1):
    if dist[i] == INF_num:  # 해당 정점으로 가는 경로가 없을 경우 INF 출력
        print('INF')
    else:  # 경로가 있을 경우 최단경로를 출력한다.
        print(dist[i])
