from sklearn.base import BaseEstimator, TransformerMixin


class Clip(BaseEstimator, TransformerMixin):
    """ Select only first n characters of string column """
    def __init__(self, n):
        self.n = n

    def fit(self, x, y=None):
        x = x[0:self.n]
        return self

    def transform(self, x):
        return x[0:self.n]
