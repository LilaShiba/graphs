# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
import time

start_time = time.time()

def path_finder(matrix,start,goal):
    length = len(matrix)
    visited = {}
    nodes = []
    path = {}
    paths = []
    spelled = []
    x,y = start
    unseenNodes = [(x,y,0)]

    for x in range(length):
        for y in range(length):
            nodes.append((x,y))
            visited[(x,y)] = float('Inf')
    visited[(0,0)] = 0

    while unseenNodes:
        unseenNodes = sorted(unseenNodes, key = lambda x: x[2])
        x,y,_ = unseenNodes[0]
        del unseenNodes[0]
        current_weight = visited[(x,y)]
        px, py = x,y
        if (x,y) == goal:
            break

        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        real_neighbors = [(x,y) for (x,y) in directions if (x,y) in nodes]

        for cx,cy in real_neighbors:
            weight =  current_weight + matrix[cx][cy]
            z = weight + (abs(cx - goal[0]) + abs(cy - goal[1]))
            if z < visited[(cx,cy)]:
                visited[(cx,cy)] = weight
                path[(cx,cy)] = (px,py)
                unseenNodes.append((cx,cy,z))



    currentNode = goal
    while currentNode != start:
        paths.insert(0,currentNode)
        currentNode = path[currentNode]
    print(paths)




# 9
f = [
    [1,9,1],
    [2,9,1],
    [2,1,1]
    ]

# ["down", "down", "right", "right", "up", "up"]

g= [
    [1,4,1],
    [1,9,1],
    [1,0,0]
    ]

print(path_finder(g,(0,0), (1,2)))


print("---%s seconds" %(time.time()- start_time))
