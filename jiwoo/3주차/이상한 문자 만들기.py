def solution(s):
    a = s.split(' ')           # 공백을 기준으로 문자열 쪼개기
    for k in range(len(a)):    
        a_word = list(a[k])    # 각각의 단어들 리스트로 만들기

        for i in range(len(a_word)):
            if i % 2 == 0:
                a_word[i] = a_word[i].upper()  # 짝수번째 대문자로 변경
            else:
                a_word[i] = a_word[i].lower()  # 홀수번째는 소문자 그대로
        a[k] = "".join(a_word)         # a_word의 단어 합치기
        
    return " ".join(a)   # 문자열 합쳐서 return