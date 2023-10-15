# Impact of TCP Parallelism 

This folder contains the dataset and plotting scripts for the improvement of TCP throughput by parallelism for Starlink and cellular networks (Figure 7 in the paper) conducted using 5GTracker.

## Folder Structure

| Filename | Description |
|---|---|
| `TCP/Downlink/A_TCP_Summary_[Network Provider]-Iperf_mmWaveTracker_classified_Downlink[number of parallel]parallel.csv` | TCP Downlink Throughput over different networks and different numbers of parallels. |
| `Fig7.py` | Python script to generate plots. |

## Dataset Description

The dataset files `TCP/Downlink/A_TCP_Summary_[Network Provider]-Iperf_mmWaveTracker_classified_Downlink[number of parallel]parallel.csv` contain several fields. We provide descriptions for each field below.

| Field name | Description of the field |
|---|---|
| `Bitrate` | TCP Downlink throughput in Megabits per second (Mbps) |
| `Time` | Time slot of the samples while experiments |

## Generating plots

The provided script here is to generate Figure 7 shown in our paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- NumPy (>= 1.26.0)
- os

### Running code

After cloning the repository, navigate to the `Figure7` folder and simply run the following command.

`python Fig7.py`

If everything succeeds, the figure of TCP throughput improvement by parallelism should be created with the format '.pdf'.
