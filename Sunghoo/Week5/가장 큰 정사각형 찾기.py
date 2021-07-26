def check(dr, dc, N, M):
    if 0 <= dr <= N and 0 <= dc <= M:
        return True


def solution(board):
    max_val = 0
    N = len(board) - 1
    M = len(board[0]) - 1
    indexes = [(idx, jdx) for jdx in range(len(board[0])) for idx in range(len(board))]

    for r, c in indexes:
        if board[r][c] and check(r + 1, c + 1, N, M):
            dr = r + 1
            dc = c + 1
            if board[dr][dc] and board[dr][c] and board[r][dc]:
                board[dr][dc] = min(board[r][c], board[dr][c], board[r][dc]) + 1

    for row in board:
        if max(row) > max_val:
            max_val = max(row)
    return max_val ** 2


# 모범 풀이
def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] += min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j])

    for i in board:
        if answer < max(i): answer = max(i)
    return answer * answer
