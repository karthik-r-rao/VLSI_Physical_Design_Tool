"""
@author: karthikrao

Get initial placement. The input layout contains only relative locations
between the various blocks (gates). This function spreads the blocks outwards
and introduces space in the middle so that routing can be done afterwards.

"""

def get_initial_placement(layout):
    """

    Parameters
    ----------
    layout : dict
        The layout obtained at the end of the floorplanning step.

    Returns
    -------
    l : dict
        Final layout with some space in between.
        Each block (gate) will be in a grid of 10x10.

    """
    
    l1 = {}
    a=0
    x=0
    sort_x = sorted(layout.items(), key = lambda item:item[1][0])
    for i in range(len(sort_x)-1):
        l1[sort_x[i][0]] = a
        if x==sort_x[i+1][1][0]:
            continue
        else:
            a+=60
            x=sort_x[i+1][1][0]
    l1[sort_x[len(sort_x)-1][0]] = a  
    
    l2 = {}
    a=0
    y=0
    sort_y = sorted(layout.items(), key = lambda item:item[1][1])
    for i in range(len(sort_y)-1):
        l2[sort_y[i][0]] = a
        if y==sort_y[i+1][1][1]:
            continue
        else:
            a+=60
            y=sort_y[i+1][1][1]
    l2[sort_y[len(sort_y)-1][0]] = a  
    
    l = {}
    for key in list(l1.keys()):
        l[key] = [l1[key], l2[key]]
    return l