import pandas as pd
import numpy as np

def load_data_to_df(data_path):
    tweets_df = pd.read_csv(data_path)
    tidy_tweets = tidy_up_data(tweets_df)
    return tidy_tweets

def tidy_up_data(df):
    clean_df = df.dropna(how = "any", axis = 1)
    clean_df = clean_df.drop(["language", "id"], axis = 1)
    return clean_df


if __name__ == "__main__":
    print(load_data_to_df("data/tweets.csv"))