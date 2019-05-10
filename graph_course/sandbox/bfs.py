graph = {1:[3], 4:[2], 2:[3], 3:[4]}

# return list of shortest paths
def bfs_shortest_path(adj, start):
    level = {start: 0}
    parent = {start: 0}
    i = 1
    frontier = [start]

    while frontier:
        to_explore = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    to_explore.append(v)
        frontier.remove(u)
        frontier = to_explore
        i += 1
    return level

print(bfs_shortest_path(graph, 1))
