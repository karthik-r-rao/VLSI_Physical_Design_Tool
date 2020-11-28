"""
@author: karthikrao

Draw layout.
"""

import random
import matplotlib.patches as pt
import matplotlib.pyplot as plt

def draw_layout(layout, w, h):
    patches = []
    colors = ['red', 'blue', 'green', 'brown', 'yellow', 'pink'] 
    for key in layout.keys():
        j = random.randint(0, 5)
        patch = pt.Rectangle(layout[key], w[key], h[key], color=colors[j], alpha=0.6, ec='black')
        patches.append((patch, key))
    
    fig = plt.figure(figsize=(10,10)) 
    ax = fig.add_subplot(111)
    for patch in patches:
        ax.add_patch(patch[0])
        rx, ry = patch[0].get_xy()
        cx = rx + patch[0].get_width()/2.0
        cy = ry + patch[0].get_height()/2.0
        ax.annotate(patch[1], (cx, cy), color='black', ha='center', va='center')
    plt.xlim([0, 700])
    plt.ylim([0, 700])
    plt.show()