def pos_average(s):
    values = s.split(", ")
    count, total = 0, 0
    for i in range(len(values)-1):
        for j in range(i+1,len(values)):
            for k in range(len(values[i])):
                if values[i][k] == values[j][k]:
                    count += 1
                total += 1
    return count / total * 100



    # matrix = []q
    # temp_arr = []
    #
    # for x in range(len(s)):
    #     if s[x] != ',':
    #         temp_arr.append(int(s[x]))
    #     else:
    #         matrix.append(temp_arr)
    #         temp_arr = []
    # matrix.append(temp_arr)
    #
    #
    # #
    # # count = 0
    # # s1 = []
    # # print(len(matrix))
    # # for r in range(len(matrix)):
    # #     for x in range(len(matrix[r])):
    # #         s1.append(matrix[x][count])
    # #     count += 1
    # #     print(s1)
    # #     s1 = []
    # average_pos_count = 0
    # count = 0
    # temp_arr = []
    # while count < len(matrix[0]):
    #     for row in range(len(matrix)):
    #         temp_arr.append(matrix[row][count])
    #
    #     # get count
    #     my_dict = {0:0, 4:0, 6:0, 9:0}
    #
    #     for x in temp_arr:
    #         my_dict[x] = 1 + my_dict[x]
    #
    #     my_new_dict = {k:v for (k,v) in my_dict.items() if v >= 2}
    #     average_pos_count = average_pos_count + len(my_new_dict)
    #     print(average_pos_count)
    #
    #     temp_arr = []
    #     count += 1
    #
    # return average_pos_count/30



test1 = "6900690040, 4690606946, 9990494604 "
# 26.6666666667

#
# 6900690040
# 4690606946
# 9990494604

print(pos_average(test1))

# 466960
# 069060
# 494940
# 060069
# 060090
# 640009
# 496464
# 606900
# 004000
# 944096
