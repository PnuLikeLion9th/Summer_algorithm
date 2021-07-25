def solution(left, right):
    s = []
    for i in range(left,right+1):
        num = 0                         # num에 약수의 개수 담아줄 것

        for j in range(1,i+1):
            if i%j == 0:                # 약수의 개수 구하는 과정
                num += 1

        if num % 2 == 0:                # num이 짝수라면 s에 추가하기
            s.append(i)
        else:                           # 홀수라면 - 붙여서 s에 추가하기
            s.append(-i)

    return sum(s)                   # s에 있는 수 모두 합해서 return