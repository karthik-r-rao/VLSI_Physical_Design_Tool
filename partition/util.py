"""
@author: karthikrao

Utilities for kernighan_lin_bisection.py.

"""

import numpy as np

def compute_cutsize(g, partition1, partition2):
    count=0
    edges = list(g.edges())
    for i in edges:
        u,v = i
        if (u in partition1 and v in partition2) or (u in partition2 and v in partition1):
            count+=1
    return count

def computeD(g, a, partition1, partition2):
    count = 0
    adj = list(g.edges(a))
    for _ in adj:
        u,v = _
        if (u in partition1 and v in partition2) or (u in partition2 and v in partition1):
            count+=1
        else:
            count-=1
    return count

def compute_gain(g, a, b, partition1, partition2):
    edges = list(g.edges())
    count = computeD(g, a, partition1, partition2) + computeD(g, b, partition1, partition2)
    if (a, b) in edges:
        count-=2 
    return count

def swap_from_list(a, b, index):
    x = a[:index+1]
    y = b[:index+1]
    a+=y
    b+=x
    del a[:index+1]
    del b[:index+1]
    return a, b