# 백준_2606_바이러스_BFS_실버 3
# bfs를 사용하여 정점을 탐색하여 1과 연결되지 않은 정점의 갯수를 출력하는 문제

from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):  # bfs 함수 실행
    dq = deque()
    visit[v] = 1
    dq.append(v)
    count = -1
    while dq:
        v = dq.popleft()
        count += 1
        for i in range(1, n+1):
            if visit[i] == 0 and tree[v][i] == 1:  # 방문 하지않았고, 다음 정점으로 가는 노드가 있을 경우 다음 정점 방문
                dq.append(i)
                visit[i] = 1
    print(count)


n = int(input())

tree = [[0]*(n+1) for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for i in range(int(input())):
    x, y = map(int, input().split())
    tree[x][y] = 1
    tree[y][x] = 1
bfs(1)
