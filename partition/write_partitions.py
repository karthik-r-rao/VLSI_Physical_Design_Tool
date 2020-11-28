"""
@author: karthikrao

"""

def write_partitions(a, b):
    """

    Parameters
    ----------
    a : list
        Nodes in partition 1.
    b : list
        Nodes in partition 2.

    Returns
    -------
    None.

    """
    
    f = open('partition1.txt', 'w')
    for node in a:
        f.write(f"{node}\n")
    f.close()
    
    f = open('partition2.txt', 'w')
    for node in b:
        f.write(f"{node}\n")
    f.close()