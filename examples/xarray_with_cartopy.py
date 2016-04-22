"""
Xarray with cartopy
===================
_thumb: 1.0, 1.0
"""

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import seaborn as sns

ds = xr.tutorial.load_dataset('air_temperature')

# Use Seaborn to set some default styles
sns.set_context("notebook")

# Setup the cartopy plot axes
ax = plt.axes([0, 0, 1, 1], projection=ccrs.Orthographic(-95, 35))
ax.set_global()
ax.coastlines(color='black', lw=1)

# Plot using the xarray.DataArray pcolormesh method
ds['air'].isel(time=0).plot.pcolormesh('lon', 'lat', levels=12, extend='both',
                                       ax=ax, transform=ccrs.PlateCarree())
