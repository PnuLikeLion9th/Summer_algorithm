def solution(n, lost, reserve):
    i = -1
    length = len(reserve)

#중복 제거
    while i<length:
        i=i+1
        try:
            lost.remove(reserve[i])
            reserve.remove(reserve[i])
            i = i-1
        except:
            print('')


    for i in range(len(reserve)):
        #앞번호 학생 먼저 탐색
        try:
            k = lost.remove(reserve[i]-1)
        except:
            k = -1
        #뒷번호 학생 탐색
        if k == -1:
            try:
                lost.remove(reserve[i]+1)
            except:
                print('')
    return n - len(lost)