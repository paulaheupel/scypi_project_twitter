import pandas as pd
from load_data import *
from collections import Counter

tweets = load_data_to_df("data/tweets.csv", ["language", "id"])

def word_count(user, term):
    '''
    expects a user (string) and a term (string) as parameters
    returns a dataframe containing the amount of the words for each tweet (and the date time for them)
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    tweets_of_user = pd.DataFrame(tweets_of_user)
    result = tweets_of_user.assign(word_occurence = 0)
    for index in result.index:
        words = result['content'][index].split()
        term_occurence = words.count(term)
        result['word_occurence'][index] = term_occurence
    result = result.groupby(result['date_time'].dt.date).sum('word_occurence')
    return result[['word_occurence']]

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
    popularity_u1 = popularity_u1.groupby(popularity_u1['date_time'].dt.date).agg({'number_of_likes' : sum, 'number_of_shares' : sum})
    popularity_u2 = popularity_u2.groupby(popularity_u2['date_time'].dt.date).agg({'number_of_likes' : sum, 'number_of_shares' : sum})
    result = [popularity_u1, popularity_u2]
    return result

def filter_term(term):
    '''
    expects a term (string) as parameter
    returns all the tweets containing the term
    '''
    result = tweets[tweets['content'].str.contains(term)]
    return result['content']

def filter_term_user(term, user):
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
    returns an overview of the user including most used words, most popular tweet and 3 latest tweets
    as a list [[list of most used words], most popular tweet, latest tweet]
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    tweets_of_user['date_time'] = pd.to_datetime(tweets_of_user['date_time'])
    most_used_words = Counter(" ".join(tweets_of_user['content']).split()).most_common(10)
    most_popular_tweet = tweets_of_user.loc[tweets_of_user['number_of_likes'].idxmax()]['content']
    latest_tweet = tweets_of_user.iloc[tweets_of_user['date_time'].argmax()]['content']
    result = [most_used_words, most_popular_tweet, latest_tweet]
    return result

def activity_user(user):
    '''
    expects a user as parameter (string)
    returns the activity of the given user over time (tweet frequency over time)
    '''
    tweets_of_user = tweets[tweets['author'] == user]
    tweets_of_user = pd.DataFrame(tweets_of_user)
    result = tweets_of_user.assign(activity = 1)
    result = result.groupby(result['date_time'].dt.date).sum('activity')
    return result[['activity']]

if __name__ == "__main__":
    print(filter_term('shadow'))