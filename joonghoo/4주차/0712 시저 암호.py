# 프로그래머스_시저 암호_문자열_레벨 1
# 문자를 아스키코드로 바꿔서 n만큼 밀수있게 한다

def solution(s, n):
    answer = ""
    for i in range(len(s)):
        ascii_num = ord(s[i]) + n  # 문자열S의 문자를 아스키코드로 바꿔서 n만큼 밀어낸다
        if s[i].isupper():  # 대문자일 경우
            if ascii_num > 90:
                answer += chr(65 + ascii_num % 91)  # Z를 넘어가면 A부터 다시 시작하게 한다
            else:
                answer += chr(ascii_num)
        elif s[i].islower():  # 소문자일 경우
            if ascii_num > 122:
                answer += chr(97 + ascii_num % 123)  # z를 넘어가면 a부터 다시 시작하게 한다
            else:
                answer += chr(ascii_num)
        else:
            answer += s[i]  # 공백일 경우
    return answer


print(solution("a B z", 4))
