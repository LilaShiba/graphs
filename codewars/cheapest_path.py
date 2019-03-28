def cheapest_path(matrix,start,goal):
    length = len(matrix)
    visited = {}
    path = {}
    spelled = []
    paths = []
    testy = []

    # fill nodes and visited init to infi
    nodes = [[(x,y) for y in range(len(matrix[0]))] for x in range(length)]
    nodes = [item for sublist in nodes for item in sublist]
    # set distances to inf
    visited = {key:float('Inf') for key in nodes}
    # start distance is 0
    visited[start] = 0
    # while time to explore
    while nodes:
        # find minNode
        minNode = None
        for node in nodes:
            if minNode == None:
                minNode = node
            elif visited[node] < visited[minNode]:
                minNode = node

        nodes.remove(minNode)
        current_weight = visited[minNode]

        x,y = minNode
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]

        for cx,cy in directions:
            if (cx,cy) in nodes:
                weight = current_weight + matrix[cx][cy]
                if weight < visited[(cx,cy)]:
                    visited[(cx, cy)] = weight
                    # child:parent
                    path[(cx,cy)] = minNode

        if minNode == goal:
            path[cx,cy] = minNode
            break

    currentNode = goal
    while currentNode != start:
        paths.insert(0,currentNode)
        currentNode = path[currentNode]

    px, py = start
    for x,y in paths:
        if x > px:
            spelled.append('down')
        elif x < px:
            spelled.append('up')
        elif y < py:
            spelled.append('left')
        else:
            spelled.append('right')
        px,py = x,y

    return spelled, paths





g= [
    [1,4,1,1],
    [1,9,1,0],
    [1,1,1,0]
    ]

h = [
    [1, 20, 1, 2, 1, 1, 1, 1, 1, 1],
    [1, 90, 90, 90, 90, 90, 90, 90, 90, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

print(cheapest_path(g,(0,0), (0,3)))
