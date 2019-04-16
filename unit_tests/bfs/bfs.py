import random
def bfs(maze, start, target):
    length = len(maze)
    frontier = [start]
    end = target
    explored = {}
    found_path = False

    while frontier:

        for u in frontier:
            x,y = u
            directions = ((x+1,y), (x-1,y), (x, y+1), (x,y-1))
            real_directions = ((x,y) for (x,y) in directions if 0<= x <length and 0<=y<length)
            for cx,cy in real_directions:
                if (cx,cy) not in explored and maze[cx][cy] != 1:
                    explored[(cx,cy)] = (x,y)
                    frontier.append((cx,cy))

                    if (cx,cy) == end:
                        current_node = end
                        path = []
                        while current_node != start:
                            path.insert(0, current_node)
                            current_node = explored[current_node]
                        return path
            frontier.remove((x,y))


    return False




maze = [[random.randint(0,100)for x in range(10)]for y in range(10)]
print(bfs(maze, (0,0),(9,9)))
