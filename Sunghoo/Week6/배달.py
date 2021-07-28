# 이 방법이 빠르긴하다.

import heapq


def solution(N, road, K):

    # 어차피 1번 노드를 기준으로 거리를 측정하는 것이 결과가 된다.
    distance = [float('inf')] * (N + 1)

    # road 매개변수에서 각 노드별 인접 노드 간 거리를 알 수 있게 됐다.
    adj = [[] for _ in range(N + 1)]

    for r in road:
        adj[r[0]].append([r[2], r[1]])
        adj[r[1]].append([r[2], r[0]])

    distance[1] = 0
    heap = []
    heapq.heappush(heap, [0, 1])
    while heap:

        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if distance[n] > cost + c:
                distance[n] = cost + c
                heapq.heappush(heap, [distance[n], n])
    return len([i for i in distance if i <= K])
#
#
# # 굳이 r[2] 를 0번째에 넣은 이유는 heapq를 사용하기 위함
# # append() 인자에 2개 넣었을 때 에러 안잡아주는거 킹받네, 킹스크립트는 바로 에러 띄우는데


# 다른 풀이
# from collections import deque


# def solution(N, road, K):
#     nodes = {}
#     dist = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}
#     for n1, n2, distance in road:
#         nodes[n1] = nodes.get(n1, []) + [(n2, distance)]
#         nodes[n2] = nodes.get(n2, []) + [(n1, distance)]
#     que = deque([1])
#     while que:
#         cur_node = que.popleft()
#         for nxt_node, d in nodes[cur_node]:
#             if dist[nxt_node] > dist[cur_node] + d:
#                 dist[nxt_node] = dist[cur_node] + d
#                 que.append(nxt_node)
#     return len([i for i in dist.values() if i <= K])

from collections import deque


def solution(N, road, K):
    adjacent = dict()
    distance = {i: float('inf') if i != 1 else 0 for i in range(1, N + 1)}
    for n1, n2, d in road:
        adjacent[n1] = adjacent.get(n1, []) + [(n2, d)]
        adjacent[n2] = adjacent.get(n2, []) + [(n1, d)]

    que = deque([1])
    while que:
        cur_node = que.popleft()
        for n2, d in adjacent[cur_node]:
            if distance[n2] > distance[cur_node] + d:
                distance[n2] = distance[cur_node] + d
                que.append(n2)  # 이 코드에 자신있나? 왜이렇게 되는지

    return len([i for i in distance.values() if i <= K])  # 여기서도 dict.values() 가 아니라 dict 를 for 문 돌려서 실수함










# dict.get("new_key", "default_key") => 2번째 인자는 기존 키 값이 존재하지 않을 때, 대신 들어간다.
# # 하나의 노드를 기준으로, 상대 노드간의 거리를 배열로 정리한다. 초깃값은 infinity
# # 우리는 K 보다 작은 거리만 고르면 되기 때문에 이를 기준으로 분기한다.
# #
#
N, K = 5, 3
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
print(solution(N, road, K))