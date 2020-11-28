"""
@author: karthikrao

Moves defined for Simulated Annealing.
"""

import random
from tests import *

"""
Swap two adjacent operands.
"""

def move1(exp):
    """

    Parameters
    ----------
    exp : list
        Input Polish Expression.

    Returns
    -------
    exp : list
        Output Polish Expression.

    """
    
    while True:
        i = random.randint(0, len(exp)//2)
        if exp[i]!='H' and exp[i]!='V':
            break
    ele1=i
    while True:
        i+=1
        if exp[i]!='H' and exp[i]!='V':
            break
    ele2=i
    exp[ele1], exp[ele2] = exp[ele2], exp[ele1]
    return exp
  
    
"""
Complement a series of operators in a sublist.
"""

def move2(exp):
    """

    Parameters
    ----------
    exp : list
        Input Polish Expression.

    Returns
    -------
    exp : list
        Output Polish Expression.

    """
    
    start = random.randint(0, len(exp)-1)
    end = random.randint(start, len(exp)-1)
    for i in range(start, end):
        if exp[i] == 'H':
            exp[i] = 'V'
        elif exp[i] == 'V':
            exp[i] = 'H'
    return exp


"""
Swap an adjacent operand-operator pair.
"""

def move3(exp):
    """

    Parameters
    ----------
    exp : list
        Input Polish Expression.

    Returns
    -------
    exp : list
        Output Polish Expression.

    """
    
    exp1 = exp.copy()
    while True:
        i = random.randint(0, len(exp)-2)
        if (exp[i]=='H' or exp[i]=='V') and (exp[i+1]!='H' and exp[i+1]!='V'):
            break
    exp1[i], exp1[i+1] = exp1[i+1], exp1[i]
    if test_ballot(exp1, i+1) and test_normalized(exp1):
        return exp1
    return exp