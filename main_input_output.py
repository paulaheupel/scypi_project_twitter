import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from pandas import Timestamp
from functionalities import *
import matplotlib.dates as dates

df = word_count('instagram', 'a')

fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))

x = df.index
y = df['word_occurence']

ax1.plot(x, y)
ax1.set_title('Press mouse button and drag to select a region in the top graph')

line2, = ax2.plot([], [])


def onselect(xmin, xmax):
    indmin, indmax = np.searchsorted(dates.date2num(x), (xmin, xmax))
    indmax = min(len(x) - 1, indmax)

    region_x = x[indmin:indmax]
    region_y = y[indmin:indmax]

    line2.set_data(region_x, region_y)
    ax2.set_xlim(region_x[0], region_x[-1])
    ax2.set_ylim(region_y.min(), region_y.max())
    fig.canvas.draw_idle()

span = SpanSelector(
    ax1,
    onselect,
    "horizontal",
    useblit=True,
    props=dict(alpha=0.5, facecolor="tab:blue"),
    interactive=True,
    drag_from_anywhere=True
)

plt.show()