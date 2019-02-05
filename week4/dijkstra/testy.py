import sys


def extract_min(visited, dist):
    min_vertex = len(dist)
    min_distance = float('inf')

    for v in range(len(dist)):
        if not visited[v] and dist[v] < min_distance:
            min_vertex = v
            min_distance = dist[v]

    return min_vertex


def distance(adj, cost, s, t):
    vertices = len(adj)
    dist = float('inf') * vertices
    visited = [False] * vertices
    dist[s] = 0

    for _ in range(vertices - 1):
        v = extract_min(visited, dist)
        if v == vertices:
            break
        visited[v] = True
        i = 0  # magic variable
        for u in adj[v]:
            if not visited[u] and dist[u] > dist[v] + cost[v][i]:
                dist[u] = dist[v] + cost[v][i]
            i += 1

    return dist[t] if dist[t] != float('inf') else -1
