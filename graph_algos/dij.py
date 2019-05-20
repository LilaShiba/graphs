#import heapq
import time,random, pprint
start_time = time.time()

def path_finder(matrix):

    length = len(matrix)
    start = (0,0,0)
    goal = (length-1, length-1)

    parent = {}
    visited = {(0,0): 0}
    unseenNodes = [start]
    #heapq.heapify(unseenNodes)

    while unseenNodes:
        #minNode = heapq.heappop(unseenNodes)
        unseenNodes = sorted(unseenNodes, key = lambda x: x[2])
        minNode = unseenNodes.pop(0)

        x,y,current_weight = minNode
        px, py = x,y

        if (x,y) == goal:
            node = goal
            while node != (0,0):
                x,y = node
                matrix[x][y] = '*'
                node = parent[node]
            pprint.pprint(matrix)
            return (visited[goal])


        neighbors = ((x-1,y),(x,y-1),(x+1,y),(x,y+1))
        real_neighbors = ((x,y) for (x,y) in neighbors if 0 <= x < length and 0<= y < len(matrix[0]))

        for cx,cy in real_neighbors:
            cost = current_weight + matrix[cx][cy]
            #dist = abs(goal[0] - cx) + abs(goal[1]-cy)
            if (cx,cy) not in parent or cost < visited[(cx,cy)]:
                visited[(cx,cy)] = cost
                unseenNodes.append((cx,cy,cost))
                parent[(cx,cy)] = (px,py)



import random, pprint
#matrix = [[x + 1 for x in range(200)] for y in range(200)]
matrix = [[0, 6, 6, 2, 8, 9, 9, 3, 8, 3],
 [6, 5, 2, 9, 5, 7, 9, 1, 7, 7],
 [3, 9, 5, 1, 4, 3, 0, 1, 8, 3],
 [4, 7, 2, 6, 4, 8, 0, 2, 9, 2],
 [3, 5, 0, 6, 0, 1, 1, 2, 6, 9],
 [9, 8, 5, 8, 3, 2, 4, 9, 9, 0],
 [9, 7, 7, 9, 1, 1, 5, 0, 2, 5],
 [1, 4, 4, 3, 3, 4, 1, 9, 4, 4],
 [5, 5, 2, 0, 9, 6, 2, 7, 3, 3],
 [8, 2, 4, 8, 2, 2, 2, 3, 1, 6]]

print(path_finder(matrix))
print("--- %s seconds ---" % (time.time() - start_time))
