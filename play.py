# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
import time

start_time = time.time()

def path_finder(matrix):
    matrix =  list(map(list, matrix.splitlines()))
    length = len(matrix)
    start = (0,0)
    goal = (length-1, length-1)
    visited = {}
    nodes = []
    path = {}
    matrix = [[int(y) for y in x] for x in matrix]


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
                    path[(cx,cy)] = minNode

# 9
f = "\n".join([
  "77700220",
  "00700330",
  "00723220",
  "00732330",
  "00743220",
  "10000010",
  "01001001",
  '00000010'

])
print(path_finder(f))

print("---%s seconds" %(time.time()- start_time))



def matrix_addition(a, b):
    ans = []
    for x in range(len(a)):
        new_list = []
        for y in range(len(a)):
            new_list.append(a[x][y] + b[x][y])
            ans.append(new_list)
    return ans
