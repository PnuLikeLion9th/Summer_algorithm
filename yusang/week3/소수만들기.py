from itertools import combinations


def solution(nums):
    
    answer = 0
    
    combination = list(combinations(nums, 3))
    combination = list(map(lambda x : sum(list(x)) ,combination))  
    combination = list(set(combination))
    
    print(combination)
    
    for number in combination:
        isAnswer = True
        for i in range(2, int(number/2)):
            print(number / i - int (number/i) == 0.0)
            if number / i - int(number / i) == 0.0 and number % i == 0:
                isAnswer = False
                break
        if isAnswer :
            answer = answer +1
            
    
    return answer


print(solution([1,2,3]))