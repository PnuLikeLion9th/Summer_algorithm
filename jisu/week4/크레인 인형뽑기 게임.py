def solution(board, moves):
    answer = 0
    stack = []  # 인형들 담을 바구니

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:  # 인형이 있다면
                tmp = board[i][move-1]  # tmp 변수에 잠시 담아둔다
                board[i][move-1] = 0  # 인형을 집어 올렸으니 원래 인형이 있던 자리는 비게 됨

                # 바구니에 인형이 1개 이상있으면서 집어 올린 인형이 바구니의 맨 위에 있는 인형과 같다면
                if len(stack) > 0 and tmp == stack[-1]:
                    stack.pop()  # 바구니 맨 위의 인형 없애줌
                    answer += 2
                else:
                    stack.append(tmp)  # 집어 올린 인형과 바구니의 맨 위 인형과 같지않다면 바구니에 추가!!
                break  # 현재 for이 열 끝까지 탐색하므로 하나씩 탐색하게 해주기 위해 break 추가
    return answer
