import pprint
def wire_DHD_SG1(existingWires):
    matrix =  list(map(list, existingWires.splitlines()))
    length = len(matrix)
    # get start node
    count = 0
    for x in matrix:
        try:
            pos = x.index('S')
            break
        except:
            pos = None
        count +=1
    s = (count,pos)

    # find start
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            x,y = u
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1,y-1), (x+1, y+1), (x-1,y+1), (x+1,y-1):
                if 0 <= x < length and 0 <= y < length:
                    if (x,y) not in level and matrix[x][y] != 'X':
                        level[(x,y)] = i
                        px,py = u
                        parent[(x,y)] = (px,py)
                        next.append((x,y))
                        if matrix[x][y] == 'G':

                            currentNode = parent[(x,y)]
                            while currentNode != s:
                                cx,cy = currentNode
                                matrix[cx][cy] = 'P'
                                currentNode = parent[currentNode]
                            strg = ''
                            for x in matrix:
                                x = ''.join(x)
                                strg+= x + '\n'
                            strg = str(strg)

                            return strg[:-1]

        frontier = next
        i += 1
    # Your code here!
    return "Oh for crying out loud..."


meow = """
XX.S.XXX..
XXXX.X..XX
...X.XX...
XX...XXX.X
....XXX...
XXXX...XXX
X...XX...X
X...X...XX
XXXXXXXX.X
G........X
""".strip('\n')

meow2 = """
.S...
XXX..
.X.XX
..X..
G...X
""".strip('\n')

meow3= """
...
SG.
...
""".strip('\n')
pprint.pprint(wire_DHD_SG1(meow))
pprint.pprint(wire_DHD_SG1(meow2))
pprint.pprint(wire_DHD_SG1(meow3))

# 'SX.\nXP.\nXXG\n' should equal
# 'SX.\nXP.\nXXG'
