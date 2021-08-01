a = int(input())    # 컴퓨터의 수 입력받기
b = int(input())    # 연결되어 있는 컴퓨터 쌍의 수 입력받기
matrix = [[0]*(a+1) for i in range(a+1)]

for i in range(b):
    x,y = map(int,input().split())   # 연결되어 있는 컴퓨터의 번호 쌍 입력받기
    matrix[x][y] = matrix[y][x] = 1  # 연결되어 있는 값 1로 변경
visit_list = [0] * (a+1)
num = []      # 바이러스 걸린 컴퓨터의 수 

def dfs(V):   # dfs 방법으로 탐색
    visit_list[V] = 1
    for i in range(1,a+1):
        if visit_list[i] == 0 and matrix[V][i] == 1 :
            num.append(1)
            dfs(i)

dfs(1)
print(sum(num))  # num에 담긴 컴퓨터의 수 모두 합해서 print