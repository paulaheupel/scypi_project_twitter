from load_data import *
from functionalities import *
from display_functions import *
from matplotlib import pyplot as plt

from matplotlib.widgets import RadioButtons
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button


axes1 = plt.axes([0.4, 0.7, 0.2, 0.075])
axes2 = plt.axes([0.4, 0.6, 0.2, 0.075])
axes3 = plt.axes([0.4, 0.5, 0.2, 0.075])
axes4 = plt.axes([0.4, 0.4, 0.2, 0.075])
axes5 = plt.axes([0.4, 0.3, 0.2, 0.075])
axes6 = plt.axes([0.4, 0.2, 0.2, 0.075])

word_count_button= Button(axes1,'word count')
popularity_button = Button(axes2,'popularity')
filter_term_button = Button(axes3,'filter term')
filter_term_user_button = Button(axes4,'filter term user')
overview_user_button = Button(axes5,'overview user')
activity_user_button = Button(axes6,'activity user')

users = ('katyperry', 'justinbieber', 'tylorswift13', 'BarackObama', 'rihanna', 'YouTube','ladygaga', 'TheEllenShow',
        'Twitter', 'jtimberlake', 'KimKardashian', 'britneyspears', 'Cristiano', 'selenagomez', 'cnnbrk', 'jimmyfallon',
        'ArianaGrande', 'shakira', 'instagram', 'ddlovato')
chosen = ''
entered_text = ''

def click_word_count(val):
    '''
    When the word count is clicked a new window pops up with a radio button for the user choice and a text box for entering a term
    The selected user and the entered term are passed on to the display_word_count function
    '''

    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0.3, 0.4, 0.5])
    radio = RadioButtons(rax, users)

    def user(choice):
        display_word_count(choice, entered_text)

    radio.on_clicked(user)

    def submit(text):
        global entered_text
        entered_text = text

    axbox = plt.axes([0.1, 0.9, 0.8, 0.075])
    text_box = TextBox(axbox, 'Term')
    text_box.on_submit(submit)

    plt.show()

def click_popularity(val):
    '''
    When the popularity is clicked a new window pops up with two radio buttons for the user choice
    The selected users are passed on to the display_popularity function
    '''
    fig = plt.figure(figsize=(9,7))
    rax = plt.axes([0.01, 0.4, 0.4, 0.5])

    radio1 = RadioButtons(rax, users)

    def user1(choice):
        global chosen
        chosen = choice

    radio1.on_clicked(user1)

    rax = plt.axes([0.5, 0.4, 0.4, 0.5])
    radio2 = RadioButtons(rax, users)

    def user2(choice):
        display_popularity(chosen, choice)
    radio2.on_clicked(user2)
    plt.show()

def click_filter_term(val):
    '''
    When the filter term is clicked a new window pops up with a text box for entering a term
    The entered term is passed on to the display_filter_term function
    '''
    fig = plt.figure(figsize=(9,7))

    def submit(text):
        display_filter_term(text)

    axbox = plt.axes([0.1, 0.9, 0.8, 0.075])
    text_box = TextBox(axbox, 'Term')
    text_box.on_submit(submit)
    plt.show()

def click_filter_term_user(val):
    '''
    When the filter term user is clicked a new window pops up with a radio button for the user choice and a text box for entering a term
    The entered term is passed on to the display_filter_term function
    '''
    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0.3, 0.4, 0.5])
    radio = RadioButtons(rax, users)

    def user(choice):
        display_filter_term_user(entered_text, choice)

    radio.on_clicked(user)

    def submit(text):
        global entered_text
        entered_text = text

    axbox = plt.axes([0.1, 0.9, 0.8, 0.075])
    text_box = TextBox(axbox, 'Term')
    text_box.on_submit(submit)

    plt.show()

def click_overview_user(val):
    '''
    When the overview user is clicked a new window pops up with a radio button for the user choice
    The selected user is passed on to the display_overview_user function
    '''
    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0.4, 0.4, 0.5])
    radio = RadioButtons(rax, users)

    def user(choice):
        display_overview_user(choice)

    radio.on_clicked(user)
    plt.show()

def click_activity_user(val):
    '''
    When the activity user is clicked a new window pops up with a radio button for the user choice
    The selected user is passed on to the display_activity_user function
    '''
    
    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0.4, 0.4, 0.5])
    radio = RadioButtons(rax, users)

    def user(choice):
        display_activity_user(choice)

    radio.on_clicked(user)
    plt.show()

word_count_button.on_clicked(click_word_count)
popularity_button.on_clicked(click_popularity)
filter_term_button.on_clicked(click_filter_term)
filter_term_user_button.on_clicked(click_filter_term_user)
overview_user_button.on_clicked(click_overview_user)
activity_user_button.on_clicked(click_activity_user)

plt.show()