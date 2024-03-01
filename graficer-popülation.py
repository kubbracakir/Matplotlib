import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import numpy as np
import geopandas as gpd
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Create a sample dataset with population data for different regions
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world['population'] = np.random.randint(0, 1000000, len(world))

# Create a figure with two subplots: one for the map and one for the colorbar
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Create a choropleth map on the first subplot
ax1 = world.plot(column='population', cmap='YlGnBu', linewidth=0.8, ax=ax1, edgecolor='white')

# Create a colorbar on the second subplot using the make_axes_locatable function
divider = make_axes_locatable(ax1)
cax = divider.append_axes("right", size="5%", pad=0.05)
cb = plt.colorbar(ax1.get_children()[0], cax=cax)

# Set the colorbar label and tick labels
cb.set_label('Population')
cbar_ticks = np.linspace(0, 1000000, 6)
cbar_tick_labels = ['{:,.0f}'.format(x) for x in cbar_ticks]
cb.set_ticks(cbar_ticks)
cb.set_ticklabels(cbar_tick_labels)

# Set the title of the plot
plt.suptitle('Population Distribution by Region', fontsize=16, y=0.92)

# Adjust the spacing between the subplots
plt.tight_layout(h_pad=2.0)

# Show the plot
plt.show()