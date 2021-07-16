# 백준_1707_이분 그래프_DFS_골드 4
# 이분 그래프 ==> 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로 표현한 그래프
# 처음 탐색시 현재 인접한 정점의 색을 현재 정점의 색과 다른색으로 칠한다
# 두번째 탐색시 현재 인접한 정점과 현재 정점의 색이 같을 경우 NO를 출력, 조건 만족하는 이분그래프 일경우 YES 출력

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(now):  # 첫 번째 탐색 함수, 그래프에 색을 칠해준다.
    for i in range(len(graph[now])):
        next = graph[now][i]
        if color[next] == 0:
            if color[now] == 1:  # 인접한 정점의 색과 현재 정점의 색을 다르게 칠함
                color[next] = 2
            elif color[now] == 2:
                color[next] = 1
            dfs(next)


def solution(now):  # 두번째 탐색 함수, 이분 그래프인지 판별한다.
    global flag
    for i in range(len(graph[now])):
        next = graph[now][i]

        if color[next] == color[now]:  # 현재의 정점과 인접한 정점의 색이 같은 경우
            flag = 1
            return

        if visited[next] == 0:  # 서로 색이 다른경우 계속 DFS 진행
            visited[next] = 1
            solution(next)

        if flag:
            return


for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    color = [0]*(v+1)  # 정점의 색을 나타내는 list
    visited = [0]*(v+1)  # 정점의 방문여부를 나타내는 list

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, v+1):  # 첫 번쨰 탐색, 모든 그래프에 색을 넣어준다
        if color[i] == 0:
            color[i] = 1
            dfs(i)

    flag = 0  # flag 변수를 통해서 이분 그래프가 아닐 경우 바로 탐색을 종료한다
    for i in range(1, v+1):  # 그래프를 탐색해서 이분 그래프인지 판별한다.
        if visited[i] == 0:
            visited[i] = 1
            solution(i)

        if flag:
            break

    if flag:  # 이분 그래프 일때 YES, 아닐떄 NO 출력
        print("NO")
    else:
        print("YES")
