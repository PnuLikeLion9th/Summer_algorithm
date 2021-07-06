def solution(s):
    answer = []
    for word in s.split(' '):
        new_word = ''  # 변환된 단어 저장할 곳(예: TrY)
        for idx, val in enumerate(word):  # 단어별로 짝/홀수 인덱스를 판단
            if idx % 2 == 0:
                new_word += val.upper()
            else:
                new_word += val.lower()
        answer.append(new_word)
    return ' '.join(answer)  # 변환된 단어들 사이에 공백 추가 후 문자열 반환
