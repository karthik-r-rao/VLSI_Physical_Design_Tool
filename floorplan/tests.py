"""
@author: karthikrao

Test the Polish Expression for its Balloting and Normalized properties.
 
"""

def test_ballot(exp, index):
    """

    Parameters
    ----------
    exp : list
        Polish Expression to be tested for its balloting property.
    index : int
        End point of the Polish Expression to be tested for its balloting property.

    Returns
    -------
    bool
        True indicates the Polish Expression satisfies the balloting property.

    """
    
    temp = exp[:index+1]
    operators=0
    for i in temp:
        if i=='V' or i=='H':
            operators+=1
    if 2*operators<(index):
        return True
    return False



def test_normalized(exp):
    """

    Parameters
    ----------
    exp : list
        Polish Expression to be tested for its normalized property.

    Returns
    -------
    bool
        True if the given Polish Expression is normalized.

    """
    
    for i in range(len(exp)-1):
        if exp[i]==exp[i+1]:
            return False
    return True