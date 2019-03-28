# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
import time
start_time = time.time()

def path_finder(a):
    # make 2d array
    matrix =  list(map(list, a.splitlines()))
    # length of maze
    length = len(matrix)
    # end of maze
    endo = length-1,length-1
    # transform string to int
    matrix = [[int(y) for y in x] for x in matrix]
    # flatten 2D array to 1D
    matrix_span = range(length)
    unseenNodes = [[(x,y) for y in matrix_span] for x in matrix_span]
    unseenNodes = [item for sublist in unseenNodes for item in sublist]
    # set distances to inf
    climbs = {key:100 for key in unseenNodes}
    # start distance is 0
    climbs[(0,0)] = 0

    for i in range(len(unseenNodes)-1):
        for u in unseenNodes:
            cx, cy = u
            for cx, cy, in (cx, cy-1), (cx, cy+1), (cx-1,cy), (cx+1,cy):
                if (cx,cy) in unseenNodes:
                    x,y = u

                    diff = abs(matrix[cx][cy] - matrix[x][y])
                    if diff + climbs[(x,y)] < climbs[(cx,cy)]:
                        climbs[(cx,cy)] = diff + climbs[(x,y)]

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

print(path_finder(f))
print("--- %s seconds ---" % (time.time() - start_time))
