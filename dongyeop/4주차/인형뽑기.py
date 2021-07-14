def solution(board, moves): #뽑으면 바로 일단 스택에 넣고 비교
    stackbox = []
    answer = 0
    for i in moves:
        for j in board:
            if j[i-1] == 0:
                pass
            else:
                stackbox.append(j[i-1])
                j[i-1] = 0
                if len(stackbox) >=2 and stackbox[-1] == stackbox[-2]:
                    del stackbox[-2:]
                    answer += 2
                break

    return answer

def solution(board,moves):#뽑고 나서 바로 비교
    selected = []
    answer =0
    for i in moves:
        poped = 0
        for j in range(len(board)):
            if board[j][i-1] != 0:
                poped= board[j][i-1]
                board[j][i-1] = 0
                break
        if poped != 0:          
            if selected:
                if selected[-1] == poped:
                    answer+=1
                    selected.pop()
                else:
                    selected.append(poped)
            else:
                selected.append(poped)
    
    return answer*2