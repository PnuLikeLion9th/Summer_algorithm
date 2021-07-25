# 자세한 풀이: https://breathtaking-life.tistory.com/118
def solution(s):
    result = []
    relation = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    arr = []
    for c in s:
        if c in relation.values(): 		# 문자가 0~9일 경우
            result.append(c) 		# 리스트에 바로 추가
        else: 		# 0~9가 아닐경우 변환 과정을 거침
            arr.append(c)
            tmp = ''.join(arr)
            if tmp in relation.keys():
                arr = []
                result.append(relation[tmp])

    return int(''.join(result))


# 다른 풀이
num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)