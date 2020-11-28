"""
@author: karthikrao

Moves to be tried during the placement step.

"""

import random
import copy

def move1(layout, vacant, occupied):
    """
    Moves a random block to a vacant location.

    Parameters
    ----------
    layout : dict
    vacant : list
        Vacant 10x10 blocks in the chip.
    occupied : list
        Occupied 10x10 blocks in the chip.

    Returns
    -------
    layout : dict
    vacant : list
        Vacant 10x10 blocks in the chip.
    occupied : TYPE
        Occupied 10x10 blocks in the chip.

    """
    
    l = random.choice(list(layout.keys())) 
    [v] = random.sample(vacant, 1)
    vacant.remove(v)
    vacant.append(layout[l])
    occupied.remove(layout[l])
    occupied.append(v)
    layout[l] = v
    return layout, vacant, occupied

def move2(layout):
    """
    Swaps locations of two random blocks.

    Parameters
    ----------
    layout : dict

    Returns
    -------
    layout : dict

    """
    l1 = random.choice(list(layout.keys()))
    l2 = random.choice(list(layout.keys()))
    layout[l1], layout[l2] = copy.deepcopy(layout[l2]), copy.deepcopy(layout[l1])
    return layout