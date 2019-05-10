adjacency_list = {2:[1], 3:[2], 3:[1], 4:[3], 4:[1], 5:[2], 5:[3]}


def dfs(graph, node, visited,ordered):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n, visited,ordered)
        ordered.append(node)
    return ordered

def topo(graph1):
    ordered=[]
    visited=[]
    dfs(graph1, 2, visited,ordered)
    ordered.reverse()
    print(ordered)

topo(adjacency_list)
