import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
from pandas import Timestamp
from functionalities import *
import matplotlib.dates as dates
import matplotlib.patheffects as path_effects

def display_word_count(user, term):
    '''
    expects as input two strings, one for the user and one for the term
    creates a plot of frequency of use with a spanselector where user can choose a span to take a closer look at
    '''
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
    '''
    expects as input two strings for the two users
    creates two plots comparing the shares and the likes of tweets of both users over time
    '''
    result = popularity(user1, user2)
    df_u1 = result[0]
    df_u2 = result[1]

    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))

    ax1.plot(df_u1.index, df_u1['number_of_likes'], label = user1)
    ax1.plot(df_u2.index, df_u2['number_of_likes'], label = user2)
    ax1.set_title('Recieved likes of both users')
    ax2.plot(df_u1.index, df_u1['number_of_shares'], label = user1)
    ax2.plot(df_u2.index, df_u2['number_of_shares'], label = user2)
    ax2.set_title('Recieved shares of both users')
    plt.legend()
    plt.tight_layout()
    plt.show()

def display_filter_term(term):
    result = filter_term(term)
    result = pd.DataFrame(result)
    display_df(result)

def display_filter_term_user(term, user):
    result = filter_term_user(term,user)
    result = pd.DataFrame(result)
    display_df(result)

def display_df(result):
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(121)
    bbox=[0, 0, 1, 1]
    ax.axis('off')
    mpl_table = ax.table(cellText = result.values, rowLabels = result.index, bbox=bbox, colLabels=result.columns)
    mpl_table.auto_set_font_size(True)
    plt.show()

def display_overview_user(user):
    result = overview_user(user)

    fig = plt.figure(figsize=(12, 6))
    text = fig.text(0.05,0.9, '10 most used words: ', ha='left', va='center', size=15)
    text.set_path_effects([path_effects.Normal()])
    for i in range(10):
        temp_text = fig.text(0.3+i*0.1, 0.9, result[0][i], ha='center', va='center', size=10)
        temp_text.set_path_effects([path_effects.Normal()])
    
    text = fig.text(0.05,0.6, 'Most popular tweet: ', ha='left', va='center', size=15)
    text = fig.text(0.3,0.6, result[1], ha='left', va='center', size=10)
    text = fig.text(0.05,0.3, 'Latest tweet: ', ha='left', va='center', size=15)
    text = fig.text(0.3,0.3, result[2], ha='left', va='center', size=10)

    plt.show()

def display_activity_user(user):

    df = activity_user(user)

    fig, (ax1, ax2) = plt.subplots(2, figsize=(8, 6))

    x = df.index
    y = df['activity']

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
    plt.tight_layout()
    plt.show()

#display_word_count('instagram', 'this')