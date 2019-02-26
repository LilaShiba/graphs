# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
# Bellman Ford
import pprint

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    start = int(matrix[0][0])
    climbs = dict()
    explored = []


    # create climbs
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = int(matrix[row][col])
            climbs[(row,col)] = 1000

    climbs[(0,0)] = 0
    print(climbs)


    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (row,col) != explored:
                x,y = row, col
                for x,y in (x, y-1), (x, y+1), (x-1,y), (x+1,y):
                    if 0 <= x < length and 0<= y < length:
                        explored.append((row,col))
                        # relax

                        if matrix[row][col] > matrix[x][y]:
                            if matrix[row][col] - matrix[x][y] < climbs[(x,y)]:
                                climbs[(x,y)] = climbs[(row,col)] + (matrix[row][col] - matrix[x][y])

                        elif matrix[row][col] < matrix[x][y]:
                            if matrix[x][y] - matrix[row][col] < climbs[(x,y)]:
                                climbs[(x,y)] = climbs[(row,col)]+ (matrix[x][y]- matrix[row][col])

                        else:
                            climbs[(x,y)] = climbs[(row,col)]







    return climbs






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
