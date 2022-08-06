# Exploring a twitter dataset of the 20 most popular twitter users

As a project we wanted to create an ineractive tool to explore a twitter dataset that holds tweets of the 20 most popular twitter users from 2009 to 2017.

Link to the dataset:
https://www.kaggle.com/datasets/mmmarchetti/tweets-dataset

## Structure

| Input  | Function | Output |
| ------------- | ------------- | ------------- |
| User, Term, Time Interval  | Word frequency of a specific user over a specified time  | Plot of the frequency in interval  |
| 2 Users  | Wompare the popularity of two users (likes and shares)in a specified time window  | Plot of the comparison  |
| Term  | Filter for a specified term  | All tweets containing the term  |
| Term, User  | Filter for a specified term among tweets of the user  | All tweets of the specified user containing the term  |
| User  | Overview: most used words, most popular post, latest post  | Overview of the user’s content  |
| User, Time Interval | Activity of the user in a time interval  | Plot of the activity  |

Used libraries: Numpy, Pandas, Matplotlib

## Usage
- install numpy, pandas and matplolib (via pip install)
- run [main.py](main.py)
- choose one out of six functionalities 
- a new window pops up and now you can enter your preferred input
  - word count: choose a term (first) and a user (second) for whom you want to know the word count for your term of choice, additionally you can interactively play around with the time window of your choice 
  - popularity: choose two users whose popularity which is based on their likes and shares you want to compare
  - filter term: choose a term and you get all the tweets which contain this term
  - filter term user: choose a term (first) and a user (second) and you get all  the tweets of this user that contain this term
  - overview user: choose a user and you get a comprehensive overview of their most used words, their most popular tweet and their latest tweet
  - activity user: choose a user and you get their Twitter activity based on their tweet frequency, additionally you can interactively play around with the time window of your choice 


## Struggles
We struggled a little to incorporate the interactive parts in our tool.
The spanselector did not work very well with a datetime index but we managed to find a workaround for that problem.
Another problem we faced was the issue of saving entries from textboxes or the choice made with the radiobuttons in order to be able ot access it later.
This is necessary when working with two sets of radiobuttons because two users can be selected or when the text entered into a textbox is required later on.
We managed to solve this problem by using global variables (or a global scope) after recieving this hint from one of the tutors. :)

Another thing that made our work a little more difficult is that the textboxes and radiobuttons are not alwayys visualized or working the way one would expect them to.
For example when one of us types something in a textbox, the text doesn't show, although entering the text afterwards does work and also calls the expected function and provides the expected output.
For the other one of us, the written text is visible, but the entering doesn't work and the attached function is not being called.
This confused us, especially because we are working with the same code and also have similar computers.
The radiobuttons and spanselectors also only work properly at one of our computers.
This made working remotely extremely difficult.


## Authors
[Leonie Grafweg](mailto:lgrafweg@uos.de)<br/>
[Paula Heupel](mailto:pheupel@uos.de)<br/>
