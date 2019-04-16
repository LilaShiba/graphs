# todo o nlogn time
def closest_pair(points):
    if len(points) == 2:
        return points
    best = None
    past_score = 100
    count = 1
    for x,y in points[count-1:]:
        for i,j in points[count:-1]:
            score = abs(x - i) + abs(y -j)
            if score < past_score:
                best = ((x,y), (i,j))
                past_score = score
                #print(best)
        count +=1
    return(best)
