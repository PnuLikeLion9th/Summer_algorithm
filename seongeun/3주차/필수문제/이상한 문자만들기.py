#이상한 문자만들기
'''전략- 일단 받은 문자 공백을 기준으로 잘라서 새로운 리스트로 만든다음에 첫 단어부터 하나씩 대문자 혹은 소문자로 바꿔줌
그다음에 새로운 리스트에 담아서 마지막에 합치기 '''


def solution(s):    
    a = s.split(" ")    #공백을 기준으로 문자열 나눔- 리스트로 바꿔짐
    b = list()          #대문자 혹은 소문자로 변환된 각 문자열을 새로 담아줄 리스트 만들어줌
    for i in range(len(a)): #리스트 안의 단어들 각각 하나씩 넣어줌 마지막 단어까지 반복
        answer = ""         #새로 바뀐 단어들 여기로 넣어주기
        for j in range(len(a[i])) : #각 단어의 첫번째 문자부터 마지막 문자까지 반복 
            if j % 2 == 0 :         #문자 위치가 짝수열이면
                answer += a[i][j].upper() #대문자로 바꿈
            else :                    #아니면
                answer += a[i][j].lower() #소문자로 바꿈
        b.append(answer)      #바뀐 단어 list에 넣어줌 
        
    return " ".join(b)     #" ".join()-list안에 요소들 합쳐줌

    # s.split( )와 s.split(" ") 차이점을 모르겠음,,