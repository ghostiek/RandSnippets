def ranged_barplot(start, end, labels, data, hue=None, order=None, hue_order=None,
            estimator=np.mean, ci=95, n_boot=1000, units=None,
            orient=None, color=None, palette=None, saturation=.75,
            errcolor=".26", errwidth=None, capsize=None, dodge=True,
            ax=None, **kwargs):
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
