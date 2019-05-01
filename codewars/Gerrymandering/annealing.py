# https://stackoverflow.com/questions/51640083/partitioning-a-colored-grid
import random
red = 'O'
blue = 'X'
voters_per_district = 5

def get_neighbours(node):
    x,y = node
    length = 5
    neighbors = ( (x+1,y), (x-1,y), (x, y+1), (x,y-1) )
    return [ (cx,cy) for (cx,cy) in neighbors if 0 <= cx < length and 0<= cy < length ]

def start_generator(max=4):
    return (random.randint(0,max), random.randint(0,max))

def get_district_win(node, matrix):
    dist_num = '1'
    x,y = node
    h_target = matrix[x][y]
    win_votes = 0
    lose_votes = 0

    if h_target == 'O':
        win_votes += 1
        matrix[x][y] = dist_num
    else:
        return False

    queue = [node]

    while win_votes < 3 and lose_votes < 3:
        minNode = queue.pop(0)
        neighbors = get_neighbours(minNode)

        for cx,cy in neighbors:
            if matrix[cx][cy] == h_target:
                queue.append((cx,cy))
                win_votes += 1
                matrix[cx][cy] = dist_num
                if win_votes == 3:
                    break
            elif matrix[cx][cy] == 'X':
                queue.append((cx,cy))
                lose_votes += 1
                matrix[cx][cy] = dist_num

    # if win_votes
    return matrix



def gerrymander(s):
    # transform into 2D array
    #matrix = list(map(list, s.splitlines()))

    matrix = []
    for x in s:
        x = list(x)
        matrix.append(x)

    d1 = False
    while d1 == False:
        start = start_generator()
        d1 = get_district_win(start,matrix)


    # solve
    #  Voronoi Approach
    #  Bowyer-Watson algorithm
    #  Fortune's algorithm




    # return ans
    ans = []
    for x in d1:
        new_x = ''.join(x)
        ans.append(new_x)
    ans = '\n'.join(ans)
    return ans


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
print(gerrymander(test1))
