"""
@author: karthikrao

Perform floorplanning on the partitioned netlist.

"""

import matplotlib.pyplot as plt
import ast
from simulated_annealing_FP import *
from generate_polish_exp import *
from get_coordinates_FP import *
from get_patches_FP import *

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


init1 = generate_polish_exp(partition1)
init_cost1, _, _ = get_cost_FP(init1, w, h)
print(f'Initial Polish Expression for partition 1:\n {init1}\n')
print(f'Initial Cost for partition 1: {init_cost1}\n')

sol1, costs1 = simulated_annealing_FP(init1, w, h)

print(f'Final Polish Expression for partition 1:\n {sol1}\n')
print(f'Final Cost for partition 1: {min(costs1)}\n')
print('\n\n')

init2 = generate_polish_exp(partition2)
init_cost2, _, _ = get_cost_FP(init2, w, h)
print(f'Initial Polish Expression for partition 2:\n {init2}\n')
print(f'Initial Cost for partition 2: {init_cost2}\n')

sol2, costs2 = simulated_annealing_FP(init2, w, h)

print(f'Final Polish Expression for partition 2:\n {sol2}\n')
print(f'Final Cost for partition 2: {min(costs2)}\n')


fig = plt.figure(figsize=(10,10)) 
ax = fig.add_subplot(111)
patches1 = get_patches_FP(init1, w, h, 0)
patches2 = get_patches_FP(init2, w, h, 1)
patches = patches1+patches2
for patch in patches:
    ax.add_patch(patch[0])
    rx, ry = patch[0].get_xy()
    cx = rx + patch[0].get_width()/2.0
    cy = ry + patch[0].get_height()/2.0
    ax.annotate(patch[1], (cx, cy), color='black', weight='bold', ha='center', va='center')
plt.title('Initial Floorplan')
plt.xlim([0, 150])
plt.ylim([0, 150])
plt.savefig('initial_FP.png')
plt.show()

fig = plt.figure(figsize=(10,10)) 
ax = fig.add_subplot(111)
patches1 = get_patches_FP(sol1, w, h, 0)
patches2 = get_patches_FP(sol2, w, h, 1)
patches = patches1+patches2
for patch in patches:
    ax.add_patch(patch[0])
    rx, ry = patch[0].get_xy()
    cx = rx + patch[0].get_width()/2.0
    cy = ry + patch[0].get_height()/2.0
    ax.annotate(patch[1], (cx, cy), color='black', weight='bold', ha='center', va='center')
plt.title('Final Floorplan')
plt.xlim([0, 150])
plt.ylim([0, 150])
plt.savefig('final_FP.png')
plt.show()

f = open('floorplan1.txt', 'w')
print(get_coordinates_FP(sol1, w, h, 0), file=f)
f.close()

f = open('floorplan2.txt', 'w')
print(get_coordinates_FP(sol2, w, h, 1), file=f)
f.close()

plt.plot(costs1)
plt.title('Cost vs iteration for partition 1')
plt.show()

plt.plot(costs2)
plt.title('Cost vs iteration for partition 2')
plt.show()