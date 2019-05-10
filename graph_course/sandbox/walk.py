bell = {
            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

bfsg = {1:[3], 4:[2], 2:[3], 3:[4]}

def bfs(adj,node):
    parent = {node:0}
    level = {node:0}
    # keep track of level
    l=1
    frontier = [node]

    while frontier:
        to_explore = []
        for u in frontier:
            # explore neighbors
            for v in adj[u]:
                # if not explore
                if v not in level:
                    level[v] = l
                    parent[v] = u
                    to_explore.append(u)
        frontier.remove(u)
        frontier = to_explore
        l+=1
    return level
print(bfs(bfsg, 1))

def bellman_ford(adj,start):
    dist = {}
    for v in adj:
        dist[v] = float('Inf')
    dist[start] = 0

    unseenNodes = adj

    for i in range(len(adj)-1):
        for u in unseenNodes:
            for v,w in adj[u].items():
                if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist

print(bellman_ford(bell,'a'))
