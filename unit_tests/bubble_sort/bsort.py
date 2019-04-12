def bubble_sort(arr):
    length = len(arr)
    for x in range(length):
        for y in range(length-1):
            if len(arr[y]) > len(arr[y+1]):
                arr[y], arr[y+1] = arr[y+1], arr[y]
    return arr

print(bubble_sort(['werwerwer','sdfsdfsdf','ewrwegfgrt4 4t435 2345', '235g wer fsd er sdf e', '25 gfs3 235 ']))
