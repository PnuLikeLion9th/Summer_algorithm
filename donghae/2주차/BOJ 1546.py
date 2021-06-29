n = int(input())
list = list(map(int, input().split()))
new_list = []   #새로운 점수를 담을 리스트
for i in range(n):
    new_list.append((list[i]/max(list))*100)
print(sum(new_list)/n)  #평균 출력
