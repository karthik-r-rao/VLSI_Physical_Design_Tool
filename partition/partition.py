"""
@author: karthikrao

Program to partition a netlist into two parts.

"""

import networkx as nx
import matplotlib.pyplot as plt
from construct_graph import *
from kernighan_lin_bisection import *
from write_partitions import *

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

a,b = get_init_partition(list(g.nodes(data=False)))
print(f'Initial Partition1: {a}')
print(f'Initial Partition2: {b}')
count = compute_cutsize(g, a, b)
print("Initial Cutsize:", count)
print("\n")

color_map = []
for i in range(len(nodes)):
    if i<18:
        color_map.append('cyan')
    else:
        color_map.append('yellow')

pos = nx.shell_layout(g)
for i in b:
    pos[i][0]+=3
    
plt.figure(figsize=(12,12))
nx.draw_networkx(g, pos, with_labels=True, node_color=color_map, font_weight='bold', node_size=500)
plt.title('Initial Partition')
plt.savefig('init_partition.png')

a, b = kernighan_lin_bisection(g) 
print(f'Final Partition1: {a}')
print(f'Final Partition2: {b}')
count = compute_cutsize(g, a, b)
print("Final Cutsize:", count)

write_partitions(a, b)

pos = nx.shell_layout(g)
for i in b:
    pos[i][0]+=3
    
plt.figure(figsize=(12,12))
nx.draw_networkx(g, pos, with_labels=True, node_color=color_map, font_weight='bold', node_size=500)
plt.title('Final Partition')
plt.savefig('final_partition.png')