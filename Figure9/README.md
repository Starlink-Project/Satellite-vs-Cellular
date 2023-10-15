# Network Performance Coverage

This folder contains the dataset and plotting scripts for the network performance coverage for Starlink and cellular networks (Figure 9 in the paper) conducted using 5GTracker.

## Folder Structure   

| Filename | Description |
|---|---|
| `UDP/Downlink/[Network Provider]_all.csv` | The files under this folder are the dataset of samples of throughput and area types. |
| `Fig9.py` | Python script to generate plots. |

## Dataset Description

The dataset files `UDP/Downlink/[Network Provider]_all.csv` contain several fields. We provide descriptions for each field below.

| Field name | Description of the field |
|---|---|
| `time` | Timestamp of the test |
| `throughput` | Downlink throughput in Megabits per second (Mbps) |
| `speed` | Driving speed while experiments in miles per hour (Mph) |
| `latitude` | Latitude of the location while experiments |
| `longtitu` | Longitude of the location while experiments |

## Generating plots

The provided script here is to generate Figure 9 shown in our paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- os

### Running code

After cloning the repository, navigate to the `Figure9` folder and simply run the following command.

`python Fig9.py`

If everything succeeds, the figure of network performance coverage should be created with the format '.pdf'.
