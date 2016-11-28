import matplotlib.pyplot as plt

def lighter_frame(ax, color='#D3D3D3', zorder='top'):
    plt.setp(ax.spines.values(), color=color, zorder=zorder)

def lighter_ticks(ax, color='#D3D3D3'):
    plt.setp([ax.get_xticklines(), ax.get_yticklines()], color=color)

def fancy_legend(ax, loc=0, fancybox=True, ec='#D3D3D3', lw=0.1, ncol=1):
    try:
        legend = ax.legend(loc=loc, fancybox=fancybox, ncol=ncol)
        legend.legendPatch.set_edgecolor(ec)
        legend.legendPatch.set_lw(lw)
    except AttributeError:
        return 

def timize(ax, framecolor='#D3D3D3', tickcolor='#D3D3D3', legend=True, legend_loc=0,
        fancybox=True, legend_ec='#D3D3D3', legend_lw=0.1, grid=True, frame_z='top',
        grid_zorder=0, legend_ncol=1, grid_color='#D3D3D3'):
    lighter_frame(ax, color=framecolor, zorder=frame_z)
    lighter_ticks(ax, color=tickcolor)
    if legend == True:
        fancy_legend(ax, loc=legend_loc, fancybox=fancybox, ec=legend_ec, lw=legend_lw,
                ncol=legend_ncol, columnspacing=legend_cspacing)
    if grid == True:
        ax.grid(grid, zorder=grid_zorder, color=grid_color)
