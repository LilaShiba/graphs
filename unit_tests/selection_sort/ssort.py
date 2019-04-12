arr = [8, 12, 28, 38, 49, 79, 2, 42, 100, 49, 75, 4, 56, 56, 100, 15, 67, 69, 95, 41, 54, 16, 22, 83, 24, 72, 0, 79, 41, 73, 10, 38, 6, 74, 47, 94, 29, 92, 7, 80, 80, 81, 95, 87, 30, 57, 49, 36, 69, 12, 73, 21, 98, 23, 9, 59, 64, 27, 3, 19, 2, 38, 63, 83, 32, 11, 0, 18, 49, 9, 34, 8, 94, 83, 37, 68, 47, 20, 0, 64, 96, 69, 49, 40, 70, 93, 62, 98, 91, 67, 81, 25, 85, 80, 8, 22, 71, 37, 89, 35]
def s_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

                # Swap the found minimum element with
                # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(s_sort(arr))
