# def matrix_addition(a, b):
#     ans = []
#     for x in range(len(a)):
#         new_list = []
#         for y in range(len(a[x])):
#             new_list.append(a[x][y] + b[x][y])
#         ans.append(new_list)
#     return ans

#
a = [[1,2], [2,3], [0,0]]
b = [[3,4], [5,6], [0,0]]
# print(matrix_addition(a,b))

def matrix_addition(a, b):
    for x in range(len(a)):
        for y in range(len(a[x])):
            a[x][y] = (a[x][y] + b[x][y])
    return a
print(matrix_addition(a,b))
