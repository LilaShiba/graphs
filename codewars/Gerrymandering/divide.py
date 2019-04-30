import pprint
def get_district(matrix, points, num):

    x,y = points
    count = [0,0]
    last = []

    if matrix[x][y] == 'O':
        count[0] += 1
        y_count = 3
        n_count = 2

    elif matrix[x][y] == 'X':
        count[1] += 1
        n_count = 5
        y_count = 1

    matrix[x][y] = num

    queue = [points]
    t_count = 1
    while queue:

        node = queue.pop(0)
        x,y = node
        neighbors = ( (x-1,y), (x+1,y), (x,y-1), (x,y+1) )
        real_neighbors = ( (x,y) for (x,y) in neighbors if 0<= x < 5 and 0<= y < 5 )

        for cx,cy in real_neighbors:
            if matrix[cx][cy] == 'O' and count[1] < n_count and y_count <= 3:
                count[0] += 1
                matrix[cx][cy] = num
                y_count +=1
                queue.append((cx,cy))
            elif matrix[cx][cy] == 'X' and count[1] < n_count and t_count < 5:
                count[1] += 1
                matrix[cx][cy] = num
                t_count += 1
                queue.append((cx,cy))
    return matrix



def gerrymander(s):
    # make matrix
    unchecked_nodes = []
    for x in s:
        x = list(x)
        unchecked_nodes.append(x)

    # points for Voronoi clusters
    p1 = (0,0)
    p2 = (4,0)
    p3 = (4,4)
    p4 = (0,4)
    p5 = (2,2)
    num = 1
    # push from left to right
    p1_ans = get_district(unchecked_nodes, (0,0), num)
    p2_ans = get_district(p1_ans, p2, 2)
    p3_ans = get_district(p2_ans,p3,3)
    p4_ans = get_district(p3_ans,p4,4)
    p5_ans = get_district(p4_ans,p5,5)
    pprint.pprint(p5_ans)

    # ans = []
    # for x in loop:
    #     new_x = ''.join(x)
    #     ans.append(new_x)
    # ans = '\n'.join(ans)
    # return ans




example_test =[
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX'
        ]

print(gerrymander(example_test))
