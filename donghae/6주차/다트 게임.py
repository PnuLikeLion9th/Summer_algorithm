def solution(dartResult):
    n = ''  #숫자 담을 문자열(0~10)
    score = []  #점수 리스트
    bonus = ['S','D','T'] 
    for i in dartResult:
        if i.isnumeric(): #숫자면 문자열에 i추가(10인 경우 고려)
            n += i
        elif i in bonus: #보너스 계산
            score.append(int(n)**(bonus.index(i)+1))
            n = ''  #n값 초기화
        elif i == '*':  #옵션 *인 경우
            if len(score) > 1:  #길이가 2이상일 때
                score[-1] = score[-1]*2
                score[-2] = score [-2]*2
            else:
                score[-1] = score[-1]*2
        elif i == '#':  #옵션 #인 경우
            score[-1] = score[-1]*(-1)  #점수 마이너스로 변경
    return sum(score)