"""
@author: karthikrao

Program to calculate cost of a floorplan given its Polish Expression.
"""

def get_cost_FP(exp, w, h):
    """

    Parameters
    ----------
    Parameters
    ----------
    exp : list
        Initial Polish Expression.
    w : dict
        Contains approx. width of each gate in the netlist.
    h : dict
        Contains approx. height of each gate in the netlist.

    Returns
    -------
    cost : int
        Gives an estimate of the cost (area) of the floorplan.
    w1 : dict
        Contains approx. width of each gate in the netlist.
    h1 : dict
        Contains approx. height of each gate in the netlist.

    """
    
    i=-1
    c=0
    exp1 = exp.copy()
    w1=w.copy()
    h1=h.copy()
    while len(exp1)>1:
        i+=1
        if exp1[i] == 'H' or exp1[i] == 'V':
            new = 'tempnode'+str(c)
            if exp1[i] == 'H':
                h1[new] = h1[exp1[i-1]] + h1[exp1[i-2]]
                w1[new] = max(w1[exp1[i-1]], w1[exp1[i-2]])
            if exp1[i] == 'V':
                h1[new] = max(h1[exp1[i-1]], h1[exp1[i-2]])
                w1[new] = w1[exp1[i-1]] + w1[exp1[i-2]]
            exp1 = exp1[:i-2] + [new] + exp1[i+1:]
            i=-1
        c+=1
    cost = h1[exp1[0]]*w1[exp1[0]]
    return cost, w1, h1