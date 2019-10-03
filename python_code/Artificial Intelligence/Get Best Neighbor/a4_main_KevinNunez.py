# Kevin Nunez
# CS-335, Spring 2019
# Asst 4

from a4_aux_KevinNunez import *
from graph_12_5 import *
#from graph_200_14 import *

print()
print("Kevin Nunez")
print("CS-335, Spring 2019, Asst 4")
print()

graph = getGraph()
n = getN()
k = getK()


for i in range(1):
    soln = hillClimbClique(n, k, graph)
    h = getHeuristic(n, k, soln, graph)

