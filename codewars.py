    for row in range(len(matrix)):
        for col in range(len(matrix)):
            adj[(row,col)] = find_neighbors(matrix, (row,col))
            current = adj[(row,col)]


    unseenNodes = adj
    print(shortest_distance)

    # search time
    while unseenNodes:
        minNode = None
        # grab first unseenNode
        for node in unseenNodes:
            # set minNode
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
        # check neighbors
        for x,y,weight in adj[minNode]:
            weight = int(weight)
            child_node = x,y

            # relax
            if weight + shortest_distance[minNode] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[minNode]
                # increase minNode for each level
                predecessor[(x,y)] = minNode
                #print(minNode)









f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

e = "\n".join([
  "277773",
  "777000",
  "077770",
  "077770",
  "077770",
  "000007"
])
print(path_finder(e))
