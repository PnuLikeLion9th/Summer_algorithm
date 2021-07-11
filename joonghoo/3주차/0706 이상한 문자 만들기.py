# 프로그래머스_이상한 문자 만들기_문자열_레벨 1
# 공백을 기준으로 짝수, 홀수를 판단해야 하므로 공백이 올때마다 count=0 해준다
# 짝수번째 알파벳은 upper함수를 이용해서 대문자로, 홀수번째 알파벳은 lower을 이용해서 소문자로 변환한다.

def solution(s):
    answer = ''
    count = 0
    for i in s:
        if i == ' ':  # 공백이 오면 count = 0 으로 초기화
            answer += ' '
            count = 0
            continue

        if count % 2 == 0:  # 짝수일경우 대문자로 변환
            answer += i.upper()
        else:  # 홀수일경우 소문자로 변환
            answer += i.lower()
        count += 1

    return answer
