#lin = '11 -86 -86 201 11 86 86 86 3 201'      #// 3
#lin = '2 4 3 2 1 4 1'                         #// 3
#lin = '3 2 5 2 5 2 5 3'                       #// 1
#lin = '3 5 2 2 5'                             #// 2
#lin = '1 2 14 4 5 6 7 30 31 32 8 19 10 11 12 13 14 15 16 17 18 19 12 21 26 27 28 8 22 23' #// 12
lin = '1 2 14 4 5 6 7 30 31 32 33 34 8 35 19 10 11 12 13 41 42 43 14 15 16 17 18 19 12 21 26 27 28 29 8 22 23' #// 14

import time
start = time.perf_counter()

line = list(lin.split())
#line = [int(x) for x in input().split()]

# заполняем словарь континентов
from collections import defaultdict
continent = defaultdict(list)           # <index continent, <list island>>
for i in range(len(line)):
    if line[i] in continent:
        continent[line[i]].append(i)
    else:
        continent[line[i]] = [i]   
print(continent)     

previous_layer, current_layer =set([-1, 0]), set([0])
layer_number = 0        
   
while len(line)-1 not in current_layer:
    next_layer = set()
    for current_index in current_layer:
        #print(current_index)
        
        #portal move        
        for next_index in continent[line[current_index]]:
            if next_index not in previous_layer:
                next_layer.add(next_index)
                previous_layer.add(next_index)
                #print(next_index)          
        
        # left move
        if current_index-1 not in previous_layer:
            next_layer.add(current_index-1)
            previous_layer.add(current_index-1)
            
        # right move   
        if current_index+1 not in previous_layer:
            next_layer.add(current_index+1)
            previous_layer.add(current_index+1)     
    
    layer_number += 1   
    current_layer = next_layer
       

finish = time.perf_counter()
print('Время работы: ' + str(finish - start))

print('Ответ: ', layer_number)