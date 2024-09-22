from collections import deque


def is_valid(x, y, MaxX, MaxY):
    if 0 <= x < MaxX and 0 <= y < MaxY:
        return True
    else:
        return False

def recursive_search(x1, y1, index_word, visited):  
    visited[x1][y1] = True   

    for dx, dy in direct:

        new_x, new_y = x1 + dx, y1 + dy

        if is_valid(new_x, new_y, maxX, maxY) and not visited[new_x][new_y]:

            if matrix[new_x][new_y] == word[index_word+1]:

                if index_word + 1 == len(word) - 1:
                    return True                    

                if recursive_search(new_x, new_y, index_word+1, visited):
                    return True
    return False         

if __name__ == '__main__':

    matrix = [
    ['A', 'F', 'R', 'D', 'H'],
    ['O', 'L', 'M', 'O', 'E'],
    ['L', 'M', 'Q', 'L', 'L']
    ]

    word = 'HELLO'
    #word = 'AOLMLF'

    maxX, maxY = len(matrix), len(matrix[0])
    print(maxX, maxY)

    is_find = False
    visited = [[False] * maxY for _ in range(maxX)]
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    #find first character
    for x, row in enumerate(matrix):   
        if is_find:
            break
        for y, character in enumerate(row):           
            if character == word[0]:
                if recursive_search(x, y, 0, visited):
                    is_find = True
                    break             


    print(visited)
    print(is_find)




