from sklearn.base import BaseEstimator, TransformerMixin


class ToBaseTen(BaseEstimator, TransformerMixin):
    """ Convert number expressed in any base to base 10 """
    def __init__(self):
        pass

    def fit(self, x, y=None):
    #    TODO
        return self

    def transform(self, x):
        return #TODO
