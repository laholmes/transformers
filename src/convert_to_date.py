from sklearn.base import BaseEstimator, TransformerMixin


class ConvertToDate(BaseEstimator, TransformerMixin):
    """ Convert string column to datetime """
    def __init__(self):
        pass

    def fit(self, x, y=None):
    #    TODO
        return self

    def transform(self, x):
        return #TODO
