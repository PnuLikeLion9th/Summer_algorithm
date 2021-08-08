graph = [
    [], #인덱스랑 번호 맞추기 위해 앞에 빈 리스트 추가
    [2,3],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9 #[False,False,False,False,False,False,False,False,False]

def dfs(graph,v,visited):   #v는 시작 노드
    visited[v] = True   #현재 노드 방문 체크
    print(v,end='') #방문한 순서 적어주는 (출력해주는) 코드. end='' 의미는 줄 띄우는 거 없이 출력한다는 뜻
    for i in graph[v]:  #방문 노드의 인접 노드를 살펴본다
        if not visited[v]:  #인접 노드가 False라면 = 인접 노드에 아직 방문하지 않았다면
            dfs(graph,i,visited)    #이 함수를 재귀적으로 사용해라 = 파고 들어가보자 = 깊이 우선 탐색!