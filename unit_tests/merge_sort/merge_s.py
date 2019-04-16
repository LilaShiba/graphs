import random
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
            ri+=1
            k+=1
    return arr

arr = [random.randint(0,100000000) for x in range(2000)]

print(merge_sort(arr))
