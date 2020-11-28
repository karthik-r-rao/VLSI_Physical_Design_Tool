"""
@author: karthikrao

Get path.

"""

import numpy as np
from queue import Queue

def get_boundaries_routing(layout):
    """

    Parameters
    ----------
    layout : dict

    Returns
    -------
    x, y
        Extreme boundary of the layout.

    """
    
    max_x=max_y=0
    for key in list(layout.keys()):
        x1, y1 = layout[key]
        if x1>max_x:
            max_x = x1
        if y1>max_y:
            max_y = y1
    return max_x + 1, max_y + 1



def check_cell(cell, vacant):
    """

    Parameters
    ----------
    cell : list
        Point on the 3D grid.
    vacant : list
        Contains empty spaces on the grid.

    Returns
    -------
    bool
        True if the cell is not occupied by a block (gate).

    """
    
    for v in vacant:
        if v==cell:
            return True
    return False



def find_path(start, end, layout, vacant):
    """
    

    Parameters
    ----------
    start : list
        Start point for routing.
    end : list
        End point for routing.
    layout : dict
    vacant : list
        Contains empty spaces on the grid.

    Returns
    -------
    path : list
        List of points in the path between <start> and <end>.

    """
    x, y = get_boundaries_routing(layout)
    costs = np.zeros((6, x, y))-1 # max layers 6
    visited = np.zeros((6, x, y))
    q = Queue()
    u, v = start
    alpha, beta = end
    costs[0][u][v] = 0
    visited[0][u][v] = True
    start = [0] + start
    end = [0] + end
    q.put(start)
    
    ##########
    # Wave expansion
    ##########
    
    while not q.empty() and not visited[0][alpha][beta]:
        z, x, y = q.get()
        l = [z, x-1, y]
        r = [z, x+1, y]
        u = [z, x, y+1]
        d = [z, x, y-1]
        t = [z+1, x, y]
        b = [z-1, x, y]
        
        z1, x1, y1 = l
        if (check_cell(l, vacant) and not visited[z1][x1][y1]) or l==end:
            costs[z1][x1][y1]=costs[z][x][y]+1
            visited[z1][x1][y1] = True
            q.put(l)

        z1, x1, y1 = r
        if (check_cell(r, vacant) and not visited[z1][x1][y1]) or r==end:
            costs[z1][x1][y1]=costs[z][x][y]+1
            visited[z1][x1][y1] = True
            q.put(r)
            
        z1, x1, y1 = u
        if (check_cell(u, vacant) and not visited[z1][x1][y1]) or u==end:
            costs[z1][x1][y1]=costs[z][x][y]+1
            visited[z1][x1][y1] = True
            q.put(u)
            
        z1, x1, y1 = d
        if (check_cell(d, vacant) and not visited[z1][x1][y1]) or d==end:
            costs[z1][x1][y1]=costs[z][x][y]+1
            visited[z1][x1][y1] = True
            q.put(d)
            
        z1, x1, y1 = t
        if (check_cell(t, vacant) and not visited[z1][x1][y1]) or t==end:
            costs[z1][x1][y1]=costs[z][x][y]+1
            visited[z1][x1][y1] = True
            q.put(t)
            
        z1, x1, y1 = b
        if (check_cell(b, vacant) and not visited[z1][x1][y1]) or b==end:
            costs[z1][x1][y1]=costs[z][x][y]+1
            visited[z1][x1][y1] = True
            q.put(b)
    
    ##########
    # Backtrace
    ##########
    
    path = []
    cell = end
    if costs[0][alpha][beta]>0:
        path.append(cell)
        while cell!=start:
            l = [cell[0], cell[1]-1, cell[2]]
            z1, x1, y1 = l
            if (check_cell(l, vacant) and costs[z1][x1][y1]==costs[cell[0]][cell[1]][cell[2]]-1) or l==start:
                path.append(l)
                cell = l
                continue
            
            r = [cell[0], cell[1]+1, cell[2]]
            z1, x1, y1 = r
            if (check_cell(r, vacant) and costs[z1][x1][y1]==costs[cell[0]][cell[1]][cell[2]]-1) or r==start:
                path.append(r)
                cell = r
                continue
            
            u = [cell[0], cell[1], cell[2]+1]
            z1, x1, y1 = u
            if (check_cell(u, vacant) and costs[z1][x1][y1]==costs[cell[0]][cell[1]][cell[2]]-1) or u==start:
                path.append(u)
                cell = u
                continue
            
            d = [cell[0], cell[1], cell[2]-1]
            z1, x1, y1 = d
            if (check_cell(d, vacant) and costs[z1][x1][y1]==costs[cell[0]][cell[1]][cell[2]]-1) or d==start:
                path.append(d)
                cell = d
                continue
            
            t = [cell[0]+1, cell[1], cell[2]]
            z1, x1, y1 = t
            if (check_cell(t, vacant) and costs[z1][x1][y1]==costs[cell[0]][cell[1]][cell[2]]-1) or t==start:
                path.append(t)
                cell = t
                continue
            
            b = [cell[0]-1, cell[1], cell[2]]
            z1, x1, y1 = b
            if (check_cell(b, vacant) and costs[z1][x1][y1]==costs[cell[0]][cell[1]][cell[2]]-1) or b==start:
                path.append(b)
                cell = b
                continue
         
    ##########
    # Clearance
    ##########
            
    for i in range(1, len(path)-1):
        vacant.remove(path[i])
    return path