import matplotlib.pyplot as plt

def lighter_frame(ax, color='#D3D3D3', zorder='top'):
    for spine in ('top', 'bottom', 'left', 'right'):
        ax.spines[spine].set_color(color)

def lighter_ticks(ax, color='#D3D3D3'):
    for t in ax.xaxis.get_ticklines():
        t.set_color(color)
    for t in ax.yaxis.get_ticklines():
        t.set_color(color)

def fancy_legend(ax, loc=0, fancybox=True, ec='#D3D3D3', lw=0.1, ncol=1,
        columnspacing=None):
    try:
        legend = ax.legend(loc=loc, fancybox=fancybox, ncol=ncol, 
                columnspacing=columnspacing)
        legend.legendPatch.set_edgecolor(ec)
        legend.legendPatch.set_lw(lw)
    except AttributeError:
        return 

def timize(ax, framecolor='#D3D3D3', tickcolor='#D3D3D3', legend=True, legend_loc=0,
        fancybox=True, legend_ec='#D3D3D3', legend_lw=0.1, grid=True, frame_z='top',
        grid_zorder=0, legend_ncol=1, grid_color='#D3D3D3', legend_cspacing=None):
    lighter_frame(ax, color=framecolor)
    lighter_ticks(ax, color=tickcolor)
    if legend == True:
        fancy_legend(ax, loc=legend_loc, fancybox=fancybox, ec=legend_ec, lw=legend_lw,
                ncol=legend_ncol, columnspacing=legend_cspacing)
    if grid == True:
        ax.grid(grid, zorder=grid_zorder, color=grid_color)
