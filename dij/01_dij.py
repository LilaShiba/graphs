def dijsktra(graph):
    length = len(graph)
    goal = (length-1, length-1)
    visited = {}
    nodes = []
    graph = [[int(x) for x in y]for y in graph]

    # nodes = [[(x,y) for y in range(length)] for x in range(length)]
    # nodes = [item for sublist in nodes for item in sublist]

    for x in range(length):
        for y in range(length):
            nodes.append((x,y))
    visited[(0,0)] = 0


    while nodes:
        # find minNode
        minNode = nodes[0]
        for node in nodes:
            if node in visited:
                if visited[node] < visited[minNode]:
                    minNode = node

        if minNode == goal:
            return visited[goal]

        nodes.remove(minNode)
        current_weight = visited[minNode]

        x,y = minNode
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for cx,cy in directions:
            if (cx,cy) in nodes:
                weight = visited[(x,y)] + abs(graph[cx][cy]- graph[x][y])
                if (cx,cy) not in visited or weight < visited[(cx,cy)]:
                    visited[(cx, cy)] = weight
                    #path[minNode] = (cx,cy)






import random
import time

start_time = time.time()

matrix = [[random.randint(0,10) for x in range(50)]for y in range(50)]
num = dijsktra(matrix)

print(num)
print("---%s seconds" %(time.time()- start_time))
