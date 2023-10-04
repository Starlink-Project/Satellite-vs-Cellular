import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


def throughputcdf(type):
    rv_throughputs_tcp = []
    rv_in_motion_throughputs_tcp = []
    rv_throughputs_udp = []
    rv_in_motion_throughputs_udp = []
    cellular_throughputs_udp = []
    cellular_throughputs_udp = []
    rv_in_motion_throughputs_udp_uplink = []
    if type == 'TCPVSUDP' or type =='RVVSRVIM':
        direction = 'Downlink'
    elif type == 'UPVSDOWN':
        direction = 'Downlink'
        direction2 = 'Uplink'
        folder_path3 = os.path.join(os.getcwd(),'UDP',direction2)
        csv_file3 = [f for f in os.listdir(folder_path3) if f.endswith('_all_area.csv') and 'delurban' not in f and 'RV-In-motion' in f]
        file_path = os.path.join(folder_path3, csv_file3[0])
        df = pd.read_csv(file_path)
        rv_in_motion_throughputs_udp_uplink = np.array(df['throughput'])
    folder_path1 = os.path.join(os.getcwd(),'TCP',direction)
    folder_path2 = os.path.join(os.getcwd(),'UDP',direction)
    legends = ['RM-TCP','MOB-TCP','Celluar-TCP','RM-UDP','MOB-UDP','Cellular-UDP']
    if type == 'TCPVSUDP':
        legends = ['MOB-TCP','Celluar-TCP','MOB-UDP','Cellular-UDP']
    elif type == 'RVVSRVIM':
        legends = ['RM','MOB']
    elif type == 'UPVSDOWN':
        legends = ['Uplink','Downlink']
    
    if direction == 'Uplink':
        csv_files2 = [f for f in os.listdir(folder_path2) if (f.endswith('_all.csv') and 'delurban' not in f and 'RV' not in f) or (f.endswith('_all_area.csv') and 'delurban' not in f and 'RV' in f and 'modified' in f)]
        csv_files1=  [f for f in os.listdir(folder_path1) if f.endswith('_all_area.csv') and 'delurban' not in f ]
    else:
        csv_files2 = [f for f in os.listdir(folder_path2) if f.endswith('_all.csv') and  'delurban' not in f]
        csv_files1 = [f for f in os.listdir(folder_path1) if f.endswith('_all_area.csv') and 'delurban' not in f ]

    for csv_file in csv_files1:
        file_path = os.path.join(folder_path1, csv_file)
        df = pd.read_csv(file_path)
        if "RV" in csv_file and "In-motion" not in csv_file:
            rv_throughputs_tcp = np.array(df['throughput'])
        elif 'RV-In-motion' in csv_file:
            rv_in_motion_throughputs_tcp = np.array(df['throughput'])
        elif 'AT_T' in csv_file or 'T-mobile' in csv_file or 'Verizon' in csv_file:
            cellular_throughputs_tcp = np.array(df['throughput'])
    
    for csv_file in csv_files2:
        file_path = os.path.join(folder_path2, csv_file)
        df = pd.read_csv(file_path)
        if "RV" in csv_file and "In-motion" not in csv_file:
            rv_throughputs_udp = np.array(df['throughput'])
        elif 'RV-In-motion' in csv_file:
            rv_in_motion_throughputs_udp = np.array(df['throughput'])
        elif 'AT_T' in csv_file or 'T-mobile' in csv_file or 'Verizon' in csv_file:
            cellular_throughputs_udp = np.array(df['throughput'])

    fig, ax = plt.subplots()
    all_throughputs = [rv_throughputs_tcp,rv_in_motion_throughputs_tcp,cellular_throughputs_tcp,rv_throughputs_udp,rv_in_motion_throughputs_udp,cellular_throughputs_udp]
    colors = ['C0','C1','C2','C0','C1','C2']
    linestles = ['--','--','--','-','-','-']
    if type == 'TCPVSUDP':
        all_throughputs = [rv_in_motion_throughputs_tcp,cellular_throughputs_tcp,rv_in_motion_throughputs_udp,cellular_throughputs_udp]
        colors = ['C0','C1','C0','C1']
        linestles = ['--','--','-','-']
    elif type == 'RVVSRVIM':
        all_throughputs = [rv_throughputs_udp,rv_in_motion_throughputs_udp]
        colors = ['C2','C0']
        linestles = ['-','-']
    elif type == 'UPVSDOWN':
        all_throughputs = [rv_in_motion_throughputs_udp_uplink,rv_in_motion_throughputs_udp]
        colors = ['C4','C1']
        linestles = ['-','-']
    for Idx,data in enumerate(all_throughputs):
        sorted_data = np.sort(data)
        cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)


        count, bins_count = np.histogram(data, bins = np.unique(data).shape[0])
        pdf = count / sum(count)
        cdf = np.cumsum(pdf)
        
        plt.plot(bins_count[1:],cdf,label = legends[Idx],color=colors[Idx],linestyle =linestles[Idx] ,linewidth=3)
    fzsize = 22
    if type == 'TCPVSUDP':
        plt.xlim(0,600)

    ax.tick_params(axis='y', labelsize=fzsize)
    ax.tick_params(axis='x', labelsize=fzsize)
    ax.set_xlabel('Throughput (Mbps)',fontsize=fzsize)
    ax.set_ylabel('CDF',fontsize=fzsize)
    legend = ax.legend(prop={'size': 20})
    x_ticks = [0, 100, 200, 300, 400, 500, 600]
    x_tick_labels = ['0', '100', '200', '300', '400', '500', '600']
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_tick_labels)

    plt.grid(True)
    plt.tight_layout()
    #plt.show()
    folder_path = os.path.join(os.getcwd())
    figname = os.path.join(folder_path,direction+'ThroughputAllCDF4.jpg')
    if type == 'TCPVSUDP':
        figname = os.path.join(folder_path,direction+'TCPVSUDP.jpg')
    elif type == 'RVVSRVIM':
        figname = os.path.join(folder_path,direction+'RVVSRVIM.jpg')
    elif type == 'UPVSDOWN':
        figname = os.path.join(folder_path,direction+'UPVSDOWN.jpg')
    plt.savefig(figname)
    figname = os.path.join(folder_path,direction+'ThroughputAllCDF4.pdf')
    if type == 'TCPVSUDP':
        figname = os.path.join(folder_path,direction+'TCPVSUDP.pdf')
    elif type == 'RVVSRVIM':
        figname = os.path.join(folder_path,direction+'RVVSRVIM.pdf')
    elif type == 'UPVSDOWN':
        figname = os.path.join(folder_path,direction+'UPVSDOWN.pdf')
    plt.savefig(figname)
    plt.close()

if __name__ == '__main__':
    throughputcdf('TCPVSUDP')
    throughputcdf('RVVSRVIM')
    throughputcdf('UPVSDOWN')
    