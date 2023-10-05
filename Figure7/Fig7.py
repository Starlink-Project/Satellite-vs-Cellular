import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def ImproveBarParallel(foldername, direction):
    folder_path = os.path.join(os.getcwd(), foldername, direction)
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 4)
    RVdata = [0]*3
    Cellulardata = [0]*3

    cmap20 = plt.cm.tab20
    colors = [cmap20(i) for i in [5, 5, 19, 19]]
    hatch_colors = [cmap20(i) for i in [4, 4, 18, 18]]
    hatches = ['///', '///', 'xxx', 'xxx']

    for file_name in os.listdir(folder_path):
        if file_name.endswith("parallel.csv"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            throughput_data = df.iloc[:, 0].values
            networkprovider = file_name.split('-')[1].split('_')[0]
            
            if networkprovider == 'RM' and file_name.endswith('1parallel.csv'):
                RVdata[0] = throughput_data
            elif networkprovider == 'RM' and file_name.endswith('4parallel.csv'):
                RVdata[1] = throughput_data
            elif networkprovider == 'RM' and file_name.endswith('8parallel.csv'):
                RVdata[2] = throughput_data
            elif networkprovider == 'ATT' and file_name.endswith('1parallel.csv'):
                Cellulardata[0] = throughput_data
            elif networkprovider == 'ATT' and file_name.endswith('4parallel.csv'):
                Cellulardata[1] = throughput_data
            elif networkprovider == 'ATT' and file_name.endswith('8parallel.csv'):
                Cellulardata[2] = throughput_data

    data = Cellulardata + RVdata
    total_delta_percent = [(np.mean(data[i+1]) - np.mean(data[0])) / np.mean(data[0]) * 100 for i in range(2)] + \
                          [(np.mean(data[i+1+3]) - np.mean(data[3])) / np.mean(data[3]) * 100 for i in range(2)]
    
    labels = ['Cellular\n4P', 'Cellular\n8P', 'Roam\n4P', 'Roam\n8P']
    bars = plt.barh(labels, total_delta_percent, color=colors)

    for bar, hatch, hatch_color in zip(bars, hatches, hatch_colors):
        bar.set_hatch(hatch)
        bar.set_edgecolor(hatch_color)

    ax.tick_params(axis='y', labelsize=18)
    ax.tick_params(axis='x', labelsize=18)
    ax.set_xlabel('Improvement Percentage (%)', fontsize=18)

    plt.grid(True)
    plt.tight_layout()
    figname = os.path.join(os.getcwd(), 'parallel.pdf')
    plt.savefig(figname)

if __name__ == '__main__':
    ImproveBarParallel('TCP', 'Downlink')
