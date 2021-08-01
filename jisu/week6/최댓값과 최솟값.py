def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        
    return str(min(arr))+" "+ str(max(arr))