def solution(s):
    l = s.split(' ')
    a = []  #새로운 문자를 만들 리스트
    for i in l:
        for j in range(len(i)):
            if j % 2 == 1:    #홀수 자리인 경우(대->소)  
                a.append(i[j].lower())
            else:             #짝수 자리인 경우(소->대)
                a.append(i[j].upper())
        a.append(' ')   #단어 단위로 띄어쓰기
    return (''.join(a[:-1])) #마지막 띄어쓰기 제외하고 문자열로 변환
    