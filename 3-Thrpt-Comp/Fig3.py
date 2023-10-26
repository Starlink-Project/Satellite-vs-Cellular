import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

config = {
    'a': {
        'legends': ['MOB-TCP', 'Cellular-TCP', 'MOB-UDP', 'Cellular-UDP'],
        'filename': 'tcp_vs_udp_dl.pdf'
    },
    'b': {
        'legends': ['RM', 'MOB'],
        'filename': 'rm_vs_mob_udp_dl.pdf'
    },
    'c': {
        'legends': ['Uplink', 'Downlink'],
        'filename': 'mob_udp_ul_vs_dl.pdf'
    }
}

def throughputcdf(plot_type):
    folder_path_base = os.getcwd()
    all_throughputs = []

    cmap20 = plt.cm.tab20

    if plot_type == 'a':
        mob_tcp = pd.read_csv(os.path.join(folder_path_base, 'TCP', 'Downlink', 'mob_all_area.csv'))['throughput']
        cellular_tcp_files = [
            pd.read_csv(os.path.join(folder_path_base, 'TCP', 'Downlink', f))['throughput'] 
            for f in ['att_all_area.csv', 'tm_all_area.csv', 'vz_all_area.csv']
        ]
        cellular_tcp = pd.concat(cellular_tcp_files, ignore_index=True)
        
        mob_udp = pd.read_csv(os.path.join(folder_path_base, 'UDP', 'Downlink', 'mob_all.csv'))['throughput']
        cellular_udp_files = [
            pd.read_csv(os.path.join(folder_path_base, 'UDP', 'Downlink', f))['throughput']
            for f in ['att_all.csv', 'tm_all.csv', 'vz_all.csv']
        ]
        cellular_udp = pd.concat(cellular_udp_files, ignore_index=True)
        
        all_throughputs.extend([mob_tcp, cellular_tcp, mob_udp, cellular_udp])
        colors = [cmap20(0), cmap20(4), cmap20(0), cmap20(4)]
        linestyles = ['--', '--', '-', '-']
    
    elif plot_type == 'b':
        rm_udp = pd.read_csv(os.path.join(folder_path_base, 'UDP', 'Downlink', 'rm_all.csv'))['throughput']
        mob_udp = pd.read_csv(os.path.join(folder_path_base, 'UDP', 'Downlink', 'mob_all.csv'))['throughput']
        
        all_throughputs.extend([rm_udp, mob_udp])
        colors = [cmap20(18), cmap20(0)]
        linestyles = ['dashdot', '-']
    
    elif plot_type == 'c':
        mob_udp_down = pd.read_csv(os.path.join(folder_path_base, 'UDP', 'Downlink', 'mob_all.csv'))['throughput']
        mob_udp_up = pd.read_csv(os.path.join(folder_path_base, 'UDP', 'Uplink', 'mob_all_area.csv'))['throughput']
    
        all_throughputs.extend([mob_udp_up, mob_udp_down])
        colors = [cmap20(2), cmap20(8)]
        linestyles = ['-', '-']


    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    plt.xlim(0, 600)
    plt.ylim(0, 1.02)

    for idx, data in enumerate(all_throughputs):
        sorted_data = np.sort(data)
        count, bins_count = np.histogram(sorted_data, bins=np.unique(sorted_data).shape[0])
        cdf = np.cumsum(count) / len(sorted_data)
        plt.plot(bins_count[1:], cdf, label=config[plot_type]['legends'][idx], color=colors[idx], linestyle=linestyles[idx], linewidth=4)

    fzsize = 22
    ax.tick_params(axis='y', labelsize=fzsize)
    ax.tick_params(axis='x', labelsize=fzsize)
    ax.set_xlabel('Throughput (Mbps)', fontsize=fzsize)
    ax.set_ylabel('CDF', fontsize=fzsize)
    legend = ax.legend(prop={'size': 20})
    ax.set_xticks([0, 100, 200, 300, 400, 500, 600])
    ax.set_xticklabels(['0', '100', '200', '300', '400', '500', '600'])
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(folder_path_base, config[plot_type]['filename']))

if __name__ == '__main__':
    throughputcdf('a')
    throughputcdf('b')
    throughputcdf('c')
