import tkinter as tk
import numpy as np

# pts_freq = 1000
# freq = np.linspace(0.1e9,10e9,pts_freq)


def get_network(plot_sets, structures):
    n = len(plot_sets)
    if n == 0:
        return
    if str(type(structures[plot_sets[0]])) != "<class 'skmd.network.Network'>":
        NETWORK = structures[plot_sets[0]].NW
    else:
        NETWORK = structures[plot_sets[0]]
    x = range(1, n, 1)
    for i in x:
        if str(type(structures[plot_sets[i]])) != "<class 'skmd.network.Network'>":
            NETWORK = NETWORK * structures[plot_sets[i]].NW
        else:
            NETWORK = NETWORK * structures[plot_sets[i]]
    return NETWORK