def solution(s,n):
    a = list(s)
    for i in range(len(a)):

        if a[i].isalpha():                      # a[i]가 알파벳인 경우
            if a[i].islower():                  # a[i]가 소문자인 경우 (대소문자 구분해서 풀어야 함!!!)
                a[i] = chr(ord("a") + ((ord(a[i]) - ord("a") + n) % 26))   # 아스키 코드 이용해 n만큼 밀어서 암호화시킴
            else:
                a[i] = chr(ord("A") + ((ord(a[i]) - ord("A") + n) % 26))   
        else:                                   # 알파벳이 아닐 경우 (공백일 경우) 그대로
            pass

    return "".join(a)   # 문자열로 합쳐서 return