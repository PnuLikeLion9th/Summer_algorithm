def solution(board, moves):
    answer = 0

    stack = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:  # 인형위치 확인
                if len(stack) > 0 and stack[-1] == board[j][i-1]:  # 터트리기 위한 확인
                    board[j][i-1] = 0
                    answer = answer + 2
                    stack.pop()
                else:  # 터트릴게 없다면
                    stack.append(board[j][i-1])
                    board[j][i-1] = 0
                break

    return answer
