def solution(s, n):
    s = list(s)  # 문자열을 쪼개서 하나씩 아스키코드로 변환해야 하므로 리스트로 변환
    for i in range(len(s)):
        if s[i].isupper():  # 대문자라면
            s[i] = chr((ord(s[i])-ord('A')+n) %
                       26+ord('A'))  # z 또는 Z 범위 넘어서면 안되므로 %26
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n) % 26+ord('a'))
    return "".join(s)
