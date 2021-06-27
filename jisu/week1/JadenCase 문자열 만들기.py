import re  # 정규식 사용. 정규식 라이브러리 re 불러옴


def solution(s):
    answer = s[0:].lower()  # answer에 s를 소문자로 변환하여 복사
    # 단어의 첫 부분이 소문자( /^[a-z] ) OR(|) 공백 뒤에 소문자( \s[a-z]/g )를
    for i in re.findall('^[a-z]|\s[a-z]', answer):
        answer = answer.replace(i, i.upper(), 1)  # 대문자로 변환

    return answer
