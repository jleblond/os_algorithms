import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import os

FACECOLORS = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:grey', 'tab:yellow']

current_path_str = os.path.dirname(__file__)
SAVE_DIR = os.path.dirname(current_path_str)
RESULTS_DIR = os.path.join(SAVE_DIR, 'outputs/cpu_scheduling/')
if not os.path.isdir(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)


def plot_gantt_chart(algorithm_name, processes_list, processes_scheduled_list):
    fig, gnt = plt.subplots()
    gnt.set_title(str(algorithm_name))

    y_lim = 15 + 10 * len(processes_list)
    gnt.set_ylim(0, y_lim + 5)
    x_lim = sum(list(map(lambda p: p['burst_time'], processes_list)))
    gnt.set_xlim(0, x_lim + 5)

    gnt.set_xlabel('burst cycles')
    gnt.set_ylabel('process')

    y_labels = list(map(lambda p: p['name'], processes_scheduled_list))
    y_labels.reverse()
    ytick = 15
    y_ticks = []
    for _ in y_labels:
        y_ticks.append(ytick)
        ytick += 10

    gnt.set_yticks(y_ticks)
    gnt.set_yticklabels(y_labels)

    gnt.tick_params(axis="x", labelsize=6)

    loc = plticker.MultipleLocator(base=2)  # this locator puts ticks at regular intervals
    gnt.xaxis.set_major_locator(loc)

    gnt.grid(True) # Setting graph attribute

    y_pos = 10 * len(processes_list)
    for process_scheduled in processes_scheduled_list:
        process_from_processes_list = next(process for process in processes_list if process['name'] == process_scheduled['name'])
        index = processes_list.index(process_from_processes_list)
        gnt.broken_barh(process_scheduled['coordinates'], (y_pos, 9), facecolors=FACECOLORS[index])
        y_pos -= 10

    file_name = algorithm_name + ".png"
    plt.savefig(RESULTS_DIR + file_name)