from sklearn.base import BaseEstimator, TransformerMixin
from fancyimpute import KNN


class KNNImpute(BaseEstimator, TransformerMixin):
    """ Impute missing column values using KNN """
    def __init__(self, k):
        self.k = k

    def fit(self, x, y=None):
        x = KNN(k=self.k).complete(x)
        return self

    def transform(self, x):
        return KNN(k=self.k).complete(x)
