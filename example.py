# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
# Bellman Ford
import pprint

# todo add min node
# todo cycle through all nodes
# todo pop off min nodes from set of nodes
def find_neighbors(row,col,matrix):
    neighbors = []
    length = len(matrix)
    x,y = row,col
    for x,y in (x, y-1), (x, y+1), (x-1,y), (x+1,y):
        if 0 <= x < length and 0<= y < length:
            neighbors.append((x,y,int(matrix[x][y])))
    return neighbors

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    # track amount of climbs
    climbs = dict()
    adj_list = dict()
    length = len(matrix)

    # create climbs & adj_list
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = int(matrix[row][col])
            climbs[(row,col)] = 1000
            adj_list[(row,col)] = find_neighbors(row,col,matrix)
    climbs[(0,0)] = 0

    unseenNodes = adj_list

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif climbs[node] < climbs[minNode]:
                minNode = node

        for cx, cy, weight in adj_list[minNode]:

            # relax
            # if parent > child
            x,y = minNode

            # if child is larger than parent in matrix
            if matrix[cx][cy] > matrix[x][y]:
                # weight between u -> v
                diff = matrix[cx][cy] - matrix[x][y]
                if diff + climbs[(x,y)] < climbs[(cx,cy)]:
                    climbs[(cx,cy)] = diff + climbs[(x,y)]

            #if parent is larger than child
            elif matrix[cx][cy] < matrix[x][y]:
                diff = matrix[x][y] - matrix[cx][cy]
                if diff + climbs[(x,y)] < climbs[(cx,cy)]:
                    climbs[(cx,cy)] = diff + climbs[(x,y)]

            else:
                if matrix[x][y] == matrix[cx][cy]:
                    climbs[(cx,cy)] = climbs[(x,y)]
        unseenNodes.pop(minNode)
    print(climbs)

    return climbs[(length-1,length-1)]



# 12
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
c = "\n".join([
  "110",
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


b = "\n".join([
  "010",
  "010",
  "010"
])
pprint.pprint(path_finder(f))
