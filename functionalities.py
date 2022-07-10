import pandas as pd
from load_data import *

tweets = load_data_to_df("data/tweets.csv")

def word_count(user, term):
    '''
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
    '''
    pass

def filter_term(term):
    '''
    '''
    pass

def filter_term_user(user, term):
    '''
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    result = tweets_of_user[tweets['content'].str.contains(term)]
    return result['content']

def overview_user(user):
    '''
    '''
    pass

def activity_user(user):
    '''
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    tweets_of_user = tweets_of_user.assign(activity = 1)
    return tweets_of_user[['date_time', 'activity']]

if __name__ == "__main__":
    print(word_count('ddlovato', 'back'))