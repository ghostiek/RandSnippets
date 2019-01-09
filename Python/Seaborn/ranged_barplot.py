"""
Plots observations based on the range given

Parameters:
start    -- string of column name of the dataframe to determine the start range
end      -- string of the column name of the dataframe to determine the end range
data     -- pd.DataFrame object
hue      -- string of the column name of the dataframe to define subsets of the data
ax       -- matplotlib.pyplot.Axes object. Will use current axes if left as None
**kwargs -- Dictionary of values that satisfy the parameters of the plot.
"""

def ranged_barplot(start, end, labels, data, hue=None, order=None, ax=None, **kwargs):
    #Get Axis
    if ax is None:
        ax = plt.gca()
    
    #Setup category to color
    if hue is not None:
        color_labels = data[hue].unique()
        rgb_values = sns.color_palette("Set1", len(color_labels))
        color_map = dict(zip(color_labels, rgb_values))

    #Plot each ranged bar and give it a label/color if hue is defined
    for i in range(len(data)):
        col = None if hue is None else color_map[data.loc[i, hue]]
        lab = None if hue is None else data.loc[i,hue]
        plt.plot([data.loc[i, start], data.loc[i, end]], [i,i], c = col, label = lab, solid_capstyle="butt",
                 **kwargs)
    
    #Add a legend to the plot if necessary
    if hue is not None:
        legend_handles, legend_labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(legend_labels, legend_handles))
        plt.legend(by_label.values(), by_label.keys())   
    
    #Rename y-axis to have the labels there
    ax.set_yticks(range(len(data[labels])))
    ax.set_yticklabels(data[labels])
    #plt.tight_layout()
    #plt.savefig("RangedBarplot.jpg")
    plt.show()
