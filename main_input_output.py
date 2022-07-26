import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from pandas import Timestamp
from functionalities import *
import matplotlib.dates as dates

def display_word_count(user, term):
    df = word_count(user, term)

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

def display_popularity(user1, user2):
    result = popularity(user1, user2)
    df_u1 = result[0]
    df_u2 = result[1]

    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))

    ax1.plot(df_u1.index, df_u1['number_of_likes'])
    ax1.plot(df_u2.index, df_u2['number_of_likes'])
    ax1.set_title('Recieved likes of both users')
    ax2.plot(df_u1.index, df_u1['number_of_shares'])
    ax2.plot(df_u2.index, df_u2['number_of_shares'])
    ax2.set_title('Recieved shares of both users')
    plt.tight_layout()
    plt.show()

def display_filter_term(term):
    pass

def display_filter_term_user(term, user):
    pass

def display_overview_user(user):
    pass

def display_activity_user(user):
    df = activity_user(user)
    fig, ax = plt.subplots(1, figsize=(8, 4))
    ax.plot(df['date_time'], df['activity'])
    plt.tight_layout()
    plt.show()

#display_activity_user('ddlovato')