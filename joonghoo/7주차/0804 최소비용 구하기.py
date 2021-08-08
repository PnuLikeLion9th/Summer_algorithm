# 백준_1916_최소비용 구하기_다익스트라_골드 5
# 백준_1753_최단경로 문제에서 시작점과 도착점이 정해진 문제이다.
# 다익스트라 알고리즘의 기본문제
# 우선순위 큐를 사용하여 문제를 풀면된다.

import sys
import heapq
input = sys.stdin.readline
INF_num = sys.maxsize  # 경로가 없음을 나타내는 INF 값

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

# 출발하는 정점을 제외한 비용들을 INF값으로 초기화 한다.
dist = [INF_num]*(n+1)
dist[start] = 0

# 우선순위 큐에 비용과 시작점을 담아준다.
heap = []
heapq.heappush(heap, (0, start))
while heap:
    now_cost, now_v = heapq.heappop(heap)  # 출발점에서의 비용과 현재의 정점을 초기화 한다

    if dist[now_v] < now_cost:
        continue

    # 다음 정점(next_v)과 현재 정점에서 다음 정점까지의 비용(next_cost)을 불러온다
    for next_v, next_cost in graph[now_v]:
        # 최단 경로를 구해야 하므로 기존의 비용보다 작을 경우 작은 비용을 갱신한다.
        if dist[next_v] > now_cost + next_cost:
            dist[next_v] = now_cost + next_cost
            heapq.heappush(heap, (dist[next_v], next_v))

# 도착점까지의 비용을 출력한다.
print(dist[end])
