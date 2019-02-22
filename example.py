# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
# Bellman Ford

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
    length = len(matrix)-1
    adj_list = dict()
    dist = {}
    adj_list[(0,0)] = {}
    current = adj_list[(0,0)]
    # make adj list with weights
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            adj_list[(row,col)] = find_neighbors(matrix, (row,col))
            current = adj_list[(row,col)]

    #print(adj_list)
    for v in adj_list:
        dist[v] = float('Inf')
    dist[(0,0)] = int(matrix[0][0])
    #print(dist)
    for i in range(len(adj_list)-1):
        for u in adj_list:
            r,c = u
            #print(r,c)
            for x,y,w in adj_list[(r,c)]:
                w = int(w)
                if dist[(r,c)] != float('Inf') and dist[(r,c)] + w < dist[(x,y)]:
                    dist[(x,y)] = dist[(r,c)] + w
    return(dist[(length,length)]-dist[(0,0)])
        #print(x,y,w)

    # relax baby

    # for j in unseenNodes:
    #     x,y = j
    #     neighbors = find_neighbors(matrix, (x,y))
    #     for z in neighbors:
    #         adj_list[(x,y)] = neighbors
    # return adj_list




f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

print(path_finder(f))
