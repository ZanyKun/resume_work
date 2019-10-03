# Kevin Nunez
# CS-335, Spring 2019
# Asst 4

import random


def hillClimbClique(n, k, graph):  # returns best state found

    state = getRandomState(n, k)
    h = getHeuristic(n, k, state, graph)
    print("Current Heuristic: ", h)
    nextState = getBestNeighbor(n, k, state, graph)
    print("Next state: ", nextState)
    hNext = getHeuristic(n, k, nextState, graph)
    print("Next Heuristic: ", hNext)
   
    while hNext > h:
        state = nextState
        h = hNext
        nextState = getBestNeighbor(n, k, state, graph)
        hNext = getHeuristic(n, k, nextState, graph)

    return state


###########################################
def getRandomState(n, k):  # returns random list of k verties (between 0 and n - 1)
    random_state = []

    while len(random_state) < k:
       v = random.randint(0, n - 1)
       if v not in random_state:
          random_state.append(v)

    print("Random State: ", random_state)
    return random_state


###########################################
def getHeuristic(n, k, state, graph):   # returns the number of conflicts in "state" given the graph

    count = 0

    for i in range(k):
       for j in range(i + 1, k):
          if graph[state[i]][state[j]] == 1:
             count += 1

    return count


###########################################
def getBestNeighbor(n, k, state, graph):  # returns the neighbor of "state" with the fewest conflicts.
    number_list = []
    for i in range(n):
        number_list.append(i)                                # Number list of every number between 0 and n

    best_neighbor = None                                     # Best Neighbor variable to be returned
    min_h = 0                                                # Minimum heuristic calculated to get the best neighbor

    for i in range(len(state)):
        copy = list(state)                                   # Copies the current state being checked
        for j in range(len(number_list)):
            if j not in state:                               # If j is not in the current state
                copy[i] = j                                  # Number at copy[i] is replaced by j to create a new state
                h_next = getHeuristic(n, k, copy, graph)     # Gets heuristic of new state
                if min_h == 0:                               # Sets min_h to first heuristic for comparison
                    min_h = h_next
                if h_next <= min_h:                          # If h_next is smaller than min_h
                    min_h = h_next                           # Changes min_h to new heuristic
                    best_neighbor = list(copy)               # Changes best_neighbor to copy but the element is
                                                             # changed to the last copy element by end of for-loop

    return best_neighbor
