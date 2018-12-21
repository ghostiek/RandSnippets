"""
Returns a seaborn barplot of the top/bottom n elements

Parameters:
n        -- Number of elements to use.
top      -- True gets the top n elements, False will get the bottom n elements. Default: True.
**kwargs -- Dictionary of values that satisfy the parameters of the barplot. Minimum necessary is data, x, y, estimator.

Return:
seaborn.barplot object
"""
import seaborn as sns
import numpy as np
import pandas as pd

def top_n_barplot(n, top = True, **kwargs):
    if n < 1:
        raise ValueError("n cannot be smaller than 1.")
    
    #Get necessary data
    data = kwargs["data"]
    x = kwargs["x"]
    y = kwargs["y"]
    estimator = kwargs["estimator"]
    
    #Get all the results and sort
    result = data.groupby(x)[y].apply(estimator).sort_values()
    
    if top:
        result = result[-n:]
    else:
        result = result[:n]
    
    #Filter according to necessary data
    top_x = result.index    
    newdata = data.loc[data[x].isin(top_x.values)].copy()
    #Make values categorical and order them
    newdata[x] = pd.Categorical(newdata[x], categories=top_x, ordered=True)
    #Assign new data to use for plot
    kwargs["data"] = newdata
    
    return sns.barplot(**kwargs)
