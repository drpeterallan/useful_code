import matplotlib as mpl
import matplotlib.pyplot as plt
from numpy import arange


def set_rc_params():

    mpl.rcParams.update({"font.size": 14,
                         "font.family": "sans-serif",
                         "lines.linewidth": 2,
                         "xtick.labelsize": 14,
                         "xtick.major.size": 5,
                         "xtick.major.width": 1,
                         "xtick.major.pad": 10,
                         "ytick.labelsize": 14,
                         "ytick.major.size": 5,
                         "ytick.major.width": 1
                         })


if __name__ == "__main__":

    # Set rc params
    set_rc_params()

    # Plot some data to demo changed rcParams
    x = arange(0, 10)
    y = x * x
    plt.plot(x, y)
    plt.show()