import time
start_time = time.time()

def cheapest_path(matrix,start,goal):
    shortest_path = {}
    unseenNodes = []
    exploring_weights = {}
    parent = {}
    paths = []
    spelled = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            shortest_path[( row, col )] = float('Inf')
            unseenNodes.append(( row, col ))
    shortest_path[start] = 0

    while unseenNodes:
        currentNode = None
        for nodes in unseenNodes:
            if currentNode is None:
                currentNode = nodes
            elif shortest_path[nodes] < shortest_path[currentNode]:
                currentNode = nodes

        unseenNodes.remove(currentNode)
        current_weight = shortest_path[currentNode]
        x, y = currentNode
        neighbors = [(x, y+1), (x+1, y), (x-1, y), (x, y-1)]

        for cx, cy in neighbors:
            if (cx,cy) in unseenNodes:
                weight = current_weight + matrix[cx][cy]
                if weight < shortest_path[( cx, cy )]:
                    shortest_path[( cx, cy )] = weight
                    exploring_weights[( cx, cy)] = weight
                    parent[( cx, cy )] = currentNode



        if currentNode == goal:
            break
            #return shortest_path

    path_done = goal

    while path_done != start:
        paths.insert(0,path_done)
        path_done = parent[path_done]



    px, py = start
    for x,y in paths:
        if x > px:
            spelled.append('up')
        elif x < px:
            spelled.append('down')
        elif y < py:
            spelled.append('right')
        else:
            spelled.append('left')
        px,py = x,y

    return (spelled, len(paths))

g= [
    [1,0,1,1],
    [1,0,1,0],
    [1,0,1,0]
    ]

h = [
    [1, 20, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 90, 90, 90, 90, 90, 90, 90, 90, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

print(cheapest_path([[1,9,1],[2,9,1],[2,1,1]], (0,0), (0,2)))

# [1,9,1]
# [2,9,1]
# [2,1,1]

#print(cheapest_path(g,(0,0), (2,0)))
print("---%s seconds" %(time.time()- start_time))
