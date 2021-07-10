def solution(s):
    s = s.split(' ')    #공백문자 포함
    l = []
    for i in range(len(s)):
        if len(s[i]) >= 1:
            l.append(s[i][0].upper())   #첫 문자를 대문자로 변경
        l.append(s[i][1:].lower()+' ')  #그 외 알파벳을 소문자로 변경
    if l[-1] == ' ':    #마지막에 공백이 있는 경우
        return (''.join(l[:-1]))
    else:
        return ''.join(l).rstrip()