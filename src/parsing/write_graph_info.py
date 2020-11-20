"""
@author: karthikrao

Write graph info to .txt files.

"""

import networkx as nx

def write_graph_info(g):
    """

    Parameters
    ----------
    g : Networkx undirected graph.
        Graph of the netlist.

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