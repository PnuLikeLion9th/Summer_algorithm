def solution(n):
    l = list(map(int, str(n))) #문자열 n을 숫자로 변환해 리스트로 만들기 
    return sum(l)   #sum함수로 리스트 합 반환