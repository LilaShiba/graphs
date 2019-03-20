def cheapest_path(matrix,start,goal):
    length = len(matrix)
    visited = {}
    nodes = []
    path = {}
    spelled = []
    paths = []

    # fill nodes and visited init to infi
    for x in range(length):
        for y in range(length):
            nodes.append((x,y))
            visited[(x,y)] = float('Inf')
    visited[start] = 0

    # while time to explore
    while nodes:
        # find minNode
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode == None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node


        nodes.remove(minNode)
        current_weight = visited[minNode]

        x,y = minNode
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]

        for cx,cy in directions:
            if 0 <= cx < length and 0 <= cy <length:
                weight = current_weight + matrix[cx][cy]
                if weight < visited[(cx,cy)]:
                    visited[(cx, cy)] = weight
                    path[(cx,cy)] = minNode
        if minNode == goal:
            path[cx,cy] = minNode
            break

    currentNode = goal
    while currentNode != start:
        paths.insert(0,currentNode)
        currentNode = path[currentNode]
    print(paths)

    px, py = start
    for x,y in paths:
        if x > px:
            spelled.append('down')
        elif x < px:
            spelled.append('up')
        elif y < py:
            spelled.append('left')
        elif y > py:
            spelled.append('right')
        px,py = x,y
    return spelled
