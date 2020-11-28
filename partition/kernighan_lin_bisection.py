"""
@author: karthikrao

Partition a graph into two blocks using the Kernighan-Lin algorithm.

"""

import numpy as np
import networkx as nx
from util import *

def get_init_partition(nodes):
    """

    Parameters
    ----------
    nodes : arr_like.
        Vertices of the netlist's graph.

    Returns
    -------
    list, list
        Nodes in partition 1 and 2.

    """
    return list(nodes[:len(nodes)//2]), list(nodes[len(nodes)//2:]) 

def kernighan_lin_bisection(g, max_iter=10):
    """

    Parameters
    ----------
    g : Networkx undirected graph
    max_iter : int, optional
        Maximum iterations the algorithm has to search for
        optimal partitions before giving up. The default is 10.

    Returns
    -------
    av : list
        Nodes in partition 1.
    bv : list
        Nodes in partition 2.

    """
    nodes = list(g.nodes(data=False))
    a, b = get_init_partition(nodes)
    for epoch in range(max_iter):
        av, bv, gv = [], [], []
        g1 = g.copy()
        for i in range(len(nodes)//2):
            th = -np.inf
            for j in range(len(a)):
                t1 = a[j]
                for k in range(len(b)):
                    t2 = b[k]
                    t3 = compute_gain(g1, t1, t2, a, b)
                    if t3>th:
                        th = t3
                        rnode = []
                        rnode.extend((t1, t2))
            av.append(rnode[0])
            bv.append(rnode[1])
            gv.append(th)
            a.remove(rnode[0])
            b.remove(rnode[1])
            g1.remove_nodes_from(rnode)
        max_sum = np.argmax(np.array(gv))
        av, bv = swap_from_list(av, bv, max_sum)
        a, b = av, bv
    return av, bv
