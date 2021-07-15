# 백준_16947_서울 지하철 2호선_DFS_골드 3
# dfs로 그래프를 탐색하며 해당 좌표가 순환선인지 지선인지 구분한다.
# 구분한 list를 통해 해당 좌표에서 순환선까지의 길이를 dfs로 구한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(now_idx, cnt, start):
    global flag
    for i in range(len(graph[now_idx])):
        next_idx = graph[now_idx][i]  # 다음 탐색할 좌표
        if visited[next_idx] == 0:  # 다음 탐색할 좌표를 방문하지 않았다면 dfs 실행
            visited[next_idx] = 1
            dfs(next_idx, cnt+1, start)

            if flag:  # 순환선일경우 0, 지선일경우 1
                check[now_idx] = 0
                return

        else:
            if cnt >= 3 and next_idx == start:  # 조건만족시 dfs 종료하는 flag = 1
                flag = 1
                check[now_idx] = 0
                return


def sum_distance(now_idx, distance):
    for i in range(len(graph[now_idx])):
        next_idx = graph[now_idx][i]  # 다음 탐색할 좌표

        if visited[next_idx] != 0:  # 탐색했던 좌표일경우 continue
            continue

        if check[next_idx] == 0:  # 다음 탐색할 좌표가 순환선 일경우 시작했던 좌표부터 순환선까지 거리 출력
            print(distance, end=' ')
            return
        else:  # 다음 좌표도 지선일경우 거리 + 1 하고 계속 탐색
            visited[next_idx] = 1
            sum_distance(next_idx, distance+1)


n = int(input())
graph = [[] for _ in range(n+1)]
check = [1]*(n+1)
for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

flag = 0
for i in range(1, n+1):
    visited = [0]*(n+1)  # 시작하는 좌표값을 다르게 탐색해 봐야하므로 dfs시작할때마다 초기화
    visited[i] = 1
    dfs(i, 1, i)
    if flag:  # 순환선 발견시 반복문 종료
        break

for i in range(1, n+1):
    if check[i] == 0:  # 해당좌표가 순환선 일경우 0 출력
        print(0, end=' ')
    else:  # 지선이라면 순환선까지 탐색하는 dfs 실행
        visited = [0]*(n+1)
        visited[i] = 1
        sum_distance(i, 1)
