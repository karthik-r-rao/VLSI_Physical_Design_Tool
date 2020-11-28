"""
@author: karthikrao

Perform routing.
"""

import copy
from get_path import *

def route(layout, edges):
    """

    Parameters
    ----------
    layout : dict
    edges : list
        Contains edges of the netlist's graph.

    Returns
    -------
    paths : list
        All the routed wires.

    """
    layout1 = copy.deepcopy(layout)
    
    for key in list(layout.keys()):
        layout[key] = [x//10 for x in layout[key]]
        
    occupied = []
    for val in list(layout.values()):
        occupied.append([x//10 for x in val])
    
    vacant = []
    x, y = get_boundaries_routing(layout)
    for k in range(6):
        for i in range(x):
            for j in range(y):
                if [k, i, j] not in occupied:
                    vacant.append([k, i, j])
    count = 0
    paths = []
    for edge in edges:
        u, v = edge
        path = find_path(layout[u], layout[v], layout, vacant)
        if len(path):
            count+=1
            paths.append(path)
        
    if count==len(edges):
        print("Routing successful!\n")
    else:
        print("Routing Failed! Go back to placement again.")
        print(f'{count} out of {len(edges)} routed successfully.')
        
    return paths, layout1