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

def merge_sort(arr, pos):
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]

        merge_sort(l_half, pos)
        merge_sort(r_half, pos)

        li = ri = k = 0
        # two pointers to stitch together new array
        while li < len(l_half) and ri < len(r_half):
            if l_half[li][pos] < r_half[ri][pos]:
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

def divide_conquer(arr_x):
    if len(arr_x) <= 3:
        return brute_force(arr_x)
    else:
        # Begin to sort into two sub lists p & q sorted by x cords
        # midpoint in arr as whole number
        mid = len(arr_x)//2
        p = arr_x[:mid]
        q = arr_x[mid:]


       # Divide

        d1 = divide_conquer(p)
        d2 = divide_conquer(q)
        # dirty hobits
        if d1 == None:
          d1 = ((100000000000, 100000000000), (100000000000, 100000000000))
        if d2 == None:
          d2 = ((100000000000, 100000000000), (100000000000, 100000000000))

        print(d2)

        d = min(d1,d2)
        #return d
        # merge_sort
        sy = merge_sort(arr_x,1)
        best = 100000000
        for i in range(len(sy)-1):
            for j in range(i+1, len(sy)):
                pp,qq = sy[i], sy[j]
                dst = (abs(sy[i][0]-sy[j][0]) + abs(sy[i][1]-sy[j][1]))
                if dst < best:
                    best = dst
                    pts = (sy[i], sy[j])
        return pts


        # find closest point


        # solve subproblems





def closest_pair(points):
    if len(points) <= 3:
        # no need for divide_conquer if n < 4
        return brute_force(points)
    else:
        # preprocess arrays to make life easier and faster
        # sort by x cords & sort by y cords
        arr_x = list(points)
        arr_y = list(points)
        # Do everything yourself because otherwise what do you learn?
        # Run merge sort as it is O(nlogn)
        # pass in arr and pos of where to sort, e.g. x or y
        sorted_x = merge_sort(arr_x,0)
        sorted_y = merge_sort(arr_y,1)

        # the pythonic way
        #sorted_x.sort(key=lambda x: x[0])
        #sorted_y.sort(key=lambda x: x[1])

        # Basic visual test passes
        # print(sorted_x)
        # print(sorted_y)

        # pass the dirty work to
        return divide_conquer(sorted_x)
