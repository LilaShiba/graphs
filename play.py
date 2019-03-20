# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
import time

start_time = time.time()

def path_finder(matrix,start,goal):
    length = len(matrix)
    visited = {}
    nodes = []
    path = []
    spelled = []


    for x in range(length):
        for y in range(length):
            nodes.append((x,y))
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


        if minNode == goal:
            path.append(goal)
            break

        nodes.remove(minNode)
        current_weight = visited[minNode]

        x,y = minNode
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for cx,cy in directions:
            if (cx,cy) in nodes:
                weight = visited[(x,y)] + matrix[cx][cy]
                if (cx,cy) not in visited or weight < visited[(cx,cy)]:
                    visited[(cx, cy)] = weight
                    if minNode not in path and minNode != start:
                        path.append(minNode)
    px, py = start
    for x,y in path:
        if x > px:
            spelled.append('Down')
        elif x < px:
            spelled.append('Up')
        elif y < py:
            spelled.append('Left')
        elif y > py:
            spelled.append('Right')
        px,py = x,y
    return(spelled)



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
    [1,1,1]
    ]

print(path_finder(g,(0,0), (0,2)))


print("---%s seconds" %(time.time()- start_time))
