"""
@author: karthikrao

Program to get graph from netlist.
Written specifically for adder.isc. 
Might not work for other netlists.
"""

import networkx as nx
import matplotlib.pyplot as plt
from get_graph_info import *

INFILE = "adder.isc" # specify path to .isc file 

get_graph_info(INFILE)
