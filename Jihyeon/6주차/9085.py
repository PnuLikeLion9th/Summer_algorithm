T = int(input())

for _ in range(T):                              # 테스트 케이스 개수 T만큼 반복
    n = int(input())                            # 자연수의 개수 n을 정수형을 변환
    num = list(map(int, input().split()))       # n개의 자연수를 공백으로 구분해 입력, 정수형 변환
    print(sum(num))