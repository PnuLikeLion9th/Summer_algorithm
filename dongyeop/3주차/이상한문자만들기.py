def solution(s):
    a = s.split(' ')#공백 기준으로 쪼개기
    answerl = list()
    for i in range(len(a)):
        answer=""
        count = 1#몇번째 알파벳인지 세는용도
        for j in a[i]:
            if count%2!=0:#카운트가 1,3,5,7이면 대문자
                answer+=j.upper()
                count+=1
            else:#나머지는 소문자
                answer+=j.lower()
                count+=1
        answerl.append(answer)#정답 리스트에 더해줌
    return ' '.join(answerl)#요소들 사이에 공백을 넣어 문자열로 반환