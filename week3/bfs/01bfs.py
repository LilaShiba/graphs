#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec13.pdf
adjacency_list = {1:[3], 4:[1], 2:[3], 3:[4]}

def distance(adj, s, t):
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
                    if v == t:
                        #return parent
                        path = list(parent.values())
                        path.append(t)
                        path.pop(0)
                        return path

        frontier = next
        i += 1
    return - 1


print(distance(adjacency_list, 1,4))
