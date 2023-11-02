import pandas as pd
from numpy import dot
from numpy.linalg import norm


class Recommender:
    """
    a class that contains all the algorithms for giving recommendations of films and finding similar users

    Parameters
    ----------
    ratings_df: Dataframe
        a dataframe where the rows are usernames and the columns are films, each cell is a rating from 1 to 10

    Attributes
    ----------
    self.ratings: Dataframe
        a dataframe where the rows are usernames and the columns are films, each cell is a rating from 1 to 10

    self.users: list
        a list of all the users (as strings)

    self.sim_matrix: Dataframe
        a dataframe where both the rows and columns are usernames, each cell is a similarity score between them

    Methods
    -------
    users_by_film()
        returns a list of users who have rated the given film
    """

    def __init__(self, ratings_df):
        self.ratings = ratings_df
        self.users = list(self.ratings.index)

        self.sim_matrix = pd.DataFrame(index=self.users, columns=self.users)
        for index in self.sim_matrix.index:
            for column in self.sim_matrix.columns:
                self.sim_matrix.loc[index, column] = self.calculate_similarity(index, column)

    def users_by_film(self, film):
        """returns a list of users who have rated the given film

        :param film: str, the film in question
        :return: list, users who have rated the given film
        """
        col = self.ratings[film]
        col = col[col.notnull()]
        return list(col.index)

    @staticmethod
    def filter_scores(user1_scores, user2_scores):
        """takes in two lists of ratings, returns the ratings for the films that both users watched

        :param user1_scores: a list of scores given by this user
        :param user2_scores: a list of scores given by this user
        :return: list, scores of mutual films
        """
        user1_new = []
        user2_new = []

        for i in range(len(user1_scores)):
            if not pd.isna(user1_scores[i]) and not pd.isna(user2_scores[i]):
                user1_new.append(user1_scores[i])
                user2_new.append(user2_scores[i])

        return user1_new, user2_new

    def calculate_similarity(self, user1, user2):
        a = self.ratings.loc[user1].tolist()
        b = self.ratings.loc[user2].tolist()
        a, b = self.filter_scores(a, b)
        return dot(a, b) / (norm(a) * norm(b))

    def get_most_similar_user(self, user, other_users=None):
        col = self.sim_matrix[user]

        if other_users is None:
            col = col.drop(user)
        else:
            if user in other_users:
                col = col.drop(user)

            col = col[other_users]

        return col.idxmax()

    def predict_score(self, user, film):
        if not pd.isna(self.ratings.loc[user, film]):
            return self.ratings.loc[user, film]

        # get only the users who watched the movie
        other_users = self.users_by_film(film)

        # find the most similar user to our user, out of them
        most_similar = self.get_most_similar_user(user, other_users)

        # return the same rating that the similar user gave
        return self.ratings.loc[most_similar, film] * self.sim_matrix.loc[user, most_similar]

    def recommend_film(self, user):
        # get all the films that this user has not watched
        user_scores = self.ratings.loc[user]
        unrated_films = user_scores.index[user_scores.isna()].tolist()

        # predict a score for each one
        d = {}
        for film in unrated_films:
            d[self.predict_score(user, film)] = film

        # return the film with the highest predicted score
        return d[max(d)]
