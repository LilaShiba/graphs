import random
import time

start_time = time.time()

def dijsktra(graph):
    length = len(graph)
    start = (0,0)
    goal = (length-1, length-1)

    visited = {}
    path = {}

    nodes = []

    for x in range(length):
        for y in range(length):
            nodes.append((x,y))
            #visited[(x,y)] = float('Inf')
    visited[(0,0)] = 0


    while nodes:
        # find minNode
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode == None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

        if minNode == (length-1, length-1):
            return visited[length-1, length-1], path

        nodes.remove(minNode)
        current_weight = visited[minNode]

        x,y = minNode
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for cx,cy in directions:
            if (cx,cy) in nodes:
                weight = visited[(x,y)] + abs(matrix[cx][cy]- matrix[x][y])
                if (cx,cy) not in visited or weight < visited[(cx,cy)]:
                    visited[(cx, cy)] = weight
                    path[minNode] = (cx,cy)
    return visited[length-1, length-1], path

matrix = [[random.randint(0,10) for x in range(5)]for y in range(5)]
num, path = dijsktra(matrix)

print("---%s seconds" %(time.time()- start_time))

print(num, path)
