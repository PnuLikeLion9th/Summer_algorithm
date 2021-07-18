#소수 찾기
'''에라토스테네스의 체 이용: 소수 찾으면 소수의 배수들 다 제거하는 방식'''

def solution(n):
    def prime_number(n): # 0~n을 소수(True)인 것으로 초기화
        prime = [True for _ in range(n + 1)] # 2부터 n까지 소수 여부 판별 (0, 1은 소수)
        for i in range(2, int(math.sqrt(n)) + 1):  # 2부터 n의 제곱근까지 확인
            
            # i가 소수인 경우 (남은 수인 경우)
            if prime[i] == True:
                # i를 제외한 i의 모든 배수는 소수가 아니므로, False 대입
                j = 2
                while i * j <= n:
                    prime[i * j] = False
                    j += 1

        return [i for i in range(2, n + 1) if prime[i]]

    return len(prime_number(n))
