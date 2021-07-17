def solution(board, moves):
    l = []  #인형이 들어갈 바구니 리스트
    res = []    #사라진 인형이 들어갈 리스트
    for i in moves:
        n = 0
        while board[n][i-1] == 0:  
            n += 1
            if n == len(board)-1:   #리스트 길이를 넘어가면 break
                break
        if board[n][i-1] != 0:  #l에 0이 들어가지 않도록 if문 사용
            l.append(board[n][i-1])
            board[n][i-1] = 0
            if len(l)>=2:
                if l[-1] == l[-2]:  #연속으로 같은 인형이 들어왔을때
                    res.append(l[-2:])
                    del l[-2:]
    return len(res)*2