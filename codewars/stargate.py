import pprint, heapq, math
def wire_DHD_SG1(existingWires):
    matrix =  list(map(list, existingWires.splitlines()))
    length = len(matrix)
    # get start node O(n)
    count = 0
    for x in matrix:
        try:
            pos = x.index('S')
            break
        except:
            pos = None
        count +=1
    # get goal node O(n)
    gx = 0
    for x in matrix:
        try:
            gy = x.index('G')
            break
        except:
            gy = None
        gx +=1

    s = [(0,count,pos)]
    heapq.heapify(s)
    parent = {}
    weight = {(count,pos):0}
    i = 1
    # dijkstra O(E log V)
    while s:
        heapq.heapify(s)
        minNode = heapq.heappop(s)

        current_weight,x,y = minNode
        px,py = x,y
        # end case here
        if matrix[x][y] == 'G':
            currentNode = (gx,gy)
            while currentNode != (count,pos):
                cx,cy = currentNode
                matrix[cx][cy] = 'P'
                currentNode = parent[currentNode]
                matrix[gx][gy] = 'G'
                matrix[count][pos] = 'S'
            strg = ''
            for x in matrix:
                x = ''.join(x)
                strg+= x + '\n'
                strg = str(strg)

            return strg[:-1]

        directions = ((x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1,y-1), (x+1, y+1), (x-1,y+1), (x+1,y-1))
        real_neighbors = ((x,y) for (x,y) in directions if 0<= x < length and 0<= y < len(matrix[0]))

        for cx, cy in real_neighbors:
            weight_c = current_weight +( math.sqrt((cx - gx)**2 + (cy - gy)**2))
            if ((cx,cy) not in parent or weight_c <= weight[(cx,cy)]) and matrix[cx][cy] != 'X':
                        parent[(cx,cy)] = (px,py)
                        weight[(cx,cy)] = weight_c
                        s.append((weight_c,cx,cy))


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
