import pandas as pd
from load_data import *

tweets = load_data_to_df("data/tweets.csv")

def word_count(user, term):
    '''
    expects a user (string) and a term (string) as parameters
    returns a dataframe containing the amount of the words for each tweet (and the date time for them)
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    result = tweets_of_user.assign(word_occurence = 0)
    for index in result.index:
        words = result['content'][index].split()
        term_occurence = words.count(term)
        result['word_occurence'][index] = term_occurence
    return result[['date_time', 'word_occurence']]

def popularity(user1, user2):
    '''
    expects two users (strings) as parameters
    reurns popularity of the two users over time (to be plotted)
    as a list with the dataframes with likes and shares of both users
    ([ dataframe_user1 ,dataframe_user2])
    dataframe contains: 'author', 'number_of_likes', 'number_of_shares', 'date_time'
    '''
    popularity_u1 = tweets[tweets['author'] == user1][['author', 'number_of_likes', 'number_of_shares', 'date_time']]
    popularity_u2 = tweets[tweets['author'] == user2][['author', 'number_of_likes', 'number_of_shares', 'date_time']]
    result = [popularity_u1, popularity_u2]
    return result

def filter_term(term):
    '''
    expects a term (string) as parameter
    returns all the tweets containing the term
    '''
    result = tweets[tweets['content'].str.contains(term)]
    return result['content']

def filter_term_user(user, term):
    '''
    expects a user (string) and a term (string) as parameter
    returns all the tweets of the given user containing the term
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    result = tweets_of_user[tweets_of_user['content'].str.contains(term)]
    return result['content']

def overview_user(user):
    '''
    expects a user as parameter (string)
    returns an overview of the user including most used words, most popular post, latest post and post frequency
    '''
    pass

def activity_user(user):
    '''
    expects a user as parameter (string)
    returns the activity of the given user over time (tweet frequency over time)
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    tweets_of_user = tweets_of_user.assign(activity = 1)
    return tweets_of_user[['date_time', 'activity']]

if __name__ == "__main__":
    print(word_count('ddlovato', 'back'))