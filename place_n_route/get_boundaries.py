"""
@author: karthikrao

Get boundaries of the current layout. (Cartesian coordinates)

"""

def get_boundaries(layout):
    """

    Parameters
    ----------
    layout : dict

    Returns
    -------
    (max_x + 10, max_y + 10) : Boundaries of the layout.
    The other boundary would be (0, 0).

    """
    max_x=max_y=0
    for key in list(layout.keys()):
        x1, y1 = layout[key]
        if x1>max_x:
            max_x = x1
        if y1>max_y:
            max_y = y1
    return max_x + 10, max_y + 10