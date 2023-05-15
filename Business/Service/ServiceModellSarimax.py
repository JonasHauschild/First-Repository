import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

class ServiceModellSarimax():
    def __init__(self,
                 modelname: str = 'Sarimax',
                 data: pd.DataFrame = None,
                 order: tuple = (1,0,0),
                 seasonal_order: tuple = (1,1,1,23),
                 quantile: float = 0.99,
                 xcol: str = None,
                 ycol: str = None):

        self.modelname = modelname
        self.data = data
        self.order = order
        self.seasonal_order = seasonal_order
        self.quantile = quantile
        self.xcol = xcol
        self.ycol = ycol

    def run(self):
        print('i am supposed to take in data and model a {} of order {} and give out a plot!'.format(self.modelname,self.order))

        #Load Data
        _df = self.data.loc[::, [self.xcol, self.ycol]].copy()

        #Define Model
        _order = self.order
        _seasonal_order = self.seasonal_order
        _model = SARIMAX(_df[self.ycol], order= _order, seasonal_order=_seasonal_order)

        #Fit the Model
        _fit = _model.fit()
        _summary = _fit.summary()

        #Gefittete Zeitreihe
        _fitted_timeseries = _fit.predict()
        _fitted_timeseries = _fitted_timeseries.iloc[1:0]

        # Forecast mit Saison
        _forecast = _fit.get_forecast(steps=100, signal_only=False)
        _fcst_maen = _forecast.predicted_mean
        _alpha = 1-self.quantile
        _fcst_qntl = _forecast.conf_int(alpha=_alpha)


        #Plot
        fig, ax = plt.subplots()
        ax.plot(_df[self.ycol], color='black', label='Historie', zorder=2)
        ax.plot(_fcst_maen, color='blue', label='Erwartungswert', zorder=2)
        ax.plot(_fcst_qntl.iloc[::,0], color='cyan', label='{}-Quantil'.format(self.quantile), zorder=1)
        ax.plot(_fcst_qntl.iloc[::,1], color='cyan', label='', zorder=1)
        ax.fill_between(x=_fcst_qntl.index,
                        y1=_fcst_qntl.iloc[::,0],
                        y2=_fcst_qntl.iloc[::,1],
                        alpha=0.5, zorder=0)

        plt.legend()
        plt.show()

        print('done')