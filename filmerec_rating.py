import pandas as pd
import numpy as np
from filmrec_constants import CSV_PATH


def get_rating_data():
    return pd.read_csv(CSV_PATH, index_col='Username')


def update_rating_data(ratings_df):
    ratings_df.to_csv(CSV_PATH)


def rate_film(username, film, rating, ratings_df):
    ratings_df.loc[username, film] = rating
    update_rating_data(ratings_df)


def add_film(ratings_df, new_film):
    ratings_df[new_film] = np.nan
    update_rating_data(ratings_df)


def remove_film(ratings_df, film):
    ratings_df = ratings_df.drop(columns=[film])
    update_rating_data(ratings_df)

