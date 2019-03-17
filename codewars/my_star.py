from heapq import heappush, heappop

def path_finder(maze):
    matrix =  list(map(list, a.splitlines()))
    start = (0,0)
    length = len(matrix)
    goal = (length-1,length-1)

    to_be_expanded = []
    heappush(to_be_expanded, (manhattan_distance(start, goal), 0, 0, start))
    tree = set()






f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

print(path_finder(f))
