# Throughput over different area types.

This folder contains the dataset and plotting scripts for throughput progression over time for single-path TCP and MPTCP iPerf download (Figure 11 in the paper). It consists of two subfigures, AT&T and Mobility, Verizon and Mobility.

## Folder Structure   

The dataset contain several data files. We provide descriptions for each file below.

| Filename | Description |
|---|---|
| `mob_att_mp.txt` | MPTCP iPerf download trace for using Mobility and AT&T |
| `mob_att_sp_att.txt` | TCP iPerf download trace using AT&T |
| `mob_att_sp_mob.txt` | TCP iPerf download trace using Mobility |
| `mob_vz_mp.txt` | MPTCP iPerf download trace using Mobility and Verizon |
| `mob_vz_sp_mob.txt` | TCP iPerf download trace using Mobility |
| `mob_vz_sp_vz.txt` | TCP iPerf download trace using Verizon |
| `parse_iperf.py` | Python script to parse data and generate plots.|

## Generating plots

The provided script here is to generate Figure 11 shown in our paper.

### Requirements

Here are the software/package requirements. The version number in the bracket indicates the minimum version that our script has been tested on.

- Python 3 (>= 3.7.7)
- argparse (>= 1.1)
- Matplotlib (>= 3.3.1)
- numpy (>= 1.26.0)

### Running code

After cloning the repository, navigate to the `Figure11` folder and simply run the following command.

`python parse_iperf.py --fig a`
`python parse_iperf.py --fig b`

If everything succeeds, figures of network performance coverage should be created with the formats '.pdf'.
