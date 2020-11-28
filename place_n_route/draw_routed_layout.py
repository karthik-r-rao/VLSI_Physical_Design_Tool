"""
@author: karthikrao

Draw routed layout.

"""

import matplotlib.pyplot as plt
import matplotlib.patches as pt
import matplotlib
import numpy as np
from matplotlib.colors import from_levels_and_colors
from matplotlib.collections import LineCollection


def draw_routed_layout(layout, paths, w, h):
    """

    Parameters
    ----------
    layout : dict
    paths : list
        Routed wires in the circuit.
    w : dict
        Approx. widths of the blocks (gates) in the circuit.
    h : dict
        Approx. heights of the blocks (gates) in the circuit.

    Returns
    -------
    None.

    """
    
    patches = []
    for key in layout.keys():
        patch = pt.Rectangle(layout[key], w[key], h[key], color='yellow', alpha=0.6, ec='black')
        patches.append((patch, key))
    
    fig = plt.figure(figsize=(12,12)) 
    ax = fig.add_subplot(111)
    for patch in patches:
        ax.add_patch(patch[0])
        rx, ry = patch[0].get_xy()
        cx = rx + patch[0].get_width() + 6
        cy = ry + patch[0].get_height()/2.0
        ax.annotate(patch[1], (cx, cy), color='black', ha='center', va='center', fontweight='semibold', size='large')
    
    new_paths = []    
    for path in paths:
        if len(path):
            new_path = []
            for i in range(1, len(path)): 
                z, x, y = path[i-1]
                z1, x1, y1 = path[i]
                if y==y1:
                    new_path.append([2*z1, x, y])
                if x==x1:
                    new_path.append([2*z1+1, x, y])
            end = len(path)-1
            z, x, y = path[end-1]
            z1, x1, y1 = path[end]
            if y==y1:
                new_path.append([2*z1, x1, y1])
            if x==x1:
                new_path.append([2*z1+1, x1, y1])
            new_paths.append(new_path)
        
    for path in new_paths:
        x = [10*i+1 for k, i, j in path]
        y = [10*j+5 for k, i, j in path]
        z = [k for k, i, j in path]
        z = np.array(z)
        
        cmap, norm = from_levels_and_colors([0, 1, 2, 3, 4, 5, 6], ['blue', 'green', 'black', 'red', 'grey', 'violet'])
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        lines = LineCollection(segments, cmap=cmap, norm=norm)
        lines.set_array(z.astype(int))
        ax.add_collection(lines)
        
    plt.xlim([0, 800])
    plt.ylim([0, 800])       
    plt.show()