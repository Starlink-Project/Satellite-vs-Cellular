# Throughput over Speed

This folder contains the dataset and plotting scripts for the Throughput over speed for Starlink networks and cellular networks (Figure 6 in the paper) conducted using 5GTracker.
## Folder Structure   

| Filename                    | Description                                                         |
|------------------------------------------|--------------------------------------------------------|
|`UDP/Downlink/delurban_[Network Provider]_all_area.csv`|The files under this folder are the dataset of samples of throughput and moving speed.|
| `Fig6.py` | Python script to generate plots.|

## Dataset Description

The dataset files `UDP/Downlink/delurban_[Network Provider]_all_area.csv` contain several fields. We provide descriptions for each field below.

| Field name           | Description of the field                                           |
|----------------------|--------------------------------------------------------------------|
| `time`               | Timestamp of the test                           |
| `throughput`         | Downlink throughput in Megabits per second (Mbps)                  |
| `speed`        | Driving speed while experiments in miles per hour (Mph)                   |
| `latitude`         | Latitude of the location while experiments                             |
| `longtitu`    |Longitude of the location while experiments|
|`area_type`|Area type of the location while experiments|

## Generating plots

The provided script here is to generate Figure 6 shown in our paper.
### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- NumPy (>= 1.26.0)
- os

### Running code


After cloning the repository, navigate to the `Figure6` folder and simply run the following command.

`python Fig6.py`

If everything succeeds, figures of throughput over speed should be created with the formats '.jpg' and '.pdf'.
