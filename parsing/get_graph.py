"""
@author: karthikrao

Create a graph from a netlist in ISCAS-85 format.

"""

import networkx as nx

def get_graph(filepath):
    """
        getGraph(filename)
        
        Parameters
        ----------
        filepath : PATH to netlist file in .isc format.
        
        Returns
        ----------
        g : graph corresponding to the input netlist.
    """
    
    f = open(filepath, 'r')
    fdata = f.readlines()
    
    data = []
    
    for i in fdata:
        temp = i.split()
        if i[0] == '\t':
            continue
        else:
            data.append(i)
    
    # data --> file data without the fanin nodes' info.
            
    g = nx.Graph()
    
    i=0
    while i<(len(fdata)):
        temp = fdata[i].split()
        g.add_node(temp[0], nodetype=temp[2])
        fanin = int(temp[4])
        if fanin:
            x = fdata[i+1].split('\t')
            for j in range(1, len(x)):
                if j==len(x):
                    x[j] = x[j][:len(x[j])]
                y = data[int(x[j])-1].split()
                g.add_node(y[0], nodetype=y[2])
                g.add_edge(temp[0],y[0])
            i+=1
        fanout = int(temp[3])
        if fanout>1:
            for j in range(fanout):
                x = fdata[i+j+1].split()
                g.add_node(x[0], nodetype=x[2])
                g.add_edge(temp[0],x[0])
            i+=fanout
        i+=1
    
    # Intermediate graph. Contract this graph to get actual graph
    # corresponding to the input netlist.
    
    
    nodes = list(g.nodes(data=True))
    gates = ['nand', 'nor', 'not', 'or', 'and', 'xor', 'xnor', 'buff']
    
    # contraction
    for node in nodes:
        if node[1]['nodetype'] not in gates:
            neighbors = [n for n in g[node[0]]]
            for neighbor in neighbors:
                g = nx.contracted_nodes(g, neighbor, node[0], self_loops=False)
                break
                
    f.close()
    return g