def solution(s):
    result = []
    for s in s.split(' '):              # 띄어쓰기를 기준으로 문자 분리하기
        st = ''
        for i in range(len(s)):         
            if i % 2 == 0:              # 짝수번째면 대문자, 홀수번째면 소문자
                st += s[i].upper()      # st라는 새 공간에
            else :
                st += s[i].lower()
        result.append(st)               # 변형시킨 st들을 result에 리스트로
    return ' '.join(result)             # 띄어쓰기를 기준으로 다시 문자 붙이기