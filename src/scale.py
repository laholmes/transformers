from sklearn.base import BaseEstimator, TransformerMixin


class Clip(BaseEstimator, TransformerMixin):
    """ Scale input vectors individually to unit norm, using sklearn """
    def __init__(self, norm='l1'):
        self.norm = norm

    def fit(self, x, y=None):
        x = sklearn.preprocessing.normalize(x, self.norm)
        return self

    def transform(self, x):
        return sklearn.preprocessing.normalize(x, self.norm)
