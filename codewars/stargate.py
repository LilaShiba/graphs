def wire_DHD_SG1(existingWires):
    matrix =  list(map(list, existingWires.splitlines()))
    length = len(matrix)
    # find start


    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            x,y = u
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length:
                    if (x,y) not in level and matrix[x][y] != 'W':
                        level[(x,y)] = i
                        parent[(x,y)] = u
                        next.append((x,y))
                        if (x,y) == t:
                            return level[(x,y)]

        frontier = next
        i += 1
    return False
    # Your code here!
    return "Oh for crying out loud...
