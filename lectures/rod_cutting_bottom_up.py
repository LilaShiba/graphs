def knapsack(c,weight,value):
    table = [0] * (c + 1)
    ans = 0

    for i in range(c + 1):
        for j in range(len(value)):
            # do you have weight left
            if weight[j] <= i:
                table[i] = max(table[i], table[i-weight[j]] + value[j])
    return table[c]


c = 15
w = [5, 10, 15]
v = [10, 30, 20]
print(knapsack(c,w,v))
