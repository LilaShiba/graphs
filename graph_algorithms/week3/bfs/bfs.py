#Uses python3

import sys
import queue

def distance(adj, s, t):
    # edges from s
    level = {s: 0}
    # keep track of predecessor
    parent = {s: None}
    # count edges
    i = 1
    # what needs to be explored
    frontier = [s]
    # loop through graph
    while frontier:
        # to be added to frontier
        next = []
        # find node
        for u in frontier:
            # find neighbors of node
            for v in adj[u]:
                # if neighbors aren't explored
                if v not in level:
                    # connected node level is dependent of distance
                    level[v] = i
                    # keep track of the parent node
                    parent[v] = u
                    # explore this neighbor later
                    next.append(v)
                    # if you reach target
                    if v == t:
                        # how many edges are between s and t
                        return level[v]
        # explore neighbors
        frontier = next
        # next level of distance
        i += 1
    # no path found
    return - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
