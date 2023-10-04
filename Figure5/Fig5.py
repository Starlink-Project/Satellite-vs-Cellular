import matplotlib.pyplot as plt
import numpy as np
import os

def boxtcppkloss():
    data1 = [
        [0/194111,7/161272,6/199032,4/154672],
        [547/79144,37/81596,3/176617,807/469957,310/594958,0/299397]
    ]
    
    data2 = [
        [12/155269,216/154128,2/154377,0/148069],
        [4/129681,0/98653,5/161002,29/954485,15/882580,1766/987599]
    ]
    data3 = [
        [1645/1576530,633/973711,37/976522,29/892062,0/385585],
        [0/26577,1524/606425,86/107937,0/26288,0/51493]
    ]

    data4 = [
        [140/11300,64/12100,42/13876,68/1356,116/21532,70/11017,518/54518],
        [980/71322,886/73100,736/71902,671/75382,106/35013,210/88982,498/137236]
    ]
    data5 = [
        [881/227698,656/234417,475/112690,11/1344,48/6719,50/6754],
        [528/143016,1400/502007,231/28219,150/15514]
    ]

    labels = ['ATT', 'TM', 'VZ', 'RM', 'MOB']

    x = np.arange(len(labels))
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 4.5)
    per1 = [100*x for x in data1[0]]
    per2 = [100*x for x in data1[1]]
    per3 = [100*x for x in data2[0]]
    per4 = [100*x for x in data2[1]]
    per5 = [100*x for x in data3[0]]
    per6 = [100*x for x in data3[1]]
    per7 = [100*x for x in data4[0]]
    per8 = [100*x for x in data4[1]]
    per9 = [100*x for x in data5[0]]
    per10 = [100*x for x in data5[1]]
    alldata = [per1,per2,per3,per4,per5,per6,per7,per8,per9,per10]
    colors = ['C0','C2','C0','C2','C0','C2','C0','C2','C0','C2']

    ftsize = 22
    x_positions = [0.9,1.1,1.5,1.7,2.1,2.3,2.7,2.9,3.3,3.5]
    alllabels = ['Uplink','Downlink','Uplink','Downlink','Uplink','Downlink','Uplink','Downlink','Uplink','Downlink']
    boxes = []
    for index, ele in enumerate(alldata):
        box = ax.boxplot(ele,positions=[x_positions[index]],widths=0.2, patch_artist=True, boxprops=dict(facecolor=colors[index]),showfliers=False,labels=[alllabels[index]])
        boxes.append(box)
    xtick_labels = ['ATT','TME','VZ','RM','MOB']
    x_ticks = [1,1.6,2.2,2.8,3.4]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(xtick_labels,fontsize=ftsize)

    ax.set_ylabel('Packet Loss (Percentage)',fontsize=22)
    ax.set_xlabel('Network Provider',fontsize=ftsize)
    
    legend_boxes = [boxes[0]['boxes'][0], boxes[1]['boxes'][0]]
    legend_labels = ['Uplink', 'Downlink']
    legend_position = (0.277, 1)
    legend = ax.legend(legend_boxes,legend_labels,loc='upper left', bbox_to_anchor=legend_position,prop={'size': ftsize})

    ax.xaxis.set_tick_params(labelsize=ftsize)
    ax.yaxis.set_tick_params(labelsize=ftsize)
    plt.tight_layout()
    plt.grid()
    plt.xlim(0.7,3.8)
    #plt.show()
    figname = os.path.join(os.getcwd(),'TCPPacketloss.jpg')
    plt.savefig(figname)
    figname = os.path.join(os.getcwd(),'TCPPacketloss.pdf')
    plt.savefig(figname)

if __name__ == '__main__':
    boxtcppkloss()