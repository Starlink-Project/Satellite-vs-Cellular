import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def plotcdfUDPPing(foldername):
    folder_path = os.path.join(os.getcwd(), foldername)
    df_list = []

    file_config = {
        'att_udpping_summary.csv': {'label': 'ATT', 'linestyle': '-'},
        'tm_udpping_summary.csv': {'label': 'TM', 'linestyle': '-'},
        'vz_udpping_summary.csv': {'label': 'VZ', 'linestyle': '-'},
        'rm_udpping_summary.csv': {'label': 'RM', 'linestyle': '--'},
        'mob_udpping_summary.csv': {'label': 'MOB', 'linestyle': '--'}
    }

    for file_name, config in file_config.items():
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        df = df[df["RTT"] != "timeo"]
        df_list.append((df, config['label'], config['linestyle']))

    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    plt.xlim(0, 160)
    plt.ylim(0, 1.02)
    colors = ['C0', 'C1', 'C2', 'C3', 'C4']

    for idx, (df, legend_label, linestyle) in enumerate(df_list):
        rtt_data = df["RTT"].astype(float)
        rtt_data = rtt_data[(rtt_data <= 3000) & (rtt_data > 0)]
        sorted_data = np.sort(rtt_data)
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        count, bins_count = np.histogram(rtt_data, bins=np.unique(rtt_data).shape[0])
        cdf = np.cumsum(count / sum(count))
        plt.plot(bins_count[1:], cdf, linestyle=linestyle, label=legend_label, color=colors[idx % len(colors)], linewidth=4)
    
    fzsize = 20
    ax.legend(prop={'size': fzsize})
    ax.tick_params(axis='y', labelsize=fzsize)
    ax.tick_params(axis='x', labelsize=fzsize)
    ax.set_xlabel('RTT (ms)', fontsize=fzsize)
    ax.set_ylabel('CDF', fontsize=fzsize)
    ax.set_xticks([0, 25, 50, 75, 100, 125, 150])
    ax.set_xticklabels(['0', '25', '50', '75', '100', '125', '150'])

    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), 'udpping_latency.pdf'))

if __name__ == '__main__':
    plotcdfUDPPing('UDPPingAll')
