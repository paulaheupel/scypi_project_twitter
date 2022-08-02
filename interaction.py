from load_data import *
from functionalities import *
from main_input_output import *
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

chosen = ''
text = ''

def safe(choice):
    chosen = choice

def click_word_count(val):

    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0, 0.4, 0.5])
    radio = RadioButtons(rax, ('katyperry',
                    'justinbieber',
                    'tylorswift13',
                    'BarackObama',
                    'rihanna',
                    'YouTube',
                    'ladygaga',
                    'TheEllenShow',
                    'Twitter',
                    'jtimberlake',
                    'KimKardashian',
                    'britneyspears',
                    'Cristiano',
                    'selenagomez',
                    'cnnbrk',
                    'jimmyfallon',
                    'ArianaGrande',
                    'shakira',
                    'instagram',
                    'ddlovato'))

    def user(choice):
        safe(choice)

    radio.on_clicked(user)

    def submit(text):
        display_word_count(chosen, text)

    axbox = plt.axes([0.1, 0.9, 0.8, 0.075])
    text_box = TextBox(axbox, 'Term', initial = 'Enter term here')
    text_box.on_submit(submit)

    plt.show()

def click_popularity(val):
    fig = plt.figure(figsize=(9,7))
    rax = plt.axes([0.01, 0.4, 0.4, 0.5])
    radio1 = RadioButtons(rax, ('katyperry',
                    'justinbieber',
                    'tylorswift13',
                    'BarackObama',
                    'rihanna',
                    'YouTube',
                    'ladygaga',
                    'TheEllenShow',
                    'Twitter',
                    'jtimberlake',
                    'KimKardashian',
                    'britneyspears',
                    'Cristiano',
                    'selenagomez',
                    'cnnbrk',
                    'jimmyfallon',
                    'ArianaGrande',
                    'shakira',
                    'instagram',
                    'ddlovato'))

    def user1(choice):
        safe(choice)

    radio1.on_clicked(user1)

    rax = plt.axes([0.5, 0.4, 0.4, 0.5])
    radio2 = RadioButtons(rax, ('katyperry',
                    'justinbieber',
                    'tylorswift13',
                    'BarackObama',
                    'rihanna',
                    'YouTube',
                    'ladygaga',
                    'TheEllenShow',
                    'Twitter',
                    'jtimberlake',
                    'KimKardashian',
                    'britneyspears',
                    'Cristiano',
                    'selenagomez',
                    'cnnbrk',
                    'jimmyfallon',
                    'ArianaGrande',
                    'shakira',
                    'instagram',
                    'ddlovato'))

    def user2(choice):
        display_popularity(chosen, choice)
    radio2.on_clicked(user2)
    plt.show()

def click_filter_term(val):
    fig = plt.figure(figsize=(9,7))

    def submit(text):
        display_filter_term(text)

    axbox = plt.axes([0.1, 0.9, 0.8, 0.075])
    text_box = TextBox(axbox, 'Term')
    text_box.on_submit(submit)
    plt.show()

def click_filter_term_user(val):
    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0, 0.4, 0.5])
    radio = RadioButtons(rax, ('katyperry',
                    'justinbieber',
                    'tylorswift13',
                    'BarackObama',
                    'rihanna',
                    'YouTube',
                    'ladygaga',
                    'TheEllenShow',
                    'Twitter',
                    'jtimberlake',
                    'KimKardashian',
                    'britneyspears',
                    'Cristiano',
                    'selenagomez',
                    'cnnbrk',
                    'jimmyfallon',
                    'ArianaGrande',
                    'shakira',
                    'instagram',
                    'ddlovato'))

    def user(choice):
        result = word_count(choice,'')
        x = result['date_time']
        y = result['word_occurence']
        ax1.plot(x, y) 

    radio.on_clicked(user)

    def submit(text):
        result = word_count('',text)
        x = result['date_time']
        y = result['word_occurence']
        ax1.plot(x, y) 

    axbox = plt.axes([0.1, 0.9, 0.8, 0.075])
    text_box = TextBox(axbox, 'Term')
    text_box.on_submit(submit)

    plt.show()

def click_overview_user(val):
    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0.4, 0.4, 0.5])
    radio = RadioButtons(rax, ('katyperry',
                    'justinbieber',
                    'tylorswift13',
                    'BarackObama',
                    'rihanna',
                    'YouTube',
                    'ladygaga',
                    'TheEllenShow',
                    'Twitter',
                    'jtimberlake',
                    'KimKardashian',
                    'britneyspears',
                    'Cristiano',
                    'selenagomez',
                    'cnnbrk',
                    'jimmyfallon',
                    'ArianaGrande',
                    'shakira',
                    'instagram',
                    'ddlovato'))

    def user(choice):
        display_overview_user(choice)

    radio.on_clicked(user)
    plt.show()

def click_activity_user(val):
    fig = plt.figure(figsize=(9,7))

    rax = plt.axes([0.1, 0.4, 0.4, 0.5])
    radio = RadioButtons(rax, ('katyperry',
                    'justinbieber',
                    'tylorswift13',
                    'BarackObama',
                    'rihanna',
                    'YouTube',
                    'ladygaga',
                    'TheEllenShow',
                    'Twitter',
                    'jtimberlake',
                    'KimKardashian',
                    'britneyspears',
                    'Cristiano',
                    'selenagomez',
                    'cnnbrk',
                    'jimmyfallon',
                    'ArianaGrande',
                    'shakira',
                    'instagram',
                    'ddlovato'))

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