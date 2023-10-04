# Throughput over different area types.

This folder contains the dataset and plotting scripts for the performance comparison between Single-path TCP and MPTCP on file download. (Figure 10 in the paper).
## Folder Structure   

| Filename | Description |
|---|---|
|`mptcp_stats.txt`|The file contains the throughput statistics of single-path TCP and MPTCP file download.|
| `mptcp_stats.gp` | Gnuplot script to generate plots.|

## Dataset Description

The dataset files `mptcp_stats.txt` contain several fields. We provide descriptions for each field below.

| Field name | Description of the field |
|---|---|
| `(column 1)` | Network Type |
| `(column 2)` | (for ordering purpose only) |
| `(column 3)` | Average |
| `(column 4)` | 5-percentile |
| `(column 5)` | 25-percentile |
| `(column 6)` | 50-percentile (median) |
| `(column 7)` | 75-percentile |
| `(column 8)` | 95-percentile |

## Generating plots

The provided script here is to generate Figure 10 shown in our paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Gnuplot 5.4

### Running code


After cloning the repository, navigate to the `Figure10` folder and simply run the following command.

`gnuplot mptcp_stats.txt`

If everything succeeds, figures of network performance coverage should be created with the format '.pdf'.
