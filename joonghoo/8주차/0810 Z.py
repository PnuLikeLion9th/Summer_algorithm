# 백준_1074_Z_분할 정복_실버 1
# 정사각형 모양의 좌표를 4분면으로 분할한다는 점이 쿼드트리 문제와 비슷하다
# 하지만 시간제한이 0.5초라서 모든 좌표를 탐색하면 시간초과가 나온다
# 따라서 입력 받은 행과 열로 해당 좌표의 값을 뽑아 내야한다

def Z(m, size):
    global cnt, r, c
    # 한변의 길이가 2인 정사각형까지 분할 했을 경우 좌표의 위치에 따라 1,2,3을 더해준다
    if m == 1:
        if r == 0 and c == 0:
            print(cnt)
        elif r == 0 and c == 1:
            print(cnt+1)
        elif r == 1 and c == 0:
            print(cnt+2)
        elif r == 1 and c == 1:
            print(cnt+3)
        return
    # 분할을 해야 하는 경우 size보다 큰 행이나 열이 있을 경우 -size 해준다
    # 현재 해당하는 정사각형의 길이에 따라 알맞은 왼쪽위 꼭짓점의 좌표값을 cnt에 저장한다
    else:
        if r < size and c < size:
            pass
        elif r < size and c >= size:
            c -= size
            cnt += 4**(m-1)
        elif r >= size and c < size:
            r -= size
            cnt += 4**(m-1)*2
        elif r >= size and c >= size:
            r -= size
            c -= size
            cnt += 4**(m-1)*3
        Z(m-1, size//2)


n, r, c = map(int, input().split())
cnt = 0
# 정사각형의 한변의 길이가 2**n이기 때문에 중간좌표에 해당하는 size값은 2를 나눠주면 된다!
Z(n, 2**(n-1))
