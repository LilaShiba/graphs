graph = {
            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

def bellmanford(graph, start):
    dist = {}
    for v in graph:
        dist[v] = float('Inf')
    dist[start] = 0

    unseenNodes = graph
    # relax baby
    for i in range(len(graph)-1):
        for u in unseenNodes:
            print('i am u',dist[u])
            for v,w in graph[u].items():
                if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    #return dist
    # check for negative cycles
    for u in unseenNodes:
        for v,w in graph[u].items():
            if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                return 'you got a negative cycle oooweee', dist
    return dist

print(bellmanford(graph, 's'))
