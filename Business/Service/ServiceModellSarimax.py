import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

class ServiceModellSarimax():
    def __init__(self,
                 modelname: str = 'Sarimax',
                 data: pd.DataFrame = None,
                 order: tuple = (1, 0, 0),
                 seasonal_order: tuple = (1, 1, 1, 23),
                 quantile: float = 0.99,
                 xcol: str = None,
                 ycol: str = None,
                 show_plot: bool = False):

        self.modelname = modelname
        self.data = data
        self.order = order
        self.seasonal_order = seasonal_order
        self.quantile = quantile
        self.xcol = xcol
        self.ycol = ycol
        self.show_plot = show_plot



    def run(self):
        print('i am supposed to take in data and model a {} of order {} and give out a plot!'.format(self.modelname,self.order))

        #Load Data
        _df = self.data.loc[::, [self.xcol, self.ycol]].copy()

        #Define Model
        _order = self.order
        _seasonal_order = self.seasonal_order
        _model = SARIMAX(_df[self.ycol], order=_order, seasonal_order=_seasonal_order)

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

        # prepare index
        df2 = _df
        df2.index = pd.to_datetime(df2[self.xcol])
        series = df2.index
        series_predict = pd.date_range(start=df2.index[-1], periods=100, freq='B')
        series = series.append(series_predict)

        # one common dataframe for fistorical data, prediction mean and prediction quantile
        _results = pd.DataFrame(pd.concat([_df[self.ycol], _fcst_maen, _fcst_qntl.iloc[::, 0], _fcst_qntl.iloc[::, 1]],
                                          axis=1))
        _results = _results.rename(columns={'Amount_EUR': 'Historie', 'predicted_mean': 'Mittelwert',
                                            'lower Amount_EUR': '{}-Quantil lower'.format(self.quantile),
                                            'upper Amount_EUR': '{}-Quantil upper'.format(self.quantile)})

        _results[self.xcol] = series



        #Plot
        if self.show_plot:
            fig, ax = plt.subplots()
            ax.plot(_df[self.ycol], color='black', label='Historie', zorder=2)
            ax.plot(_fcst_maen, color='blue', label='Erwartungswert', zorder=2)
            ax.plot(_fcst_qntl.iloc[::, 0], color='cyan', label='{}-Quantil'.format(self.quantile), zorder=1)
            ax.plot(_fcst_qntl.iloc[::, 1], color='cyan', label='', zorder=1)
            ax.fill_between(x=_fcst_qntl.index,
                            y1=_fcst_qntl.iloc[::, 0],
                            y2=_fcst_qntl.iloc[::, 1],
                            alpha=0.5, zorder=0)

            plt.legend()
            plt.show()

        return _fit, _forecast, _results
        print('done')