string = input("")

if string == " ":                       # 문장 자체가 공백인 경우 
    print(0)
else : 
    words = string.split(" ")           # 띄어쓰기로 구분
    
    while '' in words :                 #문장 양쪽에 있는 공백이 없어질 때까지 반복
        words.remove('')
        
print(len(words))