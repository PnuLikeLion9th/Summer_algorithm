def solution(n):
    new = str(n)          # n을 문자열로 바꿔서 new에 저장하기
    add = 0
    for i in range(len(new)):        # new의 길이만큼 반복하는 i, 그동안의 n의 i 인덱스 값을 add에 계속 더하기
        add += int(new[i])
    return add