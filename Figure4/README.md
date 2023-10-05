# UDP-Ping Comparison and Analysis

This folder contains the dataset and plotting scripts for the Latency comparison between Starlink networks and Cellular networks (Figure 4 in the paper) conducted using UDP-Ping.

## Folder Structure   

| Filename | Description |
|---|---|
| `UDPPingAll/[Network Provider]_udpping_summary.csv.zip` | Dataset of UDP Ping of 5 network providers. |
| `Fig4.py` | Python script to generate plots. |

## Generating plots

The provided script here is to generate Figure 4 shown in our paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- NumPy (>= 1.26.0)
- os

### Running code

- After cloning the repository, navigate to the `Figure4` folder.
- Navigate to the 'UDPPingAll' folder and decompress all five '.zip' files into the same folder.
- Simply run the following command.

```
unzip '*.zip'
python Fig4.py
```

If everything succeeds, the figure of UDP Ping comparison should be created with the format '.pdf'.
