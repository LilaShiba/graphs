import random, pprint
def make_maze(size,level):
    matrix = [[random.randint(0,10) for x in range(size)] for y in range(size)]

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] < level:
                matrix[x][y] = 'W'
            else:
                matrix[x][y] = '.'

    return matrix

matrix = make_maze(10,3)
pprint.pprint(matrix)

def can_exit(graph):
    length = len(graph)
    start = (0,0)
    goal = (length-1, length-1)
    frontier = [start]
    explored = []
    parent = {start: 0}

    while frontier:
        to_explore = []
        for u in frontier:
            x,y = u
            for x,y in (x,y-1), (x,y+1), (x-1, y), (x+1,y):
                if 0<=x<length and 0<=y<length:
                    if (x,y) not in explored and matrix[x][y] != 'W':
                        to_explore.append((x,y))
                        explored.append((x,y))
                        parent[(x,y)] = u
                        if (x,y) == goal:
                            return parent
        frontier.remove(u)
        frontier = to_explore
    return False

print(can_exit(matrix))
