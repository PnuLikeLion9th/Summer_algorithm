def solution(s, n):
    s = list(s)
    l = []
    for i in s:
        if i >= 'A' and i <= 'Z':   #알파벳 대소문자 구분
            l.append(chr((ord(i)-ord('A')+ n)%26+ord('A'))) #알파벳 범위를 벗어나지 않도록 %26사용
        elif i >= 'a' and i <= 'z':
             l.append(chr((ord(i)-ord('a')+ n)%26+ord('a')))
        else:   #i가 알파벳이 아닌 공백인 경우
            l.append(' ')
    return ''.join(l)