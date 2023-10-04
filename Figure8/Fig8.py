import os
import matplotlib.pyplot as plt
import pandas as pd

def load_data_for_area(folder_path, area_ranges):
    throughputs_data = {
        'mob': [[] for _ in range(len(area_ranges))],
        'vz': [[] for _ in range(len(area_ranges))]
    }

    csv_files = [f for f in os.listdir(folder_path) if '_all_area1.csv' in f]

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        for i, area_t in enumerate(area_ranges):
            mask = (df["area_type"] == area_t)
            throughput_col = df.loc[mask, "throughput"].tolist()
            for key in throughputs_data:
                if csv_file.startswith(key):
                    throughputs_data[key][i].extend(throughput_col)

    return throughputs_data


def box_throughput_area(foldername, direction):
    folder_path = os.path.join(os.getcwd(), foldername, direction)
    area_ranges = ['urban', 'suburban', 'rural']
    throughputs_data = load_data_for_area(folder_path, area_ranges)

    fig, ax = plt.subplots()
    fig.set_size_inches(5.5, 4)
    fzsize = 18

    cmap20 = plt.cm.tab20
    colors = [cmap20(i) for i in [1, 5]]
    hatch_colors = [cmap20(i) for i in [0, 4]]
    hatches = ['//', 'oo']

    x_positions = [0.9, 1.1, 1.5, 1.7, 2.1, 2.3]
    alllabels = ['Cellular', 'MOB', 'Cellular', 'MOB', 'Cellular', 'MOB']

    selected_data = [throughputs_data['vz'], throughputs_data['mob']]
    transposed_list = [item for sublist in selected_data for item in sublist]

    boxes = []
    for idx, ele in enumerate(transposed_list):
        box = ax.boxplot(ele, positions=[x_positions[idx]], widths=0.2, patch_artist=True, boxprops=dict(facecolor=colors[idx % 2], hatch=hatches[idx % 2], edgecolor=hatch_colors[idx % 2]), showfliers=False, labels=[alllabels[idx]])
        boxes.append(box)

    xtick_labels = ['Urban', 'Suburban', 'Rural']
    x_ticks = [1, 1.6, 2.2]
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(xtick_labels, fontsize=fzsize)
    
    legend_boxes = [boxes[0]['boxes'][0], boxes[1]['boxes'][0]]
    legend_labels = ['Cellular', 'MOB']
    legend = ax.legend(legend_boxes, legend_labels, loc='upper left', bbox_to_anchor=(0.17, 1.03), prop={'size': fzsize}, ncol=2)

    plt.xlim(0.7, 2.5)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), 'Fig8.pdf'), bbox_inches='tight')

if __name__ == '__main__':
    box_throughput_area('UDP', 'Downlink')
