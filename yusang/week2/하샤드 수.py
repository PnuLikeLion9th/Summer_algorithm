def solution(x):
    
    if x % sum(list(map(int, list(str(x))))) == 0:
        return True
    else:
        return False


print(solution(10))