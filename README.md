# satscaler

This project calculates a scaling factor to convert the adjoint sensitivities from the old satellite-derived product (van Donkelaar et al. 2016) used in FATE to new satellite-derived products (van Donkelaar et al. 2021).

## Installation

1. Clone the repository: git clone https://github.com/omar_nawaz/satscaler.git
2. Install the required dependencies: (pip install .) or (poetry install)


## Usage

This project is intended to be used to update adjoint sensitivities used in FATE to current satellite-derived datasets.

To use the module:

```python
from data_reader import read_nc
from scaler import calculate_scale_factor

# Load the required dataframes: old_pm25, new_pm25, pop, and mask and format them (see satscaler)

# Call the function
sf = calculate_scale_factor(
    old_pm25=old_pm25,
    new_pm25=new_pm25,
    pop=pop,
    mask=mask,
    out_dir=out_dir,
)
# Results will be saved to "out_dir"
```

Alternatively you can run the "satscaler.py" function straight from the command line. This assumes that your data is stored in "../../data/"

## Data
The required data for this project is placed in the ../../data/ directory and is stored in the "inputs" and "resources" directories in the FATE file structure. It includes:

- fate_inputs/pm25_satellite_grid.nc: The old satellite-derived PM2.5 data used in FATE.
- fate_inputs/population_fine.nc: Fine resolution population data used in FATE.
- fate_inputs/country_mask.nc: Mask file used to match the grid to specific countries.

Additionally, the user should download the current (V5.GL.03) satellite-derive surface-level pm2.5 from WashU at: https://sites.wustl.edu/acag/datasets/surface-pm2-5/. The global product at 0.1° x 0.1° resolution for a base year of 2021 is used in this project currently; however, any file can be used. This file is stored in

- new_satellite_data/V5GL03.HybridPM25c_0p10.Global.202101-202112.nc

## Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue on the GitHub repository.

## License
This project is licensed under the MIT License.