from sklearn.base import BaseEstimator, TransformerMixin


class MToKM(BaseEstimator, TransformerMixin):
    """ Convert distance in Miles to Kilometres """
    def __init__(self):
        pass

    def fit(self, x, y=None):
        x = x*1.609344
        return self

    def transform(self, x):
        return x*1.609344
