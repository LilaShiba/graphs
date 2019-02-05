def dfs_visit(parent, adj, s):
    for node in adj[s]:
        if node not in parent:
            parent[node] = s
            dfs_visit(parent, adj, node)

def dfs(node, adj):
        parent = []
        for s in node:
            if s not in parent:
                parent[s] = None
                dfs_visit(parent, adj, s)
