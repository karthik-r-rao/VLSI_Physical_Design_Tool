"""
@author: karthikrao

Program to get graph from netlist.

"""

import networkx as nx
import matplotlib.pyplot as plt
from get_graph_info import *

INFILE = PATH # specify path to .isc file 
OUTDIR = PATH # specify output directory

get_graph_info(INFILE, OUTDIR)
