def solution(board, moves):
    new_board = []
    count = []
    result = 0

    for i in range(len(board)):
        temp = []
        for j in range(len(board)):
            if board[j][i] != 0:
                temp.append(board[j][i])
        new_board.append(temp[::-1])
    moves = list(map(lambda x: x - 1, moves))

    count.append(new_board[moves[0]].pop())
    del (moves[0])
    for i in moves:
        if new_board[i]:
            pops = new_board[i].pop()
            try:
                if pops == count[-1]:
                    count.pop()
                    result += 1
                else:
                    count.append(pops)
            except:
                count.append(pops)

    return result * 2
