import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def lineplot_throughput_speed():
    folder_path = os.path.join(os.getcwd(), 'UDP', 'Downlink')
    speed_ranges = [(i, i+10) for i in range(0, 90, 10)]
    legends = ['MOB', 'Cellular']

    network_data = {
        'MOB': [[] for _ in speed_ranges],
        'Cellular': [[] for _ in speed_ranges]
    }

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('_all_area.csv') and f.startswith('delurban')]

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        for i, (low, high) in enumerate(speed_ranges):
            mask = (df["speed"]*1.609344 >= low) & (df["speed"]*1.609344 < high) & (df["speed"]*1.609344 <= 60*1.609344)
            throughput_col = df.loc[mask, "throughput"].tolist()
            
            if 'mob' in csv_file:
                network_data['MOB'][i].extend(throughput_col)
            elif any(cellular in csv_file for cellular in ['delurban_att', 'delurban_tm', 'delurban_vz']):
                network_data['Cellular'][i].extend(throughput_col)

    fig, ax = plt.subplots(figsize=(9.2, 5.5))
    cmap20 = plt.cm.tab20
    colors = [cmap20(i) for i in [0, 4]]
    markers = ['o', 'D']

    for idx, (label, data) in enumerate(network_data.items()):
        mean_throughputs = [np.mean(sp_data) for sp_data in data]
        ax.plot(mean_throughputs, color=colors[idx], linestyle='-', marker=markers[idx], ms=14, linewidth=4, label=label)

    xtick_labels = [f"{a}-{b}" for a, b in speed_ranges]
    ax.set_xticks(range(len(xtick_labels)))
    ax.set_xticklabels(xtick_labels, rotation=20, fontsize=21)
    ax.tick_params(axis='y', labelsize=21)
    ax.set_xlabel('Moving Speed (Km/h)', fontsize=22)
    ax.set_ylabel('Throughput (Mbps)', fontsize=22)
    ax.legend(prop={'size': 22}, bbox_to_anchor=(0.34, 0.30))
    ax.set_ylim(0, 180)

    ax.grid(True)    
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.join(os.getcwd()), 'speed_line.pdf'))

if __name__ == '__main__':
    lineplot_throughput_speed()
