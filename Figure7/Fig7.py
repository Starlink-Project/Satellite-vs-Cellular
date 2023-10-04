import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def ImproveBarParallel(foldername,direction):

    folder_path = os.path.join(os.getcwd(),foldername,direction)
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 4)
    RVdata = [0]*3
    Cellulardata = [0]*3
    RVFile = [0]*3
    CellularFile= [0]*3
    for file_name in os.listdir(folder_path):
        if file_name.endswith("parallel.csv"):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            throughput_data = df.iloc[:, 0].values
            summary_idx = file_name.index("Summary-") + len("Summary-")
            mmwave_tracker_idx = file_name.index("Iperf_mmWaveTracker")
            legend_label = file_name[summary_idx:mmwave_tracker_idx]  + file_name[-13:-4]
            networkprovider = file_name[summary_idx:mmwave_tracker_idx-1]
            if networkprovider == 'RV' and file_name.endswith('1parallel.csv'):
                RVdata[0] = throughput_data
                RVFile[0] = file_name
            elif networkprovider == 'RV' and file_name.endswith('4parallel.csv'):
                RVdata[1] = throughput_data
                RVFile[1] = file_name
            elif networkprovider == 'RV' and file_name.endswith('8parallel.csv'):
                RVdata[2] = throughput_data
                RVFile[2] = file_name
            elif networkprovider == 'AT_T' and file_name.endswith('1parallel.csv'):
                Cellulardata[0] = throughput_data
                CellularFile[0] = file_name
            elif networkprovider == 'AT_T' and file_name.endswith('4parallel.csv'):
                Cellulardata[1] = throughput_data
                CellularFile[1] = file_name
            elif networkprovider == 'AT_T' and file_name.endswith('8parallel.csv'):
                Cellulardata[2] = throughput_data
                CellularFile[2] = file_name

    data=[Cellulardata[0],Cellulardata[1],Cellulardata[2],RVdata[0],RVdata[1],RVdata[2]]
    fzsize = 18

    total_delta_percent1 = (np.mean(data[1]) - np.mean(data[0])) / np.mean(data[0]) * 100
    total_delta_percent2 = (np.mean(data[2]) - np.mean(data[0])) / np.mean(data[0]) * 100
    total_delta_percent3 = (np.mean(data[4]) - np.mean(data[3])) / np.mean(data[3]) * 100
    total_delta_percent4 = (np.mean(data[5]) - np.mean(data[3])) / np.mean(data[3]) * 100

    plt.barh(['Cellular\n4P'], [total_delta_percent1], color='C0')
    plt.barh(['Cellular\n8P'], [total_delta_percent2], color='C0')
    plt.barh(['Roam\n4P'], [total_delta_percent3], color='C2')
    plt.barh(['Roam\n8P'], [total_delta_percent4], color='C2')

    plt.xlabel('Improvement Percentage (100%)')
    
    ax.tick_params(axis='y', labelsize=fzsize)
    ax.tick_params(axis='x', labelsize=fzsize)
    ax.set_xlabel('Improvement Percentage (100%)',fontsize=fzsize)
    plt.grid(True)
    plt.tight_layout()
    #plt.show()
    figpath = os.getcwd()
    figname = os.path.join(figpath,'parallelImprove.jpg')
    plt.savefig(figname)
    figname = os.path.join(figpath,'parallelImprove.pdf')
    plt.savefig(figname)
    plt.close()

if __name__ == '__main__':
    ImproveBarParallel('TCP','Downlink')