import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa import stattools as stt

class ServiceStatisticTools():
    def __init__(self,
                 data: pd.Dataframe = None,
                 testnames = None,
                 xcol: str = None,
                 ycol: str = None):

        if testnames is None:
            testnames = ['ACF', 'ADF']
        self.data = data
        self.testnames = testnames
        self.xcol = xcol
        self.ycol = ycol

        @staticmethod
        def run_acf(data):
            print('calculating the Auto-Correlation-Function of the given data...')
            _acf, _confint, _lb_qstat, _lb_pvalues = stt.acf(x=data, qstat=True, alpha=0.01)
            _res = {'ACF': _acf,
                    'QUANTILE': _confint,
                    'LB_QSTAT': _lb_qstat,
                    'LB_PVALUES': _lb_pvalues}
            return _res

        @staticmethod
        def run_adf(data):
            print('calculating the Augment-Diggy-Fuller Test of the given data...')
            _adf, _pvalue, _nlags, _nobs, _cvalues, _icbest = stt.adfuller(x=data, regression='c', autolag='AIC')
            _res = {'ADF': _adf,
                    'PVALUE': _pvalue,
                    'LAGS': _nlags,
                    'NOBS': _nobs,
                    'CRITICAL_VALUES': _cvalues,
                    'MAXIMIZED_INFORMATION_CRITERION': _icbest}
            return _res

        def run(self):
            print('I am supposed to take in data and run the following statistic tests {} on it!'.format(self.testnames))
            # Load Data
            _df = self.data.loc[::,[self.xcol, self.ycol]].copy()

            if 'ACF' in self.testnames:
                _res_acf = self.run_acf(data=_df[self.ycol])
                print(_res_acf)
            if 'ADF' in self.testnames:
                _res_adf = self.run_adf(data=_df[self.ycol])
                print(_res_adf)

            print('done!')