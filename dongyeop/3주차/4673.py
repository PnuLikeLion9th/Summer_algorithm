#백준 4673 셀프넘버
#셀프넘버란 => 33-> 33+3+3= 39 33은 39의 생성자이며 생성자가 없는 수를 셀프넘버라한다. 1은 2의 생성자이고 6은 12의 생성자이다.
not_self=[]#전역리스트

def answer():#1부터 10000까지의 셀프넘버를 구하여라.
    for i in range(1,10001):
        solution(i)

def solution(n):
    global not_self#지역변수가 아닌 전역 변수 not_self임을 알려줌
    if n not in not_self:
        print(n)
    a = str(n)
    next = n
    for i in range(len(a)):
        next += int(a[i])
    not_self.append(next)

answer()