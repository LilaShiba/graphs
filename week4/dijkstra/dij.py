#https://brilliant.org/wiki/dijkstras-short-path-finder/
# https://pastebin.com/3Q9rqGHA
# https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e
graph = {
            's': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

graph2 = {
        1:{2:7, 3:5},
        2:{3:2},
        3:{}
}


def dijkstra(adj, source):
    #dist=[float('inf')]*len(adj)
    shortest_distance = {}
    predecessor = {}
    unseenNodes = adj
    path = []

    for vertex in adj:
        shortest_distance[vertex] = float('inf')
    shortest_distance[source] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in adj[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    return shortest_distance


print(dijkstra(graph,'a'))
