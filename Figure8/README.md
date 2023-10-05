# Throughput over different area types.

This folder contains the dataset and plotting scripts for the Throughput over different area types for Starlink networks and cellular networks (Figure 8 in the paper) conducted using 5GTracker.
## Folder Structure   

| Filename                    | Description                                                         |
|------------------------------------------|--------------------------------------------------------|
|`UDP/Downlink/[Network Provider]_all_area1.csv`|The files under this folder are the dataset of samples of throughput and area types.|
| `Fig8.py` | Python script to generate plots.|

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

The provided script here is to generate Figure 8 shown in our paper.
### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- os

### Running code


After cloning the repository, navigate to the `Figure8` folder and simply run the following command.

`python Fig8.py`

If everything succeeds, figures of throughput over three types of areas should be created with the format '.pdf'.
