"""
@author: karthikrao

Construct a networkx graph given its vertices and edges.

"""

import networkx as nx

def construct_graph(nodes, edges):
    """
        construct_graph(nodes, edges)
        
        Parameters
        ----------
        nodes : List of nodes. 
        edges : List of edges.
        
        Returns
        ----------
        g : Networkx undirected graph. 
    """

    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    return g
