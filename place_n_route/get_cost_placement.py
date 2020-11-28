"""
@author: karthikrao

Cost function for placement.

"""

from get_boundaries import *

def getHPWL(layout, node1, node2):
    """
    
    Parameters
    ----------
    layout : dict
    node1 : str 
        Block in layout/ gate in the netlist.
    node2 : str
        Block in layout/ gate in the netlist.

    Returns
    -------
    int
        The Half-Perimeter Wirelength (HPWL) between the two points. 
        Equal to the half the perimeter of the smallest bounding rectangle.

    """
    x1, y1 = layout[node1]
    x2, y2 = layout[node2]
    return abs(x1-x2) + abs(y1-y2)

def getWirelength(layout, edges):
    """

    Parameters
    ----------
    layout : dict
    edges : list
        Edges in the graph/ connections in the netlist.

    Returns
    -------
    l : int
        The sum of HPWL of all edges in the graph..

    """
    
    l = 0
    for edge in edges:
        u, v = edge
        l+=getHPWL(layout, u, v)
    return l

def get_cost_placement(layout, edges):
    """
    Cost function = a1*Area + b1*Wirelength.
    
    Parameters
    ----------
    layout : dict
    edges : list
        Edges in the graph/ connections in the netlist.

    Returns
    -------
    int
        Cost of the placement process that is done on the chip.

    """
    
    a1 = 0.2
    b1 = 2
    x, y = get_boundaries(layout)
    area = x*y
    l = getWirelength(layout, edges)
    return a1*area + b1*l