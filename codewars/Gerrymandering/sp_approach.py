def dij_win(graph, num, start):
    dist_num = num
    length = len(graph)
    parent = {}
    visited = {(0,0):0}
    # x,y, 1= not voter 0= voter
    sx,sy = start
    start = (sx,sy,0)
    unexplored = [start]
    voters = 0
    nonvoters = 0

    if graph[sx][sy] == 'O':
        voters += 1
        graph[sx][sy] = dist_num
    elif graph[sx][sy] == 'X':
        nonvoters += 1
        graph[sx][sy] = dist_num

    while voters < 3 or nonvoters < 2:
        unexplored = sorted(unexplored, key=lambda x: x[2])
        minNode = unexplored.pop(0)
        print(minNode)

        x,y,_ = minNode
        px,py = x,y

        neighbors = ( (x-1,y), (x+1,y), (x,y-1), (x,y+1) )
        real_neighbors = ( (x,y) for (x,y) in neighbors if 0<= x < length and 0 <= y < length)

        for cx,cy in real_neighbors:

            if graph[cx][cy] == 'O':
                cost = 0
            elif graph[cx][cy] == 'X':
                cost = 1
            else:
                cost = 2

            if cost == 0 and voters < 3:
                unexplored.append((cx,cy,cost))
                graph[cx][cy] = dist_num
                voters +=1
            elif cost == 1 and nonvoters < 2:
                unexplored.append((cx,cy,cost))
                graph[cx][cy] = dist_num
                nonvoters += 1
            else:
                pass
    print(graph)
    return graph



def gerrymander(s):
    # transform into 2D array
    matrix = []
    for x in s:
        x = list(x)
        matrix.append(x)
    one = dij_win(matrix,'1', (0,0))
    two = dij_win(one,'2',(2,2))
    three = dij_win(two,'3',(4,0))

    # solve
    #  Voronoi Approach
    #  Bowyer-Watson algorithm
    #  Fortune's algorithm




    # return ans
    ans = []
    for x in three:
        new_x = ''.join(x)
        ans.append(new_x)
    ans = '\n'.join(ans)
    return ans



example_test =[
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX'
        ]

print(gerrymander(example_test))
