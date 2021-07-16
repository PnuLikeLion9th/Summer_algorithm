def solution(s,n):
    answer = ''
    for i in s:
        if i.isalpha():#알파벳이면
            if i.islower():#소문자이면
                if ord(i)+n>122:#n만큼 밀렸을때 아스키코드값이 122보다 크면
                    answer+=chr(ord(i)+n-26)#한바퀴 돌아줌
                else:
                    answer+=chr(ord(i)+n)#아니면 그냥 n만큼 밀어줌
            elif i.isupper():#대문자이면
                if ord(i)+n>90:#소문자일떄와 똑같음
                    answer+=chr(ord(i)+n-26)
                else:
                    answer+=chr(ord(i)+n)
        else:#알파벳이 아니면 공백
            answer+=" "
    return answer
