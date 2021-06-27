import re  # 정규식 사용. 정규식 라이브러리 re 불러옴


def solution(s):
    if len(s) == 4 or len(s) == 6:  # 주어진 문자열의 길이가 4 또는 6이면서
        if re.findall('[\D]', s):  # 문자열이 0~9 이외의 문자를 포함하고 있다면
            return False  # False 반환
        return True  # True 반환 (문자열의 길이가 4 or 6인 경우)
    return False  # False 반환 (문자열의 길이가 4 or 6이 아닌 경우)
