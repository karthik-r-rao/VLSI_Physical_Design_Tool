"""
@author: karthikrao

Write graph info to .txt files.

"""

import networkx as nx

def write_graph_info(g, w, h, inputs):
    """

    Parameters
    ----------
    g : Networkx undirected graph.
        Graph of the netlist.
    w : dict
        Contains approx. width of each gate in the netlist.
    h : dict
        Contains approx. height of each gate in the netlist.
    inputs: list
        Contains input nodes to the circuit.

    Returns
    -------
    None.

    """
    
    nodes = list(g.nodes(data=False))
    edges = list(g.edges())

    f = open('graph_edges.txt', 'w')
    for edge in edges:
        u,v = edge
        f.write(f"{u},{v}\n")
    f.close()
    
    f = open('graph_nodes.txt', 'w')
    for node in nodes:
        f.write(f"{node}\n")
    f.close()
    
    f = open('widths.txt', 'w')
    print(w, file=f)
    f.close()
    
    f = open('heights.txt', 'w')
    print(h, file=f)
    f.close()
    
    f = open('inputs.txt', 'w')
    for node in inputs:
        f.write(f"{node}\n")
    f.close()
