# https://www.codewars.com/kata/path-finder-number-3-the-alpinist/train/python
# Bellman Ford
import pprint
# returns x,y,weight
#def find_neighbors(maze, node):
    # x,y = node
    # length = len(maze)
    # neighbors = []
    # for x,y in (x, y-1), (x, y+1), (x-1, y), (x+1,y):
    #     if 0<= x < length and 0<= y < length:
    #         weight = maze[x][y]
    #         neighbors.append([x,y,weight])
    # return neighbors


def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    level = {s: 0}
    parent = {s: 0}
    c = 1
    frontier = [s]
    count = 0

    while frontier:
        next = []

        for u in frontier:
            x,y = u
            greedy_boy = dict()
            parent_node = int(matrix[x][y])
            px, py, = x, y
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length:
                    if (x,y) not in level:
                        # add (x,y)
                        level[(x,y)] = c
                        # check end case
                        child_node = int(matrix[x][y])

                        if parent_node > child_node:
                            new_num = parent_node - child_node
                            greedy_boy[(x,y)] = new_num

                        else:
                            greedy_boy[(x,y)] = child_node - parent_node

                        if (x,y) == t:

                            if child_node > parent_node:
                                return count + child_node
                            elif child_node <= parent_node:
                                return count + child_node



            i,j = min(greedy_boy.keys(), key=(lambda k: greedy_boy[k]))

            print(greedy_boy)
            parent_node = int(matrix[px][py])
            child_node = greedy_boy[(i,j)]

            count += child_node

            # if child_node > parent_node:
            #     count = count + child_node
            # elif child_node <= parent_node:
            #     count = count + child_node


            next.append((i,j))


        frontier = next
        c += 1
    print(count)





f = "\n".join([
  "777000",
  "007000",
  "007000",
  "007000",
  "007000",
  "007777"
])

c = "\n".join([
  "010",
  "101",
  "010"
])

g = "\n".join([
  "000000",
  "000000",
  "000000",
  "000010",
  "000109",
  "001010"
])

e = "\n".join([
  "700000",
  "277773",
  "077770",
  "077770",
  "077770",
  "000007"
])
print(path_finder(c))
