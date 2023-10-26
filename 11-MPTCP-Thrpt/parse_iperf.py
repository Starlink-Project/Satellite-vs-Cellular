import numpy as np
import os
import argparse
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
from matplotlib import pyplot as plt

DATA_PATHS = {
    "a": ["mob_att_mp.txt", "mob_att_sp_mob.txt", "mob_att_sp_att.txt"],
    "b": ["mob_vz_mp.txt", "mob_vz_sp_mob.txt", "mob_vz_sp_vz.txt"]
}

LABELS = {
    "a": ["MPTCP", "MOB", "ATT"],
    "b": ["MPTCP", "MOB", "VZ"]
}


def parse_iperf(data_path):
    timestamp, throughput = [], []
    with open(data_path) as f:
        lines = f.readlines()

    while not "sec  " in lines[0]:
        lines.pop(0)
    while "sec  " in lines[0]:
        line = lines.pop(0)
        line_seg = line.split()
        line_seg = line_seg[line_seg.index("sec")-1:]
        timestamp.append(float(line_seg[0].split('-')[0]))
        if 'G' in line_seg[5]:
            throughput.append(float(line_seg[4])*1000)
        elif 'M' in line_seg[5]:
            throughput.append(float(line_seg[4]))  # Mbps
        elif 'K' in line_seg[5]:
            throughput.append(float(line_seg[4])/1000)
        else:
            throughput.append(float(line_seg[4])/1000000)

    return timestamp, throughput

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fig", type=str, default="a", help='figure number (a or b)')
    args = parser.parse_args()
    fig = args.fig.lower()

    timestamps, results = [], []
    for data_path in DATA_PATHS[fig]:
        timestamp, result = parse_iperf(data_path)
        timestamps.append(timestamp)
        results.append(result)

    plt.rcParams.update({'font.size': 18})
    plt.figure(figsize=(10,4))
    plt.xlabel("Time (s)")
    plt.ylabel("Throughput (Mbps)")
    labels = LABELS[fig]
    for i, (timestamp, result) in enumerate(zip(timestamps, results)):
        plt.plot(timestamp, result, label=labels[i], linewidth=1.8)
    plt.legend()
    plt.grid(True, linestyle='--')
    plt.tight_layout()
    plt.savefig(f"mptcp_mob_{LABELS[fig][-1]}.pdf")
