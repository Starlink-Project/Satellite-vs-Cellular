import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def lineplot_throughput_speed():
    folder_path = os.path.join(os.getcwd(),'UDP','Downlink')
    speed_ranges = [(0, 10), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60),(60,70),(70,80),(80,90)]
    legends = ['MOB','Cellular']

    rv_throughputs_up = [[] for _ in range(len(speed_ranges))]
    rv_in_motion_throughputs_up = [[] for _ in range(len(speed_ranges))]
    rv_throughputs_down = [[] for _ in range(len(speed_ranges))]
    rv_in_motion_throughputs_down = [[] for _ in range(len(speed_ranges))]
    cellular_throughputs_up = [[] for _ in range(len(speed_ranges))]
    cellular_throughputs_down = [[] for _ in range(len(speed_ranges))]


    csv_files = [f for f in os.listdir(folder_path) if f.endswith('_all_area.csv') and f.startswith('delurban') ]

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        for i, (low, high) in enumerate(speed_ranges):
            mask = (df["speed"]*1.609344 >= low) & (df["speed"]*1.609344 < high) & (df["speed"]*1.609344 <= 60*1.609344)
            throughput_col = df.loc[mask, "throughput"].tolist()
            if "RV" in csv_file and "In-motion" not in csv_file:
                rv_throughputs_down[i].extend(throughput_col)
            elif 'RV-In-motion' in csv_file:
                rv_in_motion_throughputs_down[i].extend(throughput_col)
            elif 'delurban_AT_T' in csv_file or 'delurban_T-mobile' in csv_file or 'delurban_Verizon' in csv_file:
                cellular_throughputs_down[i].extend(throughput_col)

    fig, ax = plt.subplots()
    fig.set_size_inches(9.2, 5.5)
    all_throughputs = [rv_in_motion_throughputs_down,cellular_throughputs_down]
    elements = []
    colors = ['C0','C1']
    marks = ['o','*']
    linestles = ['-','-']
    for np_Idx, np_data in enumerate(all_throughputs):
        mean_throughputs = []
        std_throughputs = []
        x_positions = [1,2,3,4,5,6,7,8,9]
        for sp_Idx,sp_data in enumerate(np_data):
            mean_throughput = np.mean(sp_data)
            std_throughput = np.std(sp_data)
            mean_throughputs.append(mean_throughput)
            std_throughputs.append(std_throughput)
        elements.append(ax.plot(x_positions,mean_throughputs,colors[np_Idx],linestyle=linestles[np_Idx],marker= marks[np_Idx],linewidth=4,label =legends[np_Idx]))
        speed_ra = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
    xtick_labels = [f"{a}-{b}" for a, b in zip(speed_ra[:-1], speed_ra[1:])]
    xtick_labels.insert(0,'0-0')
    fzsize = 21
    legend = ax.legend(prop={'size': 22})
    ax.set_xticklabels(xtick_labels)
    ax.tick_params(axis='y', labelsize=fzsize)
    ax.tick_params(axis='x', labelsize=fzsize,rotation=20)
    ax.set_xlabel('Moving Speed (Km/h)',fontsize=fzsize)
    ax.set_ylabel('Throughput (Mbps)',fontsize=fzsize)
    plt.ylim(0,180)
    plt.grid(True)
    plt.tight_layout()
    #plt.show()
    folder_path = os.path.join(os.getcwd())
    figname = os.path.join(folder_path,'Speed_line.jpg')
    plt.savefig(figname)
    figname = os.path.join(folder_path,'Speed_line.pdf')
    plt.savefig(figname)
    plt.close()

if __name__ == '__main__':
    lineplot_throughput_speed()