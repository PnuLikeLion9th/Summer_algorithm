def solution(board, moves):
    N=len(board)    #NxN board
    cab=[-1]          #담을 바구니
    answer=0
    for i in moves:     #moves 하나씩 꺼내서 실행. i=int값
        for j in range(N):
            pa=board[j]
            if pa[i-1] != 0:
                if pa[i-1]!=cab[-1]:
                    cab.append(pa[i-1])
                    pa[i-1]=0
                    break
                elif pa[i-1]==pa[-1]:
                    pa[i-1]=0
                    cab.pop()
                    answer+=2
                    break
        return answer


                