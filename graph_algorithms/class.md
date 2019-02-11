# Comp Sci 1


## Weekly programming Homework
- Review
- New Problem


# Class
- REPO Link [Flask intro](https://github.com/kyle1james/flask_boiler)
- Parse data
- Bootstrap
- Idea's for new app


# TODO's
- UX wire frame
- Logic diagrams via IB examples


---
# Comp Sci 2
2/11
## Monday
- Make up quiz
- IA work day (due 3/1)

## Tuesday
- Review quiz
- pseudocode

## Wednesday
- Paper 3 Review

## Thursday
- IA work day

---
2/4
# Warm Up
Create a function that will find the neighbors in level one of a given node

```python
matrix = [[2, 2, 8, 1, 5], [10, 6, 1, 8, 7], [9, 8, 8, 2, 7], [0, 5, 6, 10, 3], [1, 3, 0, 3, 10]]
```
---
# BFS Shortest Path
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'[1]), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

### G = (V, E)

### Tree
is an undirected graph that is connected and acyclic
A tree on n vertices has n-1 edges

### Tree
G(V, E) with |E| = |V| - 1

![BFS](bfs.gif)

### items in slack
[problem set](https://www.codewars.com/kata/5765870e190b1472ec0022a2)

[MIT Notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec13.pdf)

![maze](maze.gif)
---
# Homework
- Vocabulary + pseudocode quiz

## Vocabulary
- memory data register
- machine execution cycle
- memory management function of an operating system
- linked list
- binary tree
- tree
- collection
- array
- interrupt
- concurrent processing
- control system
- Web 2.0
- Semantic Web
- IP
- TCP
- FTP
- HTTP
- HTTPs
- URL
- DNS
- Web Browser
- WLAN
- VPN
---
## BFS Answer

```python
matrix = [[2, 2, 8, 1, 5], [10, 6, 1, 8, 7], [9, 8, 8, 2, 7], [0, 5, 6, 10, 3], [1, 3, 0, 3, 10]]

def path_finder(a):
    matrix = list(map(list, a.splitlines()))
    length = len(matrix)
    s = (0,0)
    t = (length - 1,length - 1)
    level = {s: 0}
    parent = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            x,y = u
            for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= x < length and 0 <= y < length:
                    if (x,y) not in level and matrix[x][y] != 'W':
                        level[(x,y)] = i
                        parent[(x,y)] = u
                        next.append((x,y))
                        if (x,y) == t:
                            return level[(x,y)]
        frontier = next
        i += 1
    return False


print(distance(maze))
```
