import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import os

current_path_str = os.path.dirname(__file__)
SAVE_DIR = os.path.dirname(current_path_str)
RESULTS_DIR = os.path.join(SAVE_DIR, 'outputs/cpu_scheduling/')
if not os.path.isdir(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)



def plot_gantt_chart(processes_list, processes_scheduled_list):
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()

    # Axis limits
    y_lim = 15 + 10 * len(processes_list)
    gnt.set_ylim(0, y_lim + 5)
    x_lim = sum(list(map(lambda p: p['burst_time'], processes_list)))
    gnt.set_xlim(0, x_lim + 5)

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('burst cycles')
    gnt.set_ylabel('process')

    # Y-axis ticks and labels
    y_labels = list(map(lambda p: p['name'], processes_scheduled_list))
    y_labels.reverse()
    ytick = 15
    y_ticks = []
    for _ in y_labels:
        y_ticks.append(ytick)
        ytick += 10

    gnt.set_yticks(y_ticks)
    gnt.set_yticklabels(y_labels)


    loc = plticker.MultipleLocator(base=2)  # this locator puts ticks at regular intervals
    gnt.xaxis.set_major_locator(loc)

    # Setting graph attribute
    gnt.grid(True)

    # Declaring a bar in schedule
    gnt.broken_barh([(0, 24)], (30, 9), facecolors=('tab:blue'))

    # Declaring multiple bars in at same level and same width
    gnt.broken_barh([(24, 3)], (20, 9),
                    facecolors='tab:orange')

    gnt.broken_barh([(27, 3)], (10, 9),
                    facecolors=('tab:red'))

    # plt.savefig("output/cpu_scheduling/fcfs.png")

    file_name = "fcfs.png"
    plt.savefig(RESULTS_DIR + file_name)