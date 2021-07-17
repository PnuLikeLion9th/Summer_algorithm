def solution(board, moves):
    basket = []   
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:              # 뽑으려는 위치의 값이 0이 아닐때만!
                basket.append(board[j][i-1])   # basket에 뽑은 숫자 추가하기                    
                
                if len(basket) > 1:                 # basket에 2개 이상의 값이 있을 경우
                    if basket[-2] == basket[-1]:    # basket의 마지막 값과 그 전 값이 같다면,
                        del basket[-1]              # 중복되는 값 삭제
                        del basket[-1]  
                        answer += 2                 # 제거한 값(터진 인형의 수) 개수 추가

                board[j][i-1] = 0        # 뽑아서 basket으로 옮겼으므로 기존 board의 값은 0으로 변경
                break

    return answer