# 백준_1992_쿼드트리_분할 정복_실버 1
# 한변의 길이가 n인 정사각형 좌표를 4분면으로 분할하여 탐색하는 문제이다
# 한번 분할할때 괄호를 열고 해당 사분면의 분할이 종료될 경우 괄호를 다시 닫으면 된다

import sys
input = sys.stdin.readline


# 현재 탐색하는 정사각형의 변의길이가 m이고 좌표는 x,y인 재귀함수
# 이떄 좌표 x,y는 탐색하는 정사각형의 왼쪽위 꼭짓점 값이다
def solution(m, x, y):
    # 현재 정사각형의 왼쪽위 꼭짓점의 색을 변수로 빼준다
    color = maps[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            # 정사각형의 다른 좌표를 탐색하다가 왼쪽위 꼭짓점의 색과 다른 좌표가 나올경우 다시 분할 정복 해준다
            if color != maps[i][j]:
                print('(', end='')
                solution(m//2, x, y)
                solution(m//2, x, y+m//2)
                solution(m//2, x+m//2, y)
                solution(m//2, x+m//2, y+m//2)
                print(')', end='')
                return

    # 현재 정사각형의 모든 좌표가 같은 색이라면 해당 color를 출력한다
    if color == '0':
        print('0', end='')
    else:
        print('1', end='')


n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))

solution(n, 0, 0)
