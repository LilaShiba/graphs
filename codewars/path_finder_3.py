import time
start_time = time.time()
def path_finder(matrix):
    matrix =  list(map(list, matrix.splitlines()))
    length = len(matrix)
    start = (0,0)
    goal = (length-1, length-1)
    visited = {}
    nodes = []
    matrix = [[int(y) for y in x] for x in matrix]


    for x in range(length):
        for y in range(length):
            nodes.append((x,y))
            visited[(x,y)] = float('Inf')
    visited[(0,0)] = 0

    while nodes:
        minNode = None
        minNode = min([(visited[(x,y)], (x,y)) for (x,y) in nodes])[1]

        if minNode == goal:
            return visited[goal]

        nodes.remove(minNode)
        current_weight = visited[minNode]

        x,y = minNode
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        for cx,cy in directions:
            if (cx,cy) in nodes:
                weight = visited[(x,y)] + abs(matrix[cx][cy]- matrix[x][y])
                visited[(cx,cy)] = min(weight, visited[(cx,cy)])





e = "\n".join([
  "700000",
  "077770",
  "077770",
  "077770",
  "077770",
  "000007"
])

print(path_finder(e))
print("--- %s seconds ---" % (time.time() - start_time))
