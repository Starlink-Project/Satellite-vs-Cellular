# Throughput Performance Comparison and Analysis

This folder contains the dataset and plotting scripts for the Throughput comparison within Starlink networks (Figure 3 in the paper) conducted using 5GTracker.
## Folder Structure   

| Filename                    | Description                                                                                                |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| `TCP` | The folder that contains the dataset of TCP. |
|`UDP`|The folder that contains the dataset of UDP.|
| `Fig3.py` | Python script to generate plots.|

## Generating plots

The provided script here is to generate Figure 3 shown in our paper.
### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- Pandas (>= 1.1.3)
- Matplotlib (>= 3.3.1)
- NumPy (>= 1.26.0)
- os

### Running code

After cloning the repository, navigate to the `Figure3` folder and simply run the following command.

`python Fig3.py`

If everything succeeds, figures of TCP vs. UDP, Roam vs. Mobility, Uplink vs. Downlink should be created with the formats '.jpg' and '.pdf'.
