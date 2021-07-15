# 프로그래머스_크레인 인형뽑기 게임_스택_레벨 1
# 첫 번째 시도에서 stack에 인형을 다 담고 같은 인형들을 한번에 제거하는 방법 사용했으나, 런타임 에러
# 두 번째 시도에서 stack에 인형을 하나 담을때 마다 앞뒤로 같은 인형들을 제거하는 방법 사용해서 성공!

def solution(board, moves):
    count = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:  # moves 원소의 값을 x 좌표로 잡고, y 좌표 0부터 증가시킨다.
                stack.append(board[j][i-1])  # 인형이 존재할 경우 stack에 append
                board[j][i-1] = 0  # 해당 좌표에 0을 대입하여 비어있는 공간으로 만들어준다.
                break
        # stack의 길이가 2 이상이고, 마지막 2개의 값이 같으면 pop을 해주고 count += 1
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            count += 1

    return count*2  # 인형의 개수는 2배 많으므로 *2 해준다
