lin = '11 -86 -86 201 11 86 86 86 3 201'      #// 3
lin = '2 4 3 2 1 4 1'                         #// 3
lin = '3 2 5 2 5 2 5 3'                       #// 1
lin = '3 5 2 2 5'                             #// 2
lin = '1 2 14 4 5 6 7 30 31 32 8 19 10 11 12 13 14 15 16 17 18 19 12 21 26 27 28 8 22 23' #// 12
lin = '1 2 14 4 5 6 7 30 31 32 33 34 8 35 19 10 11 12 13 41 42 43 14 15 16 17 18 19 12 21 26 27 28 29 8 22 23' #// 14

import time
start = time.perf_counter()

line = list(lin.split())
#line = [int(x) for x in input().split()]

INF = 1e9;
distance = [INF for n in range(0, len(line))]
distPortal = { }    # <index continent, distance>

from queue import Queue
q = Queue(maxsize=0)

q.put(0)
distance[0] = 0
   
while not q.empty():
    currentIndex = q.get() 
    currentContinent = line[currentIndex]
    #print(currentIndex, currentContinent)   

    # portal move
    if currentContinent in distPortal:
        # not first Continent portal
        if distPortal[currentContinent] > distance[currentIndex]:
            distPortal[currentContinent] = distance[currentIndex]
        else:
            if distPortal[currentContinent] + 1 < distance[currentIndex]:
                distance[currentIndex] = distPortal[currentContinent] + 1
    else:
        # first Continent portal
        distPortal[currentContinent] = distance[currentIndex]    
  
    # right move
    if currentIndex + 1 < len(distance) and distance[currentIndex] + 1 < distance[currentIndex + 1]:
        distance[currentIndex + 1] = distance[currentIndex] + 1
        q.put(currentIndex + 1)
    
    # left move
    if currentIndex > 0 and distance[currentIndex] + 1 < distance[currentIndex - 1]:
        distance[currentIndex - 1] = distance[currentIndex] + 1
        q.put(currentIndex - 1) 

finish = time.perf_counter()
print('Время работы: ' + str(finish - start))

print('Ответ: ',distance[-1])