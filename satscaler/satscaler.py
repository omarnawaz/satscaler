"""
satscaler.py
==============

A Python module for rescaling the adjoint coefficients used in FATE by calculating scaling factors between the old and new satellite-derived datasets.

Functions:
---------

- read_nc(filename, variable, outvariable): Read the netcdf data and returns a dataframe
- calculate_scale_factor(old_pm25,new_pm25,pop,mask,out_dir): Calculate the scale factor 
                                                              based on the two products
"""

# %%
# Imports
import numpy as np

from data_reader import read_nc
from scaler import calculate_scale_factor

# %%
# Constants
base_dir = "./"
fate_dir = f"{base_dir}../../data/fate_inputs/"
sat_dir = f"{base_dir}../../data/new_satellite_data/"
out_dir = f"{base_dir}../../data/scaling_factor/"

# %%
# Main
if __name__ == "__main__":
    # Read in old pm2.5 data
    pm25_data = read_nc(f"{fate_dir}pm25_satellite_grid.nc", "sat_pm25_grid", "pm25")
    pm25_data.loc[pm25_data.pm25 < 0, :] = np.nan  # remove negative pm2.5 values
    # Read in new pm2.5 data
    new_pm25_data = read_nc(
        f"{sat_dir}V5GL03.HybridPM25c_0p10.Global.202101-202112.nc", "GWRPM25", "pm25"
    )
    new_pm25_data = new_pm25_data.rename(columns={"lat": "lat_f", "lon": "lon_f"})
    # Read in population data
    population_data = read_nc(f"{fate_dir}population_fine.nc", "fine_pop", "population")
    # Read in country mask data
    mask_data = read_nc(f"{fate_dir}country_mask.nc", ["mask", "frac"])

    # Calculate scale factor
    sf = calculate_scale_factor(
        old_pm25=pm25_data,
        new_pm25=new_pm25_data,
        pop=population_data,
        mask=mask_data,
        out_dir=out_dir,
    )
