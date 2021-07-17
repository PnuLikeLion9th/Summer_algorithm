def solution(board, moves):
    stacklist=[]
    answer=0
    for m in moves:
        for i in board:
            if i[m-1]!=0:
                stacklist.append(i[m-1])
                i[m-1]=0
                break
            else:
                pass
        if len(stacklist)>=2:
            if stacklist[-1]==stacklist[-2]:
                stacklist.pop()
                stacklist.pop()
                answer+=2
    return answer