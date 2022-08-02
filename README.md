# Exploring a twitter dataset of the 20 most famous twitter users

As a project we wanted to create an ineractive tool to explore a twitter dataset that holds tweets of the 20 most popular twitter users from 2009 to 2017.

Link to the datasaet:
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
- run [main.py](main.py)
- choose one out of six functionalities 
- a new window pops up and now you can enter your preferred input
  - word count: choose a user for whom you want to know the word count for your term of choice, additionally you can interactively play around with the time window of your choice 
  - popularity: choose two users whose popularity which is based on their likes and shares you want to compare
  - filter term: choose a term and you get all the tweets which contain this term
  - filter term user: choose a term and a user and you get all  the tweets of this user that contain this term
  - overview user: choose a user and you get a comprehensive overview of their most used words, their most popular tweet and their latest tweet
  - activity user: choose a user and you get their Twitter activity based on their tweet frequency, additionally you can interactively play around with the time window of your choice 


## Struggles
We struggled to incorporate the interactive parts in our tool.
The spanselector did not work very well with a datetime index but we managed to find a workaround for that problem.
What remains a problem until now is the issue of saving entries from textboxes or the choice made with the radiobuttons in order to be able ot access it later.
This is necessary when working with two sets of radiobuttons because two users can be selected or when the text entered into a textbox is required later on.
The functionalities in the background are working proplerly but can not all be accessed correctly through the interface due to that issue.
Functions where a user and a term or two users have to be selected are therefore not working properly in combiantion with the interface.
Our approach was to save the entries from the textboxes and the user that was chosen first to variables and access them later when calling the function.
Unfortunately we were not able to make that work and could not find another workaround for that issue.


## Authors
[Leonie Grafweg](mailto:lgrafweg@uos.de)<br/>
[Paula Heupel](mailto:pheupel@uos.de)<br/>
