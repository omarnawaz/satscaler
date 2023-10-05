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
The required data for this project is located in the data/ directory. It includes:

pm25.csv: The old satellite-derived PM2.5 data used in FATE.
population.csv: Population data.
mask.csv: Mask file used to match the grid to specific countries.
Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue on the GitHub repository.

##License
This project is licensed under the MIT License.