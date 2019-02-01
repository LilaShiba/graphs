graph1 = {
    'A' : ['B','E'],
    'B': ['C'],
    'C': ['D'],
    'D': [],
    'E': ['D']

}
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
    dfs(graph1, 'A', visited,ordered)
    ordered.reverse()
    print(ordered)

topo(graph1)
