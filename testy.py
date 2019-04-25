def path_finder(matrix):
    # input 2D array full of intergers
    # interger element = cost of movement
    length = len(matrix)
    goal = (length-1,length-1)
    start = (0,0,0)
    # store the cost of a node
    visited = {(0,0): 0}
    unexplored = [start]
    parent = {}

    while unexplored:
        # sort by weight
        unexplored = sorted(unexplored, key = lambda x: x[2])
        # smallest weighted vertex from unexplored
        minNode = unexplored.pop(0)

        x,y,current_weight = minNode

        # parent node or child node
        px,py = x,y

        # end program
        if (px,py) == goal:
            return visited[goal] + matrix[px][py]

        # neighbors
        neighbors = ( (x-1,y), (x+1,y), (x,y-1), (x, y+1) )
        # make sure you are in the bound of the maze
        real_neighbors = ( (x,y) for (x,y) in neighbors if 0 <= x < length and 0 <= y < len(matrix[0]) )

        for cx,cy in real_neighbors:
            cost = current_weight + matrix[cx][cy]
            if (cx,cy) not in parent or cost < visited[(cx,cy)]:
                visited[(cx,cy)] = cost
                parent[(cx,cy)] = (px,py)
                unexplored.append((cx,cy,cost))

import random
arr = [[x + 1 for x in range(100)] for y in range(100)]
print(path_finder(arr))
