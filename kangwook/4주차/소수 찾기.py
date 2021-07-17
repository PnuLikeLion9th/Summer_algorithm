def solution(numbers):
	# 2부터 n까지의 숫자 배열 만들기
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num: # 배수 제거
            num = num - set(range(i*2, n+1, i))

    answer = len(num)

    return answer