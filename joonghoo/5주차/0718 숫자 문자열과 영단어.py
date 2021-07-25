# 프로그래머스_숫자 문자열과 영단어_문자열_레벨 1
# isdecimal 함수를 이용해서 문자열의 원소가 정수인지 판별
# 정수라면 바로 result에 더하고, 정수가 아니라면 해당 문자가 나타내는 숫자를 딕셔너리로 불러와서 result에 더해줌

def solution(s):
    result = ""
    num = ""
    nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}  # 정수를 나타내는 문자를 딕셔너리에 저장해줌
    for i in s:
        if i.isdecimal():  # 해당 문자가 정수인지 판별하는 isdecimal 함수 사용
            result += i
        else:
            num += i
            if num in nums:
                result += nums[num]  # 딕셔너리로 해당하는 숫자를 불러온다
                num = ""
    return int(result)


s = 'one4seveneight'
print(solution(s))
