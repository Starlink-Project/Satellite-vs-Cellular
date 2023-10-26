import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.colorbar import ColorbarBase

def extract_throughput(csv_file, time1, time2):
    df = pd.read_csv(csv_file, parse_dates=['time'])
    mask = (df['time'] >= time1) & (df['time'] <= time2)
    return df.loc[mask, 'throughput'].tolist()

def plot_color_line(ax, y, data, cmap, max_thrpt, min_thrpt):
    data = np.array(data)
    normalized_data = (data - min_thrpt) / (max_thrpt - min_thrpt)
    for i in range(len(data)):
        color = cmap(normalized_data[i])
        ax.hlines(y, i, i+1, colors=color, linewidth=35)

def plotTimeSeq3(time1, time2):
    folder_path = os.getcwd()
    thrpt = {'att': [], 'tm': [], 'vz': [], 'mob': []}
    filenames = [
        'att_all_area1.csv',
        'tm_all_area1.csv',
        'vz_all_area1.csv',
        'mob_all_area1.csv'
    ]

    for filename in filenames:
        file_path = os.path.join(folder_path, filename)
        key = filename.split('_')[0]
        thrpt[key] = extract_throughput(file_path, time1, time2)

    fig, ax = plt.subplots(figsize=(12.5, 4.2))
    plt.subplots_adjust(left=0.11, right=0.89, bottom=0.17, top=0.95)

    plt.xlabel("Time (s)", fontsize=20)
    cmap_list = [plt.cm.Reds, plt.cm.Oranges, plt.cm.Greens, plt.cm.Blues]
    y_labels = ['ATT\n(AT&T)', 'TM\n(T-Mobile)', 'VZ\n(Verzion)', 'MOB\n(Mobility)']

    max_thrpt = max(max(v) for v in thrpt.values())
    min_thrpt = min(min(v) for v in thrpt.values())
    for i, data in enumerate(thrpt.values()):
        plot_color_line(ax, i+1, data, cmap_list[i], max_thrpt, min_thrpt)

    ax.set_yticks(range(1, len(thrpt) + 1))
    ax.set_yticklabels(y_labels, fontsize=18)
    ax.xaxis.set_tick_params(labelsize=20)

    cax = plt.axes([0.89, 0.17, 0.03, 0.78])
    norm = Normalize(vmin=0, vmax=1)
    cb = ColorbarBase(cax, cmap=plt.cm.Greys, norm=norm, ticks=[0, 0.5, 1])
    cb.set_ticklabels([f"{int(min_thrpt)}", f"{int((max_thrpt - min_thrpt)/2)}", f"{int(max_thrpt)}"])
    cb.set_label("Throughput (Mbps)", fontsize=20)
    cb.ax.tick_params(labelsize=18)

    figname = os.path.join(folder_path, 'Fig1.pdf')
    plt.savefig(figname)
    plt.close()

if __name__ == '__main__':
    plotTimeSeq3(time1='2023-04-9 15:59:00 CDT', time2='2023-04-9 16:18:41 CDT')
