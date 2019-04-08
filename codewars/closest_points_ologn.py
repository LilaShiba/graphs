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

points = (
            (2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
        )
#expected = ((6, 3), (7, 4))

points2 =(
                (2, 2), # A
                (2, 8), # B
                (5, 5), # C
                (5, 5), # C
                (6, 3), # D
                (6, 7), # E
                (7, 4), # F
                (7, 9)  # G
        )
#expected =((5, 5), (5, 5))



print(closest_pair(points))
