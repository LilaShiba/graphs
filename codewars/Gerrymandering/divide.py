import pprint
wins_total = 0
o_amount = 4
def get_district(matrix, points, num):
    global wins_total
    global o_amount
    x,y = points
    count = [0,0]
    last = []
    local_o = 0

    if matrix[x][y] == 'O':
        count[0] += 1

    elif matrix[x][y] == 'X':
        count[1] += 1

    matrix[x][y] = num

    queue = [points]
    while queue:
        node = queue.pop(0)
        x,y = node
        neighbors = ( (x+1,y), (x-1,y), (x,y+1), (x,y-1) )
        real_neighbors = ( (x,y) for (x,y) in neighbors if 0<= x < 5 and 0<= y < 5 )

        for cx,cy in real_neighbors:
            if matrix[cx][cy] == 'O' and count[0] + count[1] < 5 and count[0] < o_amount:

                count[0] += 1
                matrix[cx][cy] = num
                queue.append((cx,cy))
                local_o +=1
                if count[0] == 3:
                    wins_total += 1
                if local_o == 4:
                    o_amount = 3

            elif matrix[cx][cy] == 'X' and count[0] + count[1] < 5:
                count[1] += 1
                matrix[cx][cy] = num
                queue.append((cx,cy))

    return matrix



def gerrymander(s):
    # make matrix
    global wins_total
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
    p1_ans = get_district(unchecked_nodes, p1, num)
    p2_ans = get_district(p1_ans, p2, 2)
    p3_ans = get_district(p2_ans,p3,3)
    p4_ans = get_district(p3_ans,p4,4)
    p5_ans = get_district(p4_ans,p5,5)
    pprint.pprint(p5_ans)
    return(p5_ans)
    # ans = []
    # for x in loop:
    #     new_x = ''.join(x)
    #     ans.append(new_x)
    # ans = '\n'.join(ans)
    # return ans




test1 =[
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX',
		'OOXXX'
        ]

test2 = [
    'XOXOX',
    'OXXOX',
    'XXOXX',
    'XOXOX',
    'OOXOX'
    ]
print(gerrymander(test2))
