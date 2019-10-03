# Kevin Nunez
# CS-335, Spring 2019

#Example_Graph
                 
Ex1_Heuristic = [100, 200, 0, 700, 600]

Ex1_Graph = [
               [(2, 300)],                         #city 0
               [(0, 200)],                         #city 1
               [],                                 #city 2
               [(1, 400), (4, 100)],               #city 3
               [(1, 200), (0, 500), (2, 1200)]     #city 4
            ]
             



 
sldRomania = [366, 0, 160, 242, 161, 178, 77, 151, 226, 244, 241, 234, 380, 98, 193, 253, 329, 80, 199, 374]
         
Romania = [
            [(15, 140), (19, 75), (16, 118)], #0  A
            [(5, 211), (13, 101), (6, 90), (17, 85)], #1  B
            [(3, 120), (14, 146), (13, 138)], #2 C
            [(10, 75), (2, 120)], #3 D
            [(7, 86)], #4 E
            [(15, 99), (1, 211)], #5 F
            [(1, 90)], #6 G
            [(17, 98), (4, 86)], #7 H
            [(11, 87), (18, 92)], #8 I
            [(16, 111), (10, 70)], #9 L
            [(9, 70), (3, 75)], #10 M
            [(8, 87)], #11 N
            [(19, 71), (15, 151)], #12 O
            [(14, 97), (2, 138), (1, 101)], #13 P
            [(15, 80), (2, 146), (13, 97)], #14 R
            [(12, 151), (0, 140), (14, 80), (5, 99)], #15 S
            [(0, 118), (9, 111)], #16 T
            [(0, 85), (7, 98), (18, 142)], #17 U
            [(8, 92), (17, 142)], #18 V
            [(12, 71), (0, 75)]  #19 Z
          ]


def priority_pop(ls):
    def last(a):
        return a[-1]
    h = list(map(last, ls))
    index = h.index(min(h))
    return(ls.pop(index))



def a_star(start, dest, sld, graph):

    q = [[start, 0, sld[start]]]
    visited = []

    while len(q) > 0:
         currentNode = priority_pop(q)
         currentCity = currentNode[-3]
         distance = currentNode[-2]
         reachable = graph[currentCity]

         if currentCity == dest:
             visited.append(currentNode)

         for edge in reachable:
             newNode = currentNode[0:-2]                                 # Grab list of current cities traveled
             nextCity = edge[0]                                          # Grab the next city
             newNode.append(nextCity)                                    # Append next city to current cities traveled
             cityEdge = edge[1]                                          # Edge to get to next city
             new_distance = distance + cityEdge                          # The distance + new edge distance
             newNode.append(new_distance)                                # Append the new distance to the node
             city_heauristic = sld[nextCity]
             heauristic = new_distance + city_heauristic
             newNode.append(heauristic)
             q.append(newNode)
         if len(q) > 200:
             break

    return visited[0]


if __name__ == "__main__":
    cityA = int(input("Enter a city between 1 - 19: "))
    cityB = int(input("Enter a city that isn't City "+ str(cityA) + ": "))
    solution = a_star(cityA, cityB, sldRomania, Romania)
    print()
    print("The fastest way from City 3 to City 2 is ", end = "")
    print(solution)
