def gerrymander(s):
    # transform into 2D array
    #matrix = list(map(list, s.splitlines()))

    matrix = []
    for x in s:
        x = list(x)
        matrix.append(x)

    midpoint = 13
    # solve
    #  Voronoi Approach
    #  Bowyer-Watson algorithm
    #  Fortune's algorithm




    # return ans
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
print(gerrymander(test1))
