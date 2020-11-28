"""
@author: karthikrao

Get rectangular patches for plotting.
"""

from get_coordinates_FP import *
import random
import matplotlib.patches as pt

def get_patches_FP(exp, w, h, pnumber):
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
    patches : list of Matplotlib Patches
        These patches will be used for visualizing the floorplan.

    """
    
    xy = get_coordinates_FP(exp, w, h, pnumber)
    patches = []
    colors = ['red', 'blue', 'green', 'brown', 'yellow', 'pink'] 
    for key in xy.keys():
        if key[0]=='t':
            continue
        j = random.randint(0, 5)
        patch = pt.Rectangle(xy[key], w[key], h[key], color=colors[j], alpha=0.6, ec='black')
        patches.append((patch, key))
    return patches