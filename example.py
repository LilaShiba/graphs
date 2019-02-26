# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
# Bellman Ford
import pprint
# returns x,y,weight
#def find_neighbors(maze, node):
    # x,y = node
    # length = len(maze)
    # neighbors = []
    # for x,y in (x, y-1), (x, y+1), (x-1, y), (x+1,y):
    #     if 0<= x < length and 0<= y < length:
    #         weight = maze[x][y]
    #         neighbors.append([x,y,weight])
    # return neighbors
def find_neighbors(maze, node):
    x,y = node
    length = len(maze)
    neighbors = []
    for x,y in (x, y-1), (x, y+1), (x-1, y), (x+1,y):
        if 0<= x < length and 0<= y < length:
            weight = maze[x][y]
            neighbors.append([x,y,weight])
    return neighbors

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    #dist=[float('inf')]*len(adj)
    shortest_distance = {}
    predecessor = {}
    path = []
    adj = dict()

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            adj[(row,col)] = find_neighbors(matrix, (row,col))
            current = adj[(row,col)]

    # set all unexplored nodes to inf
    for vertex in adj:
        shortest_distance[vertex] = float('inf')
    shortest_distance[(0,0)] = int(matrix[0][0])

    unseenNodes = adj
    print(shortest_distance)

    # search time
    while unseenNodes:
        minNode = None
        # grab first unseenNode
        for node in unseenNodes:
            # set minNode
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        # check neighbors
        for x,y,weight in adj[minNode]:
            weight = int(weight)
            child_node = x,y

            # relax
            if weight + shortest_distance[minNode] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[minNode]
                # increase minNode for each level
                predecessor[(x,y)] = minNode
                #print(minNode)



        unseenNodes.pop(minNode)
    return shortest_distance







f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

e = "\n".join([
  "700000",
  "277773",
  "077770",
  "077770",
  "077770",
  "000007"
])
print(path_finder(e))
