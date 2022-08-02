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


## Struggles
We struggled to incorporate the interactive parts in our tool.
The spanselector did not work very well with a datetime index but we managed to find a workaround for that problem.
What remains a problem until now is the issue of saving entries from textboxes or the choice made with the radiobuttons in order to be able ot access it later. This is necessary when working with to sets of radiobuttons because two users can be selected.


## Authors
[Leonie Grafweg](mailto:lgrafweg@uos.de)<br/>
[Paula Heupel](mailto:pheupel@uos.de)<br/>
