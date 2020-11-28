"""
@author: karthikrao

Perform Simulated Annealing to get an optimal floorplan.
"""

import numpy as np
import random
from moves import *
from get_cost_FP import *
import math

def simulated_annealing_FP(init, w, h):
    """

    Parameters
    ----------
    init : list
        Initial Polish Expression.
    w : dict
        Contains approx. width of each gate in the netlist.
    h : dict
        Contains approx. height of each gate in the netlist.

    Returns
    -------
    finalsol : list
        Final, optimal Polish Expression.
    costs : list
        Contains history of costs over the Simulated Annealing process.

    """
    
    init_temp = 1000
    final_temp = 0.01
    alpha = 0.95
    costs = []
    min_cost = np.inf
    
    curr_temp = init_temp
    sol = init.copy()
    while curr_temp>final_temp:
        for loops in range(500):
            x = random.randint(0, 2)
            if x==0:
                neighbor = move1(sol)
            elif x==1:
                neighbor = move2(sol)
            elif x==2:
                neighbor = move3(sol)
    
            new_cost, _, _ = get_cost_FP(neighbor, w, h)
            old_cost, _, _ = get_cost_FP(sol, w, h)
            costs.append(new_cost)
            cost_diff = new_cost - old_cost
            if cost_diff<0:
                sol = neighbor
            else:
                 if random.uniform(0, 1) < math.exp(-cost_diff / curr_temp):
                     sol = neighbor
            if new_cost<min_cost:
                finalsol = sol
                min_cost = new_cost
        curr_temp*=alpha
    return finalsol, costs