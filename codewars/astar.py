import random, heapq, time
matrix = [[x+1 for x in range(100)]for y in range(110)]

def astar(matrix,source,target):
    length = len(matrix)
    shortest_path = {source:0}
    parent = {}
    x,y = source
    start = (0,x,y)
    unseenNodes = [start]
    heapq.heapify(unseenNodes)

    while unseenNodes:
        heapq.heapify(unseenNodes)
        minNode = heapq.heappop(unseenNodes)
        _,x,y = minNode
        current_weight = shortest_path[(x,y)]

        if (x,y) == target:
            return shortest_path[target]

        px, py = x,y
        directions = ((x+1,y), (x,y+1), (x-1,y), (x, y-1))
        real_neighbors = ((x,y) for (x,y) in directions if 0<= x < length and 0<= y < length)

        for cx,cy in real_neighbors:
            weight = shortest_path[(x,y)] + matrix[cx][cy]
            heuristic = weight + (abs(cx - target[0]) + abs(cy - target[1]))
            if (cx,cy) not in shortest_path or heuristic < shortest_path[(cx,cy)]:
                shortest_path[(cx,cy)] = weight
                unseenNodes.append((heuristic,cx,cy))
                parent[(cx,cy)] = (x,y)



    return (shortest_path)

start_time = time.clock()
print(astar(matrix, (0,0), (0,99)))
end = time.clock()

print(end - start_time)
