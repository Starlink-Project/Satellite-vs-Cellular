import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

def plotcdfUDPPing(foldername):
    folder_path = os.path.join(os.getcwd(),foldername)
    df_list = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith("Summary.csv"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)

            df = df[df["RTT"] != "timeo"]

            legend_label = file_name.split("_UDP_Ping")[0]
            
            df_list.append((df, legend_label))
    df_list = [df_list[2],df_list[3],df_list[4],df_list[0],df_list[1]]

    fig, ax = plt.subplots()
    colors = ['C0','C1','C2','C3','C4']
    for df, legend_label in df_list:
        rtt_data = df["RTT"]
        rtt_data = rtt_data.astype(float)
        rtt_data = rtt_data[rtt_data <= 3000 ]
        rtt_data = rtt_data[rtt_data>0]
        sorted_data = np.sort(rtt_data)
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        count, bins_count = np.histogram(rtt_data, bins = np.unique(rtt_data).shape[0])
        pdf = count / sum(count)
        cdf = np.cumsum(pdf)
        colors = ['C0','C1','C2','C3','C4']
        linestyle = '-'
        if legend_label == 'AT-T':
            legindex = 0
            legend_label = 'ATT'
        elif legend_label == 'T-mobile':
            legindex = 1
            legend_label = 'TM'
        elif legend_label == 'Verizon':
            legindex = 2
            legend_label = 'VZ'
        elif legend_label == 'RV':
            legindex = 3
            legend_label = 'RM'
            linestyle= '--'
        elif legend_label == 'RV-In-motion':
            legindex = 4
            legend_label = 'MOB'
        plt.plot(bins_count[1:],cdf,linestyle=linestyle,label = legend_label,color=colors[legindex%len(colors)],linewidth=3)
         
    plt.xlim([0, 150])
    fzsize = 20
    legend = ax.legend(prop={'size': fzsize})
    ax.tick_params(axis='y', labelsize=fzsize)
    ax.tick_params(axis='x', labelsize=fzsize)
    ax.set_xlabel('RTT (ms)',fontsize=fzsize)
    ax.set_ylabel('CDF',fontsize=fzsize)
    plt.grid(True)
    plt.tight_layout()
    #plt.show()
    x_ticks = [0, 25, 50, 75, 100,125,150]
    x_tick_labels = ['0', '25', '50', '75', '100','125','150']
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_tick_labels)
    fig_path = os.path.join(os.getcwd())
    figname = os.path.join(fig_path,'UDPPingCDF.jpg')
    plt.savefig(figname)
    figname = os.path.join(fig_path,'UDPPingCDF.pdf')
    plt.savefig(figname)
    plt.close()

if __name__ == '__main__':
    plotcdfUDPPing('UDPPingAll')