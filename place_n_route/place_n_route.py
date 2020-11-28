"""
@author: karthikrao

Placement and routing performed on the obtained floorplan.

"""

import ast
from get_initial_placement import *
from get_boundaries import *
from construct_graph import *
from simulated_annealing_placement import *
from get_cost_placement import *
from draw_layout import *
from get_path import *
from route import *
from draw_routed_layout import *

f = open('graph_edges.txt', 'r')
edges = f.readlines()
for i in range(len(edges)):
    u, v = eval(edges[i])
    edges[i] = (str(u), str(v))
f.close()

f = open('graph_nodes.txt', 'r')
nodes = f.read().split('\n')
del nodes[-1]
f.close()

g = construct_graph(nodes, edges)

f = open('widths.txt', 'r')
w = f.read()
w = ast.literal_eval(w)
f.close()

f = open('heights.txt', 'r')
h = f.read()
h = ast.literal_eval(h)
f.close()

f = open('partition1.txt', 'r')
partition1 = f.read().split('\n')
del partition1[-1]
f.close()

f = open('partition2.txt', 'r')
partition2 = f.read().split('\n')
del partition2[-1]
f.close()

f = open('floorplan1.txt', 'r')
layout1 = f.read()
layout1 = ast.literal_eval(layout1)
f.close()

f = open('floorplan2.txt', 'r')
layout2 = f.read()
layout2 = ast.literal_eval(layout2)
f.close()


####################
####################
# PARTITION 1
####################
####################

"""
Placement done on partition 1.

"""

l1 = {}
for key in list(layout1.keys()):
    if key[0] == 't':
        continue
    else:
        l1[key] = layout1[key]
l1 = get_initial_placement(l1)

x1, y1 = get_boundaries(l1)

vacant = []
for i in range(0, x1, 10):
    for j in range(0, y1, 10):
        vacant.append([i, j])
occupied = []
for key in list(l1.keys()):
    if key[0] == 't':
        continue
    else:
        occupied.append(l1[key])
        vacant.remove(l1[key])
        

g1 = g.subgraph(list(l1.keys()))
nodes1 = list(g1.nodes(data=False))
edges1 = list(g1.edges())

print(f'\n\nInitial Cost:{get_cost_placement(l1, edges1)}')
draw_layout(l1, w, h)
print('\n\n')

final, vacant, occupied = sim_annealing_placement(l1, vacant, occupied, edges1)

print(f'Final Cost:{get_cost_placement(final, edges1)}')
draw_layout(final, w, h)
print('\n\n')

f = open('placement_initial_p1.txt', 'w')
print(l1, file=f)
f.close()

f = open('placement_final_p1.txt', 'w')
print(final, file=f)
f.close()

"""
Routing performed on placed layout of partition 1.

"""

paths, final = route(final, edges1)
# calculate path cost
cost=0
for path in paths:
    x, y, z = path[0]
    x1, y1, z1 = path[-1]
    cost+=(abs(x-x1) + abs(y-y1) + abs(z-z1))*10
print(f'Routing Cost for partition 1: {cost}')
draw_routed_layout(final, paths, w, h)


####################
####################
# PARTITION 2
####################
####################

"""
Placement done on partition 2.

"""

l2 = {}
for key in list(layout2.keys()):
    if key[0] == 't':
        continue
    else:
        l2[key] = layout2[key]
l2 = get_initial_placement(l2)

x2, y2 = get_boundaries(l2)

vacant = []
for i in range(0, x2, 10):
    for j in range(0, y2, 10):
        vacant.append([i, j])
occupied = []
for key in list(l2.keys()):
    if key[0] == 't':
        continue
    else:
        occupied.append(l2[key])
        vacant.remove(l2[key])
        

g2 = g.subgraph(list(l2.keys()))
nodes2 = list(g2.nodes(data=False))
edges2 = list(g2.edges())

print(f'\n\nInitial Cost:{get_cost_placement(l2, edges2)}')
draw_layout(l2, w, h)
print('\n\n')
   
final, vacant, occupied = sim_annealing_placement(l2, vacant, occupied, edges2)

print(f'Final Cost:{get_cost_placement(final, edges2)}')
draw_layout(final, w, h)
print('\n\n')

f = open('placement_initial_p2.txt', 'w')
print(l2, file=f)
f.close()

f = open('placement_final_p2.txt', 'w')
print(final, file=f)
f.close()


"""
Routing performed on placed layout of partition 2.

"""

paths, final = route(final, edges2)
# calculate path cost
cost=0
for path in paths:
    x, y, z = path[0]
    x1, y1, z1 = path[-1]
    cost+=(abs(x-x1) + abs(y-y1) + abs(z-z1))*10
print(f'Routing Cost for partition 2: {cost}')
draw_routed_layout(final, paths, w, h)