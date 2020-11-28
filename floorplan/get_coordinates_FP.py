"""
@author: karthikrao

Get coordinates of various blocks (gates) given a Polish Expression.
"""

from get_cost_FP import *
import copy

def get_coordinates_FP(exp, w, h, pnumber):
    """
    
    Parameters
    ----------
    exp : list
        Input Polish Expression.
    w : dict
        Contains approx. width of each gate in the netlist.
    h : dict
        Contains approx. height of each gate in the netlist.
    pnumber : int
        Indicates the partition number. 
        Purely used for visual purposes when the final floorplan is plotted.

    Returns
    -------
    xy : dict
        Contains the Cartesian coordinates of all the blocks present in the Polish Expression.

    """
    
    i=-1
    c=0
    exp1 = exp.copy()
    info = []
    while len(exp1)>1:
        i+=1
        if exp1[i] == 'H' or exp1[i] == 'V':
            new = 'tempnode'+str(c)
            info.append((new, exp1[i-2], exp1[i-1], exp1[i]))
            exp1 = exp1[:i-2] + [new] + exp1[i+1:]
            i=-1
        c+=1
    xy = {}
    _, w1, h1 = get_cost_FP(exp, w, h)
    xy[info[len(info)-1][0]] = [0, 0]
    for i in range(len(info)-1, -1, -1):
        if info[i][3] == 'H':
            xy[info[i][2]] = copy.deepcopy(xy[info[i][0]])
            xy[info[i][1]] = [copy.deepcopy(xy[info[i][0]][0]), copy.deepcopy(xy[info[i][0]][1]) + h1[info[i][2]]]
        if info[i][3] == 'V':
            xy[info[i][1]] = copy.deepcopy(xy[info[i][0]])
            xy[info[i][2]] = [copy.deepcopy(xy[info[i][0]][0]) + w1[info[i][1]], copy.deepcopy(xy[info[i][0]][1])]
    for key in list(xy.keys()):
        xy[key][0] += 60*pnumber
    return xy