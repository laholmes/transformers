from sklearn.base import BaseEstimator, TransformerMixin


class StripCurrency(BaseEstimator, TransformerMixin):
    """ Remove currency symbol (and any other characters) from monetary amount """

    def fit(self, x, y=None):
        x = float(x.sub(r'[^0-9' + '.' + r']+', '', str(param[2])))
        return self

    def transform(self, x):
        return float(x.sub(r'[^0-9' + '.' + r']+', '', str(param[2])))
