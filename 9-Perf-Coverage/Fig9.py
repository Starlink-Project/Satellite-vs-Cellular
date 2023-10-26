import os
import pandas as pd
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
import matplotlib.pyplot as plt

def coveragePrec(foldername, direction):
    folder_path = os.path.join(os.getcwd(), foldername, direction)

    bins = [0, 20, 50, 100, float('inf')]
    labels = ['Very Low', 'Low', 'Medium', 'High']
    coverage_data = {label: [] for label in labels}
    filenames = [
        "att_all.csv", 
        "tm_all.csv", 
        "vz_all.csv", 
        "best_cl.csv", 
        "rm_all.csv", 
        "best_rm.csv", 
        "mob_all.csv", 
        "best_mob.csv"
    ]

    for filename in filenames:
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        column_values = df.iloc[:, 1].values

        bin_counts = pd.Series(pd.cut(column_values, bins=bins, labels=labels, right=False)).value_counts(normalize=True)
        for label in labels:
            coverage_data[label].append(bin_counts.get(label, 0))

    print(coverage_data)
    return coverage_data

def barcoveragePrec():
    categories = ['ATT', 'TM', 'VZ', 'BestCL', 'RM', 'RM+CL', 'MOB', 'MOB+CL']

    cmap20 = plt.cm.tab20
    colors = [cmap20(i) for i in [1, 5, 3, 7]]
    hatch_colors = [cmap20(i) for i in [0, 4, 2, 6]]
    hatch_styles = ['//', 'oo', '++', '\\\\']

    coverage_data = coveragePrec('UDP', 'Downlink')

    fig, ax = plt.subplots()
    fig.set_size_inches(12, 6.9)
    bar_positions = range(len(categories))

    accumulated_data = [0] * len(categories)
    for idx, label in enumerate(['Very Low', 'Low', 'Medium', 'High']):
        ax.bar(bar_positions, coverage_data[label], bottom=accumulated_data, label=label, color=colors[idx], hatch=hatch_styles[idx], edgecolor=hatch_colors[idx])
        accumulated_data = [x + y for x, y in zip(accumulated_data, coverage_data[label])]

    ftsize = 26
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(categories)
    ax.set_ylabel('Coverage Percentage', fontsize=ftsize)
    ax.set_xlabel('Network Provider', fontsize=ftsize)
    
    legend = ax.legend(prop={'size': ftsize}, loc='upper center', bbox_to_anchor=(0.45, 1.18), ncol=4)
    ax.xaxis.set_tick_params(labelsize=23, rotation=0)
    ax.yaxis.set_tick_params(labelsize=ftsize)
    
    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), 'Fig9.pdf'), bbox_inches='tight')

if __name__ == '__main__':
    barcoveragePrec()
