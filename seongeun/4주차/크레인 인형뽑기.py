# 크레인 인형뽑기
def solution(board, moves):
    basket = []  # 바구니에 속한 인형 리스트 미리 만들기
    n = len(board[0])
    answer = 0
    
    for m in moves:
        m -= 1        # board의 (move - 1)열에 대해 모든 행 순회
        for i in range(n): # board[i][m]에 인형이 있을 때,
            if board[i][m] != 0:   # 바구니가 비어있지 않고, 현재 집은 인형과 바구니 가장 위쪽의 인형이 같으면 두 인형 제거
                if basket and basket[-1] == board[i][m]:
                    basket.pop()
                    answer += 2
                else:   # 그렇지 않은 경우, 현재 집은 인형을 바구니에 추가
                    basket.append(board[i][m])
                    
                board[i][m] = 0  # 집은 인형 게임 화면에서 제거
                break
    
    return answer
