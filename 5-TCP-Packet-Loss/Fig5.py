import matplotlib.pyplot as plt
import os

def boxtcppkloss():
    data = {
        'ATT': [[0/194111, 7/161272, 6/199032, 4/154672], 
                [547/79144, 37/81596, 3/176617, 807/469957, 310/594958, 0/299397]],
        'TM': [[12/155269, 216/154128, 2/154377, 0/148069], 
               [4/129681, 0/98653, 5/161002, 29/954485, 15/882580, 1766/987599]],
        'VZ': [[1645/1576530, 633/973711, 37/976522, 29/892062, 0/385585],
               [0/26577, 1524/606425, 86/107937, 0/26288, 0/51493]],
        'RM': [[140/11300, 64/12100, 42/13876, 68/1356, 116/21532, 70/11017, 518/54518],
               [980/71322, 886/73100, 736/71902, 671/75382, 106/35013, 210/88982, 498/137236]],
        'MOB': [[881/227698, 656/234417, 475/112690, 11/1344, 48/6719, 50/6754], 
                [528/143016, 1400/502007, 231/28219, 150/15514]]
    }

    fig, ax = plt.subplots(figsize=(10, 4.5))

    cmap20 = plt.cm.tab20
    colors = [cmap20(i) for i in [3, 9]]
    hatch_colors = [cmap20(i) for i in [2, 8]]
    hatches = ['///', 'xxx']
    directions = ['Uplink', 'Downlink']
    legend_handles = []
    
    for idx, (label, datalist) in enumerate(data.items()):
        for j, direction_data in enumerate(datalist):
            position = 1 + 0.6 * idx + 0.2 * j - 0.1
            box = ax.boxplot([100*d for d in direction_data], positions=[position], 
                       widths=0.2, patch_artist=True, showfliers=False, 
                       medianprops=dict(color=cmap20(6), linewidth=2), 
                       boxprops=dict(facecolor=colors[j], hatch=hatches[j], edgecolor=hatch_colors[j]))
            if label == list(data.keys())[0]: 
                legend_handles.append(box['boxes'][0])
            
    ax.set_xticks([1 + 0.6 * idx for idx in range(len(data))])
    ax.set_xticklabels(list(data.keys()), fontsize=22)
    ax.set_ylabel('Packet Loss (%)', fontsize=22)
    ax.set_xlabel('Network Provider', fontsize=22)
    ax.legend(legend_handles, directions, loc='upper left', fontsize=22, bbox_to_anchor=(0.05, 0.95))
    ax.xaxis.set_tick_params(labelsize=22)
    ax.yaxis.set_tick_params(labelsize=22)
    plt.xlim(0.7, len(data) * 0.6 + 0.7)

    ax.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), 'tcp_packetloss.pdf'))

if __name__ == '__main__':
    boxtcppkloss()
