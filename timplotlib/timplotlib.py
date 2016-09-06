import matplotlib.pyplot as plt

def lighter_frame(ax, color='#D3D3D3'):
    plt.setp(ax.spines.values(), color=color)

def lighter_ticks(ax, color='#D3D3D3'):
    plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='#D3D3D3')

def fancy_legend(ax, loc=0, fancybox=True, ec='#D3D3D3', lw=0.1):
    try:
        legend = ax.legend(loc=loc, fancybox=fancybox)
    except AttributeError:
        return 
    legend.legendPatch.set_edgecolor(ec)
    legend.legendPatch.set_lw(lw)

def timize(ax, framecolor='#D3D3D3', tickcolor='#D3D3D3', legend=True, legend_loc=0,
        fancybox=True, legend_ec='#D3D3D3', legend_lw=0.1, grid=True):
    lighter_frame(ax, color=framecolor)
    lighter_ticks(ax, color=tickcolor)
    if legend == True:
        fancy_legend(ax, loc=legend_loc, fancybox=fancybox, ec=legend_ec, lw=legend_lw)
    ax.grid(grid)
