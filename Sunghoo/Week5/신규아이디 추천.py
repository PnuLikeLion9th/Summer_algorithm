# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

from collections import deque
import re


def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    second = ''
    for l in new_id:
        if l.isdigit() or l.isalpha() or l in ['-', '_', '.']:
            second += l

    # 3단계
    while True:
        if '..' in second:
            second = second.replace('..', '.')
        else:
            break

    # 4단계
    second = deque(second)
    if second[0] == '.':
        second.popleft()

    if second and second[-1] == '.':
        second.pop()

    # 5단계
    if not second:
        second = 'a'

    # 6단계
    second = list(second)
    if len(second) >= 16:
        second = second[0:15]
        if second[-1] == '.':
            second = second[0:14]

    # 7단계
    while len(second) <= 2:
        second += second[-1]

    return ''.join(second)


new_id = "...!@BaT#*..y.abcdefghijklm"


def solution2(new_id):

    # 1 : 소문자 치환
    new_id = new_id.lower()

    # 2 : 특정 문자 외 제거
    answer = re.sub('[^a-z\d\-\_\.]', '', new_id)

    # 3 : 마침표 2번 연속은 하나로 치환
    answer = re.sub('\.\.+', '.', answer)

    # 4 : 양 끝 마침표 제거
    answer = re.sub('^\.|\.$', '', answer)

    # 5 : 빈 문자열일 경우 'a' 추가
    if not answer:
        answer = 'a'

    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])

    # 7단계 : 길이가 3이 될 때까지 반복해서 끝에 붙이기
    while len(answer) < 3:
        answer += answer[-1]

    return answer


print(solution2(new_id))

# 3,4,5, 11, 15
