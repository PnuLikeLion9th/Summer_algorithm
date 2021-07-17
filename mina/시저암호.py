#시저암호 가보자가보자

#문자랑 아스키코드 변환하는 함수!!
#chr() 문자를 아스키코드로 
#ord() 아스키코드를 문자로 

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) #영어 알파벳이 26개니까 !! 대문자일 때
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) #이건 소문자일 때
 
    return "".join(s)
 