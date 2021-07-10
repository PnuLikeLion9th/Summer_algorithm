def solution(s):
    result = []
    for s in s.split(' '):  #띄어쓰기를 기준으로 문자를 나눠주고
        st = ''
        for i in range(len(s)):  
            if i % 2 == 0:  #짝수번째라면 대문자, 홀수번째라면 소문자
                st += s[i].upper()  #그 결과를 st에 붙여주고
            else :
                st += s[i].lower()
        result.append(st)  #변형시킨 st들을 result에 리스트로 붙여주고
    return ' '.join(result)  #띄어쓰기를 기준으로 다시 문자를 붙여주기