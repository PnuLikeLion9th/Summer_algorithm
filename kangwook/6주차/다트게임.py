def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10','k')   #10 처리하는 방법 : str의 replace를 사용
    point = ['10' if i == 'k' else i for i in dartResult]   #다시 다른 리스트에 담아준다

    i = -1  #answer에서 인덱스를 for문 안에서 다루기 위한 코드
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)