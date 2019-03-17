def path_finder(a):
    matrix =  list(map(list, a.splitlines()))
    # length of maze
    length = len(matrix)
    # end of maze
    endo = length-1,length-1

    matrix = [[int(y) for y in x] for x in matrix]
    matrix_span = range(length)
    unseenNodes = [[(x,y) for y in matrix_span] for x in matrix_span]
    unseenNodes = [item for sublist in unseenNodes for item in sublist]
    climbs = {key:float('Inf') for key in unseenNodes}
    climbs[(0,0)] = 0
    while unseenNodes:
        # get next move
        minNode = min(unseenNodes)
        for node in unseenNodes:
            if climbs[node] < climbs[minNode]:
                minNode = node

        # end condition
        if minNode == endo:
            return climbs[endo]


        # check out neighbors
        cx, cy = minNode
        neighbors = [(cx, cy-1), (cx, cy+1), (cx-1,cy), (cx+1,cy)]

        for cx, cy, in neighbors:
            if (cx,cy) in unseenNodes:
            # relax
                x,y = minNode
                diff = abs(matrix[cx][cy] - matrix[x][y])

                if diff + climbs[(x,y)] < climbs[(cx,cy)]:
                    climbs[(cx,cy)] = diff + climbs[(x,y)]
        unseenNodes.remove((minNode))
