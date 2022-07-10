import pandas as pd

def load_data_to_df(data_path, cols_delete = []):
    '''
    expects a path to the data as a parameter and returns a dataframe of the given data
    expects a list of column-names that should be deleted to give to tidy_up_data as second parameter
    also calls tidy_up_data on the dataframe before returning it
    '''
    tweets_df = pd.read_csv(data_path)
    tidy_tweets = tidy_up_data(tweets_df, cols_delete)
    return tidy_tweets

def tidy_up_data(df, cols_delete = []):
    '''
    expects a dataframe
    optional parameter: a list of column-names that are not needed
    deletes NaN-columns
    also deletes specified columns that are not needed
    '''
    clean_df = df.dropna(how = "any", axis = 1)
    clean_df = clean_df.drop(cols_delete, axis = 1)
    return clean_df

if __name__ == "__main__":
    print(load_data_to_df("data/tweets.csv"), ["language", "id"])