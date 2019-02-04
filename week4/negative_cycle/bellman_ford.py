graph = {
            's': {'a': 1, 'b': 1},
            'a': {'s': 1, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }


def bellmanford(adj, src):
    # init dist from src as inif
    dist = {}
    for vertex in adj:
        dist[vertex] = float('inf')
    dist[src] = 0
    unseenNodes = adj

    # relax all edges
    for i in range(len(adj) - 1):
        for u in adj:
            for v, w in adj[u].items():
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
    # return(dist)
    # check for negative-weight cycles
    for u in adj:
        for v,w in adj[u].items():
            if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                print('there is a negative cycle')

bellmanford(graph, 'a')
