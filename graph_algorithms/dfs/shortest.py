#https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec14.pdf
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    shortest = None

    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath:
                if shortest == None or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
