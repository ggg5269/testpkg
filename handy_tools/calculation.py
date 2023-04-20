import pandera
def sum_lists(*args):
    """對 list 做元素間加總

    Returns:
        list
    """
    return list(map(sum, zip(*args)))

def mul_lists(lis):
    """list 元素作連乘
    >>> lis = [[1,2,3],[2,3,4],[3,4,5]]
    >>> mul_lists(lis)
    >>> [6, 24, 60]

    Args:
        lis (list)
    Returns:
        list
    """
    from operator import mul
    from functools import reduce
    return [reduce(mul, x) for x in lis]

def add_num_to_list(ls, num):
    """將 list 當中各元素加上給定數值

    Args:
        ls (list)
        num (float)

    Returns:
        list
    """
    return [num+i for i in ls]

def zscore(arr, window):
    """calculate the rolling z-scaore of pandas series

    Args:
        arr (pd.Series): pandas series
        window (int): rolling window

    Returns:
        pd.Series
    """
    import pandas as pd
    
    x = arr.rolling(window = 1).mean()
    u = arr.rolling(window = window).mean()
    o = arr.rolling(window = window).std()

    return (x-u)/o

def sign(x):
    return x and (1, -1)[x<0]
