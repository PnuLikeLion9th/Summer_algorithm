# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다.
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

list = []
for i in range(10):
    x = int(input()) % 42
    list.append(x)
print(len(set(list))) #set함수로 중복 제거 후 길이 구하기
