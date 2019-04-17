import numpy
def divide_conquer(arr,arr2):
    if len(arr) == 2:
        d = (arr[0], arr[1])
    else:
        # midpoint in arr as whole number
        mid_x = len(arr)//2
        # splice x sorted arr
        r_x = arr[:mid_x]
        l_x = arr[mid_x:]
        # splice y sorted arr
        l_y = arr2[:mid_x]
        r_y = arr2[mid_x:]
        




        print(r_x, l_x)
        print(l_y, r_y)

points1 = [(2, 4), (3, 3), (4, 8), (7, 9), (8, 2), (9, 5), (10, 10), (10, 7)]
points2 = [(8, 2), (3, 3), (2, 4), (9, 5), (10, 7), (4, 8), (7, 9), (10, 10)]

print(divide_conquer(points1, points2))
