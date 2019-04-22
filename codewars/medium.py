def brute_force(points):
    if len(points) == 2:
        return points
    best = None
    past_score = 100
    count = 1
    for x,y in points[count-1:]:
        for i,j in points[count:-1]:
            # manhattan distance
            score = abs(x - i) + abs(y -j)
            # euclidean distance
            #score = math.sqrt( (x-i)**2 + (y-j)**2 )
            if score < past_score:
                best = ((x,y), (i,j))
                past_score = score
                #print(best)
        count +=1
    return(best)

def divide_conquer(ax, ay):
    length = len(ax)
    # base case
    if length <=3:
        return brute_force(ax)

    mid = length // 2
    qx = ax[:mid]
    rx = ax[mid:]

    # get midpoint
    midpoint = ax[mid][0]
    qy = list()
    ry = list()

    for x in ay:
        if x[0] <= midpoint:
            qy.append(x)
        else:
            ry.append(x)

    # divide
    (p1,q1,mi1) = divide_conquer(qx,qy)
    (p2,q2,mi2) = divide_conquer(rx,ry)

    # conquer
    if mi1 <= mi2:
        d = mi1
        mn = (p1,q1)
    else:
        d = mi2
        mn = (p1,q1)
    (p3,q3,mi3) = closest_split_pair(ax,ay,d,mn)

    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3
def closest_pair(points):
    ax = sorted(points, key=lambda x: x[0])  # Presorting x-wise
    ay = sorted(points, key=lambda x: x[1])  # Presorting y-wise
    p1, p2, mi = divide_conquer(ax, ay)  # Recursive D&C function
    return p1,p2
