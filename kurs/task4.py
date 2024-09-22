from collections import deque

def is_valid(x, y, MaxX, MaxY):
    if 0 <= x < MaxX and 0 <= y < MaxY:
        return True
    else:
        return False
    
def bfs(x1, y1, maxX, maxY, word, matrix):          
    
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]   
    
    visited = [[False] * maxY for _ in range(maxX)]
    visited[x1][y1] = True       
  
    deq = deque([(x1, y1, 0)])  
                   
    while deq:
        x, y, index_word = deq.popleft()
        count = 0
        for dx, dy in direct:
            new_x, new_y = x + dx, y + dy
            
            if is_valid(new_x, new_y, maxX, maxY) and not visited[new_x][new_y]:
                
                if matrix[new_x][new_y] == word[index_word+1]:
                    
                    if index_word + 1 == len(word) - 1:                        
                        return True
               
                    deq.append((new_x, new_y, index_word+1))
                    visited[new_x][new_y] = True
                    count += 1
                    if count > 1:
                        

                       
        

if __name__ == '__main__':
    
    matrix = [
    ['A', 'F', 'R', 'D', 'H'],
    ['O', 'L', 'M', 'O', 'E'],
    ['L', 'M', 'Q', 'L', 'L']
    ]
    # word = 'HELLO'
    word = 'AOLMLF'

    maxX, maxY = len(matrix), len(matrix[0])
    
    is_find = False

    #find first character
    for x, row in enumerate(matrix):   
        if is_find:
            break
        for y, character in enumerate(row):           
            if character == word[0]:
                if bfs(x, y, maxX, maxY, word, matrix):
                    is_find = True
                    break             
    
    print(is_find)
