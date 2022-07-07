import pandas as pd

def load_data_to_df(data_path):
    tweets_df = pd.read_csv(data_path)
    return tweets_df

#def tidy_up_data(df):


if __name__ == "__main__":
    print(load_data_to_df("data/tweets.csv"))