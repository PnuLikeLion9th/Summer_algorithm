# 숫자문자열과 영단어
'''매개변수 s에 zero부터 nine을 찾아서 문자형태인 숫자로 바꿔준다음에 마지막에 숫자형태로 return'''

def solution(s):
    english = ['zero','one','two','three','four','five','six','seven','eight','nine']
    number = ['0','1','2','3','4','5','6','7','8','9']
   #영어랑 숫자 리스트 각각 만들어줌
    for i in range(10) : #0부터 9까지 숫자 대입
        if (english[i] in s) : #zero부터 nine까지 문자 있으면 
            s = s.replace(english[i],number[i]) # 그 문자 number로 바꿔줌
    return int(s) #숫자형으로 보내야되서 int
    