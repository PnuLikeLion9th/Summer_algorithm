def solution(phone_number):
    return (len(phone_number)-4)*'*' + phone_number[-4:]
    # 1. (len(phone_number)-4)*'*' : 주어진 전화번호 뒷 4자리를 제외한 나머지를 *로 바꾼다.
    # 2. 전화번호 뒷 4자리를 주어진 문자열에서 복사해온다.
