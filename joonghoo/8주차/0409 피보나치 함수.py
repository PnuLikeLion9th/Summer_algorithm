# 백준1003_피보나치 함수_dp_실버 3
# 규칙을 찾아서 푸는 방법
# n을 0~9 까지 넣어보며 규칙을 찾는다
# n    zero one
# 0 ==>  1   0
# 1 ==>  0   1
# 2 ==>  1   1
# 3 ==>  1   2
# 4 ==>  2   3
# 5 ==>  3   5
# 6 ==>  5   8
# 7 ==>  8   13
# 8 ==>  13  21
# 9 ==>  21  34
# 이렇게 보면 n이 1증가할때
# 현재 항의 zero의 값은 전항의 one의 값이고, one의 값은 전항의 zero+one 이라는 것을 알수있다

for _ in range(int(input())):
    n = int(input())
    zero = 1
    one = 0
    for _ in range(n):
        temp = one
        one = temp + zero
        zero = temp
    print(zero, one)
