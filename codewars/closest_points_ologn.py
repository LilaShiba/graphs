import math
# todo o nlogn time
# merge sort to build up to this
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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]

        merge_sort(l_half)
        merge_sort(r_half)

        li = ri = k = 0

        while li < len(l_half) and ri < len(r_half):
            if l_half[li] < r_half[ri]:
                arr[k] = l_half[li]
                li +=1
            else:
                arr[k] = r_half[ri]
                ri +=1
            k+=1
        # the invarient is that you merge two sorted lists
        # so, this makes sure you merge both lists brah
        while li < len(l_half):
            arr[k] = l_half[li]
            li+=1
            k+=1
        while ri < len(r_half):
            arr[k] = r_half[ri]
            ri+=1
            k+=1

    return arr

def divide_conquer(points):
    mid = len(points)//2
    left_half = points[:mid)]
    right_half = points[mid:]

def closest_pair(points):
    if len(points) <= 3:
        return brute_force(points)
    else:
        arr = list(points)
        sorted_points = merge_sort(arr)
        return divide_conquer(sorted_points)







points = (
            (8, 2), # A
            (4, 8), # B
            (9, 5), # C
            (3, 3), # D
            (10, 7), # E
            (2, 4), # F
            (7, 9),
            (10,10)  # G
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



print(divide_conquer(points))
