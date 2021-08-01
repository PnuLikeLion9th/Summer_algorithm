#백준 50제

H, M = map(int, input().split())
time = int(input()) 

H += time // 60
M += time % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H,M)