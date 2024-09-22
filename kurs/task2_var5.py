

lin = '28 28 66 28'
# lin = '1 98 34 98 6'
# lin = '11 -86 -86 201 11 86 86 86 3 201'      #// 3
#lin = '2 4 3 2 1 4 1'                         #// 3
#lin = '3 2 5 2 5 2 5 3'                       #// 1
# lin = '3 5 2 2 5'                             #// 2
#lin = '1 2 14 4 5 6 7 30 31 32 8 19 10 11 12 13 14 15 16 17 18 19 12 21 26 27 28 8 22 23' #// 12
#lin = '1 2 14 4 5 6 7 30 31 32 33 34 8 35 19 10 11 12 13 41 42 43 14 15 16 17 18 19 12 21 26 27 28 29 8 22 23' #// 14



from collections import deque


continents = {}
deq = deque([0])


def connection(x, y):
    graph[x].append(y)
    graph[y].append(x)


line = list(lin.split())
size_line = len(line)


graph = [[] for _ in range(0, 2 * size_line - 1)]


for x in range(0, 2 * size_line - 2):
    connection(x, x + 1)


for i, x in enumerate(line):
    portal = continents.setdefault(x, len(graph))
    if portal == len(graph):
        graph.append([])
    connection(2 * i, portal)


distance = [0 for x in range(0, len(graph))]


while deq:
    current_node = deq.popleft()
    if current_node == 2 * size_line - 2:
        break
    for x in graph[current_node]:
        if distance[x] == 0:
            # print(current_node, graph[current_node], x)
            distance[x] = distance[current_node] + 1
            print(current_node, graph[current_node], x)
            deq.append(x)


print(distance[2 * size_line - 2] // 2)