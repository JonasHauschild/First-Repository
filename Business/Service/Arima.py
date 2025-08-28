import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima.model import ARIMAResults
from statsmodels.graphics.tsaplots import plot_predict
from statsmodels.tsa.stattools import acf
import matplotlib.pyplot as plt
from numpy import log

df = pd.read_csv(r'C:\Users\jonas.hauschild\PycharmProjects\First-Repository-2\Business\Test-Data\data.csv')

print(df.head())
plt.show()
#First, I will check if the series is stationary using the Augmented Dickey Fuller test (ADF Test), from the statsmodels package.
# The reason being is that we need differencing only if the series is non-stationary. Else, no differencing is needed, that is, d=0.
#The null hypothesis (Ho) of the ADF test is that the time series is non-stationary.
# So, if the p-value of the test is less than the significance level (0.05) then we reject the null hypothesis and infer that the time series is indeed stationary.
#So, in our case, if P Value > 0.05 we go ahead with finding the order of differencing.

# AR = p --> PACF  --> Direct Impact of a past value on the current value -- > First DIfferenzierung
# MA = q --> ACF   --> Moving Average Impact
# Differencing = d for non stationary to stationary time series (using log e. g. or Difference of Xt and Xt-1)
# Differenzierung ist der Prozess, bei dem der aktuelle Wert einer Zeitreihe von ihrem vorherigen Wert oder von einem verzögerten Wert subtrahiert wird.
# Wenn Sie z. B. eine monatliche Zeitreihe von Verkäufen haben, können Sie diese differenzieren, indem Sie die Verkäufe des Vormonats vom aktuellen Monat subtrahieren.
# Dadurch erhalten Sie die Veränderung der Verkäufe von Monat zu Monat, was eine neue Zeitreihe ist.
# Sie können diesen Vorgang wiederholen, um Differenzen höherer Ordnung zu erhalten, z. B. die Änderung der Umsatzänderung usw.
# Die Idee dahinter ist, alle Trends oder Saisonalitäten zu entfernen, die die ursprüngliche Zeitreihe nicht stationär machen.

result = adfuller(df.value.dropna())
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

df_value_diff_1 = df.value.diff().dropna()
result_diff_1 = adfuller(df_value_diff_1)
print('ADF Statistic Dif 1: %f' % result_diff_1[0])
print('p-value Dif 1: %f' % result_diff_1[1])

df_value_diff_2 = df.value.diff().diff().dropna()
result_diff_2 = adfuller(df_value_diff_2)
print('ADF Statistic Dif 2: %f' % result_diff_2[0])
print('p-value Dif 2: %f' % result_diff_2[1])

df_value_diff_3 = df.value.diff().diff().diff().dropna()
result_diff_3 = adfuller(df_value_diff_3)
print('ADF Statistic Dif 3: %f' % result_diff_3[0])
print('p-value Dif 3: %f' % result_diff_3[1])

#Since p-value (1) is greater than the significance level (0.05), let’s difference the series and see how the autocorrelation plot looks like.

plt.rcParams.update({'figure.figsize':(9,7), 'figure.dpi':120})

# Original Series
fig, axes = plt.subplots(3, 2, sharex=True)
axes[0, 0].plot(df.value); axes[0, 0].set_title('Original Series')
plot_acf(df.value, ax=axes[0, 1])

#plt.show()

# 1st Differencing
axes[1, 0].plot(df.value.diff()); axes[1, 0].set_title('1st Order Differencing')
plot_acf(df.value.diff().dropna(), ax=axes[1, 1])

#plt.show()

# 2nd Differencing
axes[2, 0].plot(df.value.diff().diff()); axes[2, 0].set_title('2nd Order Differencing')
plot_acf(df.value.diff().diff().dropna(), ax=axes[2, 1])

#plt.show()

#For the above data, we can see that the time series reaches stationarity with two orders of differencing.

#The next step is to identify if the model needs any AR terms. We will find out the required number of AR terms by inspecting the Partial Autocorrelation (PACF) plot.
#Partial autocorrelation can be imagined as the correlation between the series and its lag, after excluding the contributions from the intermediate lags.
#So, PACF sort of conveys the pure correlation between a lag and the series. This way, we will know if that lag is needed in the AR term or not.
#Now, we should find the number of AR terms. Any autocorrelation in a stationarized series can be rectified by adding enough AR terms.
#So, we initially take the order of AR term to be equal to as many lags that crosses the significance limit in the PACF plot.

#PACF plot of 1st differenced series
plt.rcParams.update({'figure.figsize':(9,3), 'figure.dpi':120})

fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.value.diff()); axes[0].set_title('1st Differencing')
axes[1].set(ylim=(0,5))
plot_pacf(df.value.diff().dropna(), ax=axes[1])

fig, axes = plt.subplots(1, 2, sharex=True)
axes[0].plot(df.value.diff().diff()); axes[0].set_title('2st Differencing')
axes[1].set(ylim=(0,5))
plot_pacf(df.value.diff().diff().dropna(), ax=axes[1])

#plt.show()

# We will try with p = 1 (AR) because the first Value 1 in the PACF Plot is strongly significant and rearrange if neccesary.

#To find the right MA (q) term we will look again on the ACF plot.
#We can see that couple of lags are well above the significance line.
#So, we will fix q as 2. If there is any doubt, we will go with the simpler model that sufficiently explains the Y.

#It may happen that the time series is slightly under differenced. Differencing it one more time makes it slightly over-differenced.
#If the series is slightly under differenced, adding one or more additional AR terms usually makes it up.
#Likewise, if it is slightly over-differenced, we will try adding an additional MA term.

#Now, we have determined the values of p, d and q. We have everything needed to fit the ARIMA model. We will use the ARIMA() implementation in the statsmodels package.

# 1,1,2 ARIMA Model
model = ARIMA(df.value, order=(1,1,2))
model_fit = model.fit()
print(model_fit.summary())

#The model summary provides lot of information. The table in the middle is the coefficients table where the values under ‘coef’ are the weights of the respective terms.

#The coefficient of the MA2 term is close to zero and the P-Value in ‘P>|z|’ column is highly insignificant.
#It should ideally be less than 0.05 for the respective X to be significant.

#So, we will rebuild the model without the MA2 term.

# 1,1,1 ARIMA Model
model = ARIMA(df.value, order=(1,1,1))
model_fit = model.fit()
print('Model_Fit:',model_fit.summary())

#The model AIC has slightly reduced, which is good. The p-values of the AR1 and MA1 terms have improved and are highly significant (<< 0.05).

#Let’s plot the residuals to ensure there are no patterns (that is, look for constant mean and variance).

# Plot residual errors
residuals = pd.DataFrame(model_fit.resid)
print('Residuals Mean: %f' %residuals.mean())
print('Residuals Var: %f' %residuals.var())
fig, ax = plt.subplots(1,2)
residuals.plot(title="Residuals", ax=ax[0])
residuals.plot(kind='kde', title='Density', ax=ax[1])
#plt.show()

#The residual errors seem fine with near zero mean and uniform variance. Let’s plot the actuals against the fitted values using plot_predict().

#Actual vs Fitted
_fitted_timeseries = model_fit.predict()
df2 = _fitted_timeseries.to_frame()
df3 = pd.concat([df, df2], axis=1)
df3.plot(kind='line', x='date', y=['value', 'predicted_mean'])
plt.title('Zeitreihe gegen Modell')
plt.xlabel('Datum')
plt.ylabel('Wert')
plt.legend(['value', 'predicted_mean'])
#plt.show()

#So, we seem to have a decent ARIMA model. But, we can’t say that this is the best ARIMA model because we haven’t actually forecasted into the future and compared the forecast with the actual performance.

#So, the real validation we need now is the Out-of-Time cross-validation, discussed next.

#In Out-of-Time cross-validation, we move backwards in time and forecast into the future to as many steps we took back.
#Then we compare the forecast against the actuals.

#To do so, we will create the training and testing dataset by splitting the time series into 2 contiguous parts in a reasonable proportion
#based on time frequency of series.

from statsmodels.tsa.stattools import acf

# Create Training and Test
train = df.value[:85]
test = df.value[85:]
#fig, ax = plt.subplots()
#ax.plot(train, color= 'black', label='Trainings-Data', zorder= 2)
#ax.plot(test, color= 'blue', label='Test-Data', zorder= 2)
#plt.legend()
#plt.show()

#Now, we will build the ARIMA model on training dataset, forecast and plot it.

# Build Model
model = ARIMA(train, order=(3,2,1))
#model = ARIMA(train, order=(2, 2, 3))
fitted = model.fit()
print(fitted.summary())

# Forecast
forecast = fitted.get_forecast(119, signal_only=False)
forecast_mean = forecast.predicted_mean
alpha = 0.15
forecast_quantile = forecast.conf_int(alpha=alpha)


fig, ax = plt.subplots()
ax.plot(train, color= 'black', label='Training', zorder= 2)
ax.plot(test, color= 'blue', label='Actual', zorder= 2)
ax.plot(forecast_mean, color= 'green', label='Expected Value', zorder=2)
#ax.plot(forecast_quantile.iloc[::,0], color='cyan', label='{}-Quantil'.format(forecast_quantile), zorder=1)
ax.plot(forecast_quantile.iloc[::,0], color='cyan', label='', zorder=1)
ax.plot(forecast_quantile.iloc[::,1], color='cyan', label='', zorder=1)
ax.fill_between(x=forecast_quantile.index,
                y1=forecast_quantile.iloc[::,0],
                y2=forecast_quantile.iloc[::,1],
                alpha=alpha,
                zorder=0)
plt.legend()
plt.show()

#From the above chart, the ARIMA(1,1,1) model seems to predict a correct forecast. The actual observed values lie within the 95% confidence band.

#But, we can see that the predicted forecasts is consistently below the actuals. That means, by adding a small constant to our forecast, the accuracy will certainly improve.

#So, in this case, we should increase the order of differencing to two (d=2) and iteratively increase p and q up to 5 to see which model gives least AIC and also look for a chart that gives closer actuals and forecasts.

#While doing this, I keep an eye on the P values of the AR and MA terms in the model summary. They should be as close to zero, ideally, less than 0.05.

#The AIC has reduced to 245 from 843 which is good. Mostly, the p-values of the X terms are less than < 0.05, which is great. So overall this model is much better.


#The commonly used accuracy metrics to judge forecasts are:

#Mean Absolute Percentage Error (MAPE)
#Mean Error (ME)
#Mean Absolute Error (MAE)
#Mean Percentage Error (MPE)
#Root Mean Squared Error (RMSE)
#Lag 1 Autocorrelation of Error (ACF1)
#Correlation between the Actual and the Forecast (corr)
#Min-Max Error (minmax)
#Typically, we will use three accuracy metrices:-

#MAPE
#Correlation and
#Min-Max Error
#can be used. The above three are percentage errors that vary between 0 and 1. That way, we can judge how good is the forecast irrespective of the scale of the series.

# Accuracy metrics
def forecast_accuracy(forecast, actual):
    mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
    me = np.mean(forecast - actual)             # ME
    mae = np.mean(np.abs(forecast - actual))    # MAE
    mpe = np.mean((forecast - actual)/actual)   # MPE
    rmse = np.mean((forecast - actual)**2)**.5  # RMSE
    corr = np.corrcoef(forecast, actual)[0,1]   # corr
    mins = np.amin(np.hstack([forecast[:,None],
                              actual[:,None]]), axis=1)
    maxs = np.amax(np.hstack([forecast[:,None],
                              actual[:,None]]), axis=1)
    minmax = 1 - np.mean(mins/maxs)             # minmax
    #acf1 = acf(fc-test)[1]                      # ACF1
    return({'mape':mape, 'me':me, 'mae': mae,
            'mpe': mpe, 'rmse':rmse,
            'corr':corr, 'minmax':minmax})

print(forecast_accuracy(forecast_mean.values, test.values))

#Around 23.22% MAPE implies the model is about 76.78% accurate in predicting the next 15 observations. Now we know how to build an ARIMA model manually.

#But, we should also know how to automate the best model selection process. So, we will discuss it next.
