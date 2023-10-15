# Download Throughput for Different Networks

This folder contains the dataset and plotting scripts for the Starlink and cellular network throughput measurements (Figure 1 in the paper) conducted using 5GTracker.

## Folder Structure

| Filename | Description |
|---|---|
| `att_all_area1.csv` | Dataset of AT&T (cellular) throughput used in this figure. |
| `mob_all_area1.csv` | Dataset of Mobility (Starlink) throughput used in this figure. |
| `tm_all_area1.csv` | Dataset of T-mobile (cellular) throughput used in this figure. |
| `vz_all_area1.csv` | Dataset of Verizon (cellular) throughput used in this figure. |
| `Fig1.py` | Python script for plotting. |

## Dataset Description

The dataset files `att_all_area1.csv`, `mob_all_area1.csv`, `tm_all_area1.csv`, and `vz_all_area1.csv` contain several fields. We provide descriptions for each field below.

| Field name | Description of the field |
|---|---|
| `time` | Timestamp of the test |
| `throughput` | Downlink throughput in Megabits per second (Mbps) |
| `speed` | Driving speed while experiments in miles per hour (Mph) |
| `latitude` | Latitude of the location while experiments |
| `longtitu` | Longitude of the location while experiments |

## Generating plots

The provided script here is to generate Figure 1 shown in the paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- NumPy (>= 1.26.0)
- os

### Running code

After cloning the repository, navigate to the `Figure1` folder and simply run the following command.

`python Fig1.py`

If everything succeeds, the figure should be created with the format '.pdf'.
