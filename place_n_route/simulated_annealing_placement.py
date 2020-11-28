"""
@author: karthikrao

Simulated Annealing for placement.

"""

import numpy as np
import random
import math
import copy
from get_cost_placement import *
from moves_placement import *

def sim_annealing_placement(layout, vacant, occupied, edges):
    """

    Parameters
    ----------
    layout : dict
    vacant : list
        Vacant 10x10 blocks in the chip.
    occupied : list
        Occupied 10x10 blocks in the chip.
    edges : TYPE
        DESCRIPTION.

    Returns
    -------
    finalsol : dict
    finalvac : list
        Vacant 10x10 blocks in the chip.
    finalocc : list
        Occupied 10x10 blocks in the chip.

    """
    
    init_temp = 20000
    final_temp = 0.01
    alpha = 0.95
    min_cost = np.inf
    costs = []

    curr_temp = init_temp
    sol = layout.copy()
    while curr_temp>final_temp:
        for loops in range(100):
            x = random.randint(0, 1)
            if x:
                neighbor = move2(layout)
            else:
                neighbor, vacant, occupied = move1(layout, vacant, occupied)
            new_cost = get_cost_placement(neighbor, edges)
            old_cost = get_cost_placement(sol, edges)
            cost_diff = new_cost - old_cost
            if cost_diff < 0:
                sol = copy.deepcopy(neighbor)
                costs.append(new_cost)
            else:
                if random.uniform(0, 1) < math.exp(-cost_diff / curr_temp):
                    sol = copy.deepcopy(neighbor)
                    costs.append(new_cost)
            if new_cost<min_cost:
                finalsol = copy.deepcopy(sol)
                finalvac = copy.deepcopy(vacant)
                finalocc = copy.deepcopy(occupied)
                min_cost = new_cost
        curr_temp*=alpha
    #plt.plot(costs)
    #plt.show()
    return finalsol, finalvac, finalocc