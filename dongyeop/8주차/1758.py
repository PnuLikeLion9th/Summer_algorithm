#팁 액수가 적을수록 뒤로 밀어야한다.
#팁액수에서 본인의 인덱스값을 뺀값이 주는 팁
n = int(input())
person = list()
answer = 0
for i in range(n):
    person.append(int(input()))

person.sort(reverse=True)
for i in range(len(person)):
    tip = person[i]-i
    if tip>0:
        answer+=tip
    else:
        pass

print(answer)