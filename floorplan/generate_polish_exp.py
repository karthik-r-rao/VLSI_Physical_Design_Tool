"""
@author: karthikrao

Function to generate an initial Polish Expression.
"""

def generate_polish_exp(nodes):
    """

    Parameters
    ----------
    nodes : list/ arr_like
        Nodes of the netlist.

    Returns
    -------
    exp : list
        A Polish Expression.

    """
    
    exp = []
    for i in range(len(nodes)):
        exp.append(nodes[i])
        if i!=0:
            if i<(len(nodes)//2):
                exp.append('V')
            else:
                exp.append('H')
    return exp