#죠르디 .. 아이고 머리야 .. 

#어려워서 .. 구글 보면서 아예 따라하깅 .. !! ㅜ.ㅜ 담에 다시 풀어보겠습니닷 ..

def solution(board, moves):
    basket = [] 
    answer = 0 
    
    for move in moves: 
        for column in board: 
            if column[move-1] != 0: 
                basket.append(column[move-1]) 
                
                if len(basket) > 1: 
                    if basket[-2] == basket[-1]: 
                        del basket[-2] 
                        del basket[-1] 
                        answer += 2 
                        
                column[move-1] = 0 
                break 
    return answer 

#이건 .. 너무 어렵군효 ..