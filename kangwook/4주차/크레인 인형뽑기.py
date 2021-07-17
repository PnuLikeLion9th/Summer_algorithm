def solution(board, moves):
    N=len(board)    #NxN board
    cab=[]          #담을 바구니
    k=0
    answer=0
    for i in moves:     #moves 하나씩 꺼내서 실행. i=int값
        for j in range(0,N+1):
            pa=board[j]
            if pa[i] == 0:
                pass
            else:
                cab.append(pa[i])
                j.replace(pa[i],0)
                break
        k+=1
        if k>=2:
            if cab[k-2] == cab[k-1]:
                answer+=1
                cab.remove(cab[k-2])
                cab.remove(cab[k-1])
        else:
            pass
        return answer


                