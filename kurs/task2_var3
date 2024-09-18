import collections

islands = [3, 2, 5, 2, 5, 2, 5, 3]

n = len(islands)

graph = [[] for _ in range(2 * n - 1)]


def connect(j1, j2):
    graph[j1].append(j2)
    graph[j2].append(j1)


for j in range(2 * n - 2):
    connect(j, j + 1)

continents = {}
for i, c in enumerate(islands):
    k = continents.setdefault(c, len(graph))
    if k == len(graph):
        graph.append([])
    connect(2 * i, k)

distance = [0] * len(graph)
queue = collections.deque([0])
while queue:
    j = queue.popleft()
    if j == 2 * n - 2:
        break
    for k in graph[j]:
        if distance[k] == 0:
            distance[k] = distance[j] + 1
            queue.append(k)

print(distance[2 * n - 2] // 2)