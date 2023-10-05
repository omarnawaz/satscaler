import xarray as xr
import pandas as pd


def read_nc(filename, variables, out_variables=None):
    """
    Read the original netcdf data from FATE files located at the given filename.

    Parameters:
    filename        (str): The path to the netCDF file.
    variables       (str): The name of the variables(s) to extract from the neCDF file.
    out_variables   (str): The desired name of the variable. Set to None as default to retain the
                           original variable.

    Returns:
    nc_data (pandas.DataFrame): The netcdf file as a dataframe
    """
    df = xr.open_dataset(filename).to_dataframe()
    nc_data = df[variables].reset_index()
    if out_variables:
        nc_data = nc_data.rename(columns={variables: out_variables})
    return nc_data
