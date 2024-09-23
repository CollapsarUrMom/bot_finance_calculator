# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)

#     print(start)

#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# dfs(graph, '0')





# ===================================================================================================================
# ===================================================================================================================







a, b, c, d, e, f, g, h = range(8)
N = [
   {b, c, d, e, f}, # a
   {c, e}, # b
   {d}, # c
   {e}, # d
   {f}, # e
   {c, g, h}, # f
   {f, h}, # g
   {f, g} # h
]

#импортируем класс очереди
from queue import Queue

#соответсвие цифры букве
letters="abcdefgh"
visited_nodes={}

#Начальные переменные
queue=Queue()
beg_node=a
target_node=h

#шаг 1.    Поместить узел, с которого начинается поиск, в изначально пустую очередь.
queue.put(beg_node)
visited_nodes={beg_node}

# это у нас цикл с постусловием
while True:
   #шаг 2. Извлечь из начала очереди узел "u" и пометить его как развёрнутый.
   u=queue.get()
   print("Обходим узел",letters[u])

   #Если узел "u" является целевым узлом, то завершить поиск с результатом «успех».
   if u==target_node:
      print("Поиск успешно завершен")
      break
   else:
      #В противном случае, в конец очереди добавляются все преемники узла "u", которые ещё не развёрнуты и не находятся в очереди.
      for node in N[u]:
         print(" -- Смотрим ребро", letters[node])
         if not(node in visited_nodes):
            print("   ---- Узел", letters[node],"добавили в очередь")
            visited_nodes.add(node)
            queue.put(node)

   #шаг 3.    Если очередь пуста, то все узлы связного графа были просмотрены, следовательно, целевой узел
   # недостижим из начального; завершить поиск с результатом «неудача».
   if queue.empty():
      print("Вершина ",letters[u]," не найдена")

   #шаг 4. Вернуться к п. 2.