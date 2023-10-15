# TCP Packet Loss Comparison and Analysis

This folder contains plotting scripts for the TCP Packet Loss between Starlink and Cellular networks (Figure 5 in the paper) conducted using TCPDump. The data used in this figure are from the tcpdump we collected during the experiment. We have extracted the data by manually analyzing tcpdump on Wireshark. 

## Folder Structure

| Filename | Description |
|---|---|
| `Fig5.py` | Python script to generate plots. |

## Generating plots

The provided script here is to generate Figure 5 shown in our paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Matplotlib (>= 3.3.1)
- NumPy (>= 1.26.0)
- os

### Running code

After cloning the repository, navigate to the `Figure5` folder. Then Simply run the following command.

`python Fig5.py`

If everything succeeds, the figure of TCP Packet Loss Ratio should be created with the format '.pdf'.
