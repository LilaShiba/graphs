# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
# Bellman Ford
import pprint

# todo add min node
# todo cycle through all nodes
# todo pop off min nodes from set of nodes

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    # track amount of climbs
    climbs = dict()

    # create climbs
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = int(matrix[row][col])
            climbs[(row,col)] = 1000
    climbs[(0,0)] = 0

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            x,y = row, col
            # find neighbors
            for x,y in (x, y-1), (x, y+1), (x-1,y), (x+1,y):
                if 0 <= x < length and 0<= y < length:
                    # relax
                    # if parent > child
                    if matrix[row][col] > matrix[x][y]:
                        # if parent - child < value in climbs for child
                        if matrix[row][col] - matrix[x][y] < climbs[(x,y)]:
                            climbs[(x,y)] = climbs[(row,col)] + (matrix[row][col] - matrix[x][y])
                    # if child > parent
                    elif matrix[row][col] < matrix[x][y]:
                        # if child - parent < value in climbs for child
                        if matrix[x][y] - matrix[row][col] < climbs[(x,y)]:
                            climbs[(x,y)] = climbs[(row,col)]+ (matrix[x][y]- matrix[row][col])
                    # if they are equal
                    else:
                        # carry over climb count
                        climbs[(x,y)] = climbs[(row,col)]

    print(climbs)
    return climbs[(length-1,length-1)]


f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
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
pprint.pprint(path_finder(b))
