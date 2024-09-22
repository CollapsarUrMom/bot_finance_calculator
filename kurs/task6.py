from collections import deque
deq = deque()
deq.append(left_node)
while deq:

    start_node = Node(1, Node(2), Node(3))
    #start(Node, int, int) 
    #start(Node(1, Node(2), Node(3), 2, 3)


current_layer = set(start_node.left) #2
layer_number = 0


while right_node not in current_layer: #3
    next_layer = set()
    for current_node in current_layer:

        next_layer.add(current_node.value)    #1


    layer_number += 1
    current_layer = next_layer
    
print(layer_number)