def solution(n):
    answer = 0
    while(n > 0):
        answer += n % 10  # 나머지를 구해서 합을 구함 (=각 자릿수의 합)
        n //= 10  # 10으로 나눠줌
    return answer
