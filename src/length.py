from sklearn.base import BaseEstimator, TransformerMixin


class Length(BaseEstimator, TransformerMixin):
    """ Convert string column to length of value """
    def __init__(self):
        pass

    def fit(self, x, y=None):
    #    TODO
        return self

    def transform(self, x):
        return #TODO
