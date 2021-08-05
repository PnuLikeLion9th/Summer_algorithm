import sys
sys.stdin = open("input.txt","r")   #입력 예시 담긴 input.txt 가져오기

from collections import deque

n, m, v = map(int, input().split())

#숫자들의 연결 확인을 위해 행렬 리스트 생성
#정점의 번호(1부터 시작)와 리스트의 인덱스를 맞추기 위해 n+1 X n+1
graph = [[0] * (n + 1) for _ in range(n + 1)] 

for i in range(m):  #간선의 개수만큼 반복
    a,b = map(int,input().split())  #간선이 연결하는 두 노드 번호 a,b
    graph[a][b]=graph[b][a]=1   #연결된 경우 1입력(간선은 양방향) 

def dfs(start, visited):    #깊이 우선 탐색 dfs(시작노드, 방문 처리)
    visited += [start]  #시작 노드 방문 처리
    for c in range(len(graph[start])):
        if graph[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited  

def bfs(start): #너비 우선 탐색 bfs(시작노드)
    visited = [start]   #방문 처리
    queue = deque()
    queue.append(start) #시작 노드 큐에 삽입

    while queue:    #큐에 남은것이 없을 때 까지 반복
        v = queue.popleft() #큐에서 노드 꺼내기
        for c in range(len(graph[start])):
            if graph[v][c] == 1 and (c not in visited):
                queue.append(c) #방문하지 않은 노드를 큐에 넣고
                visited.append(c)   #방문처리
    return visited

print(*dfs(v,[]))
print(*bfs(v))

