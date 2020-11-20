"""
@author: karthikrao

Construct a networkx graph given its vertices and edges.

"""

import networkx as nx

def construct_graph(nodes, edges):
    """

    Parameters
    ----------
    nodes : arr_like.
        List of nodes generated in parsing.
    edges : arr_like.
        List of edges (u, v) generated in parsing.
        (u, v) represents an edge from vertex u to vertex v.

    Returns
    -------
    g : Networkx undirected graph.
        Constructed graph.
        
    """

    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    return g