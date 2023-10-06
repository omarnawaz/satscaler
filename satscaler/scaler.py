import numpy as np
import pandas as pd


def calculate_country_pm25(df, pop, mask):
    """
    Calculate population weighted PM2.5 values for each county based on dataframes df, pop, and mask.

    Args:
        df (pandas.DataFrame): DataFrame containing latitude, longitude, and PM2.5 values.
        pop (pandas.DataFrame): DataFrame containing latitude, longitude, and population values.
        mask (pandas.DataFrame): DataFrame containing latitude, longitude, and mask values.

    Returns:
        pandas.DataFrame: DataFrame containing population weighted PM2.5 values for each country.
    """
    dflat, dflon = np.round(df.lat_f, 2), np.round(df.lon_f, 2)
    mapped_df = dict(zip(list(zip(dflat, dflon)), list(df.pm25)))
    mapped_pop = dict(zip(list(zip(pop.lat_f, pop.lon_f)), list(pop.population)))
    countries = []

    mask["pm25"] = [*map(mapped_df.get, list(zip(mask.lat_f, mask.lon_f)))]
    mask["population"] = [*map(mapped_pop.get, list(zip(mask.lat_f, mask.lon_f)))]
    for country in np.unique(mask["mask"]):
        country_df = mask.loc[mask["mask"] == country, :]
        popfrac = country_df.population * country_df.frac
        pw_pm = np.sum(country_df.pm25 * popfrac) / np.sum(popfrac)
        countries.append(pd.DataFrame({"pw_pm": [pw_pm], "id": [country]}))
    return pd.concat(countries).set_index("id")


def calculate_scale_factor(old_pm25, new_pm25, pop, mask, old_sf, out_dir=None):
    """
    Calculates scale factor based on the ratio of country-scale population-weighted pm2.5 from the old product to the new product

    Parameters:
    -----------
    old_pm25 : pandas.DataFrame
        DataFrame containing the old satellite-derived product used in FATE.
    new_pm25 : pandas.DataFrame
        DataFrame containing the new satellite-derived product to update to.
    pop      : pandas.DataFrame
        DataFrame containing population data.
    mask     : pandas.DataFrame
        DataFrame containing the mask file used to match the grid to specific countries.
    out_dir  : str
        A string that if specified will write a .csv file to the out_dir location.

    Returns:
    --------
    pandas.DataFrame
        Dataframe of scaling factors for every country

    """
    old_country_pm25 = calculate_country_pm25(old_pm25, pop, mask)
    new_country_pm25 = calculate_country_pm25(new_pm25, pop, mask)
    sf = new_country_pm25.pw_pm / old_country_pm25.pw_pm
    sf = sf.rename({"pw_pm": "pm_sat_rsfct"})
    new_sf = old_sf.copy()
    # Adds new scaling factor to old file structure retaining values of 1.
    new_sf["pm_sat_rsfct"] = [
        sf[sf.index == i].iloc[0] if (factor != 1) & (any(sf.index == i)) else 1
        for i, factor in old_sf["pm_sat_rsfct"].items()
    ]
    # Write the new scaling factor to csv
    if out_dir:
        new_sf.to_csv(f"{out_dir}rescaling_factors")
    return sf
