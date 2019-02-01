adjacency_list = {1:[2], 4:[1], 2:[3], 3:[1]}

def distance(adj, s, t):
    #write your code here
    dist = [len(adj)] * len(adj)
    dist[s] = 0
    queue = []
    queue.append(s)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == len(adj):
                queue.append(v)
                dist[v] = dist[u] + 1
    if dist[t] != len(adj):
        return dist[t]
    return -1

distance(adjacency_list, 2,4)
