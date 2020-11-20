"""
@author: karthikrao

Program to get graph from netlist.

"""

import networkx as nx
from get_graph import *
from write_graph_info import *

filename = 'adder.isc'  # PATH to isc file

g = get_graph(filename)
nodes = list(g.nodes(data=False))
edges = list(g.edges())

print(f"The number of nodes in the graph are: {len(nodes)}\n ")
print(f'The nodes in the graph are:\n{nodes}\n')
print(f"The number of edges in the graph are: {len(edges)}\n ")
print(f'The edges in the graph are:\n{edges}\n')

write_graph_info(g) # Writes files to current working directory
