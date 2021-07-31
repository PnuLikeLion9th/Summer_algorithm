def solution(n, lost, reserve):
    r = set(reserve) - set(lost)    #set으로 바꿔서 리스트의 중복 제거
    l = set(lost) - set(reserve)    
    for i in r: #reserve 내에서 반복
        if i-1 in l:    #최대한 많이 빌려주기 위해 작은쪽 먼저
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)
    return n-len(l) #전체 - 못 빌린 사람