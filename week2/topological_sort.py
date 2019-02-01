adjacency_list = {2:[1], 3:[2], 3:[1], 4:[3], 4:[1], 5:[2], 5:[3]}
# output ['c', 'b', 'a', 'd', 'e']
#Uses python3

def dfs(adj, used, order, node):
    if node not in used:
        used.append(node)
        try:
            for n in adj[node]:
                dfs(adj,used,order,n)
                order.append(node)
        except:
            KeyError: 2
    order.reverse()
    return order

def toposort(adj):
    used = []
    order = []
    for vertex in adj:
        if vertex not in used:
            dfs(adj, used, order, vertex)
    for x, y in adj.items():
        sink = y.pop()
        if sink not in order:
            order.append(sink)
    return order

#print(toposort(adjacency_list))

print(toposort(adjacency_list))
