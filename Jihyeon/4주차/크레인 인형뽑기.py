def solution(board, moves) :
    container=[-1]                                      # '바구니' : 이전에 담겨진 인형값과 같은지 확인하기 위한 리스트/ -1을 넣어야 오류x
    answer=0
    for i in moves :
        for j in range(len(board)):                     # 몇번째 열을 탐색할지 결정하기 위해 해당 열을 모두 탐색하도록
            if board[j][i-1]!=0:                        
                if board[j][i-1]!=container[-1]:        # container의 맨 마지막 값과 새로 탐색된 인형값이 같지 않은 경우
                    container.append(board[j][i-1])     # contaioner에 넣어 나중에 비교할 수 있게 함
                    board[j][i-1]=0                     # board는 0으로
                    break
                elif board[j][i-1]==container[-1]:      # container의 맨 마지막 값과 새로 탐색된 인형값이 같은 경우
                    board[j][i-1]=0
                    container.pop()                     # 마지막 인형 빼기
                    answer+=2                           # 2개의 인형이 사라지기 때문에 answer+=2 사용
                    break
        return answer




        # 살짝이해붉ㄱ가ㅏㄱ