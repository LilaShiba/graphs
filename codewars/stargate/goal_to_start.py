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


    s = [(0,gx,gy)]
    heapq.heapify(s)
    parent = {}
    weight = {(gx,gy):0}

    # dijkstra O(E log V)
    while s:
        minNode = heapq.heappop(s)
        print(minNode)

        current_weight,x,y = minNode
        px,py = x,y

        # end case here
        if matrix[x][y] == 'S':
            currentNode = (count,pos)
            while currentNode != (gx,gy):
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

        # relax
        directions = ((x, y-1), (x, y+1), (x-1, y), (x+1, y), (x-1,y-1), (x+1, y+1), (x-1,y+1), (x+1,y-1))
        real_neighbors = ((x,y) for (x,y) in directions if 0<= x < length and 0<= y < len(matrix[0]))

        for cx, cy in real_neighbors:
            weight_c = current_weight +( abs(count - cx) + abs(pos - cy))
            if ((cx,cy) not in parent or weight_c < weight[(cx,cy)]) and matrix[cx][cy] != 'X':
                        parent[(cx,cy)] = (px,py)
                        weight[(cx,cy)] = weight_c
                        s.append((weight_c,cx,cy))


    # Your code here!
    return "Oh for crying out loud..."
