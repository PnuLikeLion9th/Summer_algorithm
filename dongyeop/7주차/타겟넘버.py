def solution(numbers,target):
    length = len(numbers)
    answer = 0
    def recursion(n,result):
        if n == length:
            if target == result:
                nonlocal answer
                answer+=1
            return
        else:
            recursion(n+1,result+numbers[n])
            recursion(n+1,result-numbers[n])
    recursion(0,0)
    return answer