#You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

#You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

#Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

#Languages
#=========

#To provide a Python solution, edit solution.py
#To provide a Java solution, edit Solution.java

#Test cases
#==========
#Your code should pass the following test cases.
#Note that it may also be run against hidden test cases not shown here.

#-- Python cases --
#Input:
#solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
#Output:
#    7

#Input:
#solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
#Output:
#    11

#-- Java cases --
#Input:
#Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})
#Output:
#    7

#Input:
#Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})
#Output:
#    11
adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def shortestPath(map, x1, y1):
    r = len(map)
    c = len(map[0])
    visited = dict()
    q = []
    q.append((x1,y1))
    visited[(x1,y1)] = 1
    shortFromStart = dict()
    shortFromStart[(x1, y1)] = 1
    while(len(q) > 0):
        l = len(q)
        for i in range(0, l):
            (x, y) = q[0]
            q.pop(0)
            for j in adj:
                adjx = x+j[0]
                adjy = y+j[1]
                if adjx >= 0 and adjx < r and adjy>=0 and adjy < c and ((adjx, adjy) not in visited):
                   shortFromStart[(adjx, adjy)] =  shortFromStart[(x, y)] + 1
                   visited[(adjx, adjy)] = 1
                   if map[adjx][adjy] == 0:
                       q.append((adjx, adjy))
    if (r-1, c-1) in shortFromStart:
        return shortFromStart[(r-1, c-1)] 
    return 10000    


def solution(map):
    r = len(map)
    c = len(map[0])
    start = (0, 0)
    shortFromStart = dict()
    visited = dict()
    shortFromBlockers = dict()
    blockers = []
    for i in range(0, r):
        for j in range(0, c):
            if int(map[i][j]) == 1:
                blockers.append((i, j))
    q = []
    q.append((0,0))
    visited[(0,0)] = 1
    shortFromStart[(0, 0)] = 1
    while(len(q) > 0):
        l = len(q)
        for i in range(0, l):
            (x, y) = q[0]
            q.pop(0)
            for j in adj:
                adjx = x+j[0]
                adjy = y+j[1]
                if adjx >= 0 and adjx < r and adjy>=0 and adjy < c and ((adjx, adjy) not in visited):
                   shortFromStart[(adjx, adjy)] =  shortFromStart[(x, y)] + 1
                   visited[(adjx, adjy)] = 1
                   if map[adjx][adjy] == 0:
                       q.append((adjx, adjy))
    
    for i in blockers:
        shortFromBlockers[i] = shortestPath(map, i[0], i[1])
    answer = 100000
    if (r-1, c-1) in shortFromStart:
        answer = shortFromStart[(r-1, c-1)]
    for i in blockers:
        if (i[0], i[1]) in shortFromStart:
            answer = min(answer, shortFromStart[i] +  shortFromBlockers[i] - 1)
    return answer

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
#print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))