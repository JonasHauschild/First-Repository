import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
from scipy.stats import norm


# Einfluss von exogenen Faktoren (US Treasury Index als Benchmark für stabile Zinssätze (FVX) &
# Deutscher Aktienindes (GDAXI)) auf das Risiko eines Aktienportfolios

data = pd.read_excel('./Price_Data.xlsx',sheet_name= 'Historical_Prices')

data['Date'] = pd.to_datetime(data['Date'], format= '%d-%m-%y')

data = data.sort_values(['Date'], ascending = [True])

a = dict(data.dtypes)
# Erstellt ein Dictionary welches zeigt, welchen Datentyp die Werte in den einzelnen Spalten des Dataframes haben

returns= data[[value for value in dict(data.dtypes) if dict(data.dtypes)[value] in ['float64','int64']]].pct_change()
# Für diejenigen Werte des Dataframes welche Zahlen sind, wird die prozentuale Veränderung zur vorherigen Zeile berechnet

returns = returns[1:]
# Da die erste Zeile des Dataframes Returns keine Werte enthält, wird diese gelöscht

returns['Intercept'] = 1
# Y-Achsenabschnitt

hilfsliste = list()

for key in a.keys():
    hilfsliste.append(key)
stockNames = hilfsliste[1:11]
factorNames = hilfsliste[11:]
factorNames.append('Intercept')
# Aufteilen der Inhalte des Dataframes in Aktien- und Faktorwerte

stockReturns = returns[stockNames]
#Gibt diejenigen Spalten des Dataframes zurück, welche in der Liste stockNames enthalten sind

factorReturns = returns[factorNames]
#Gibt diejenigen Spalten des Dataframes zurück, welche in der Liste factorNames enthalten sind

weights = np.array([1/len(stockNames)]*len(stockNames))
# Portfoliogewichtung einzelner Aktien, Annahme: Gleichverteilung alles Aktien

CoVarMatrixStocks = stockReturns.cov()

historicalTotalRisk = np.dot(np.dot(weights,CoVarMatrixStocks),weights.T)
# Summenprodukt des Geichtungsvektors mit der Kovarianzmatrix und dem transponierten Gewichtungsvektor

print('%.4f'% (historicalTotalRisk*100),'%')

xData = factorReturns

modelCoeffs = []

for eachStock in stockNames:
    yData = stockReturns[eachStock]
    model = sm.OLS(yData,xData)             # Ordinary least square Methode da Linearität zwischen x und y vorausgesetzt
    result = model.fit()                    # TBD
    factorCoeffs = result.params            # Berechnung der Faktor Koeffizienten
    modelCoeffRow = list(factorCoeffs)      # Überführung der Faktor Koeffizienten in eine Liste
    residuals = result.resid                # Berechnung der Störterme pro Timebucket
    standard = np.std(residuals,ddof = 1)   # Berechnung der Standardabweichung aller Störterme # ddof = The divisor used in calculation of the variance is n - ddof (Bessels Correction = n-1)
    modelCoeffRow.append(standard)          # Überführung der Standardabweichung der Störterme in die Liste
    modelCoeffs.append(modelCoeffRow)       # Überführung der Aktienspezifischen Liste in eine übergreifende Liste
    #print(result.summary())

modelCoeffs = pd.DataFrame(modelCoeffs)
# Liste mit Listen als Dataframe darstellen

modelCoeffs.columns = ['B_FVX', 'B_GDAXI', 'Alpha', 'ResidVol']

modelCoeffs['Names'] = stockNames
# Spalte mit den dazugehörigen Namen der Aktien einfügen

CoVarMatrixFactor = factorReturns[['FVX', 'GDAXI']].cov()

CoVarReconstructed = np.dot(np.dot(modelCoeffs[['B_FVX', 'B_GDAXI']], CoVarMatrixFactor), modelCoeffs[['B_FVX', 'B_GDAXI']].T)

systematicRisk = np.dot(np.dot(weights,CoVarReconstructed),weights.T)

idiosyncraticRisk = sum(modelCoeffs['ResidVol']*modelCoeffs['ResidVol']*weights*weights)

factorModelTotalRisk = systematicRisk + idiosyncraticRisk

print(factorModelTotalRisk)

#Scenario calculation


fvxScenarios = np.arange(min(returns['FVX']),max(returns['FVX']),0.05)
# np.arange gibt gleichmäßig verteilte Werte innerhalb eines bestimmten Intervalls zurück - Step Size 0.05
# Intervall ist hier von min return bis max return insgesamt 27 Werte bzw. Veränderungen (Szenarien)

gdaxiScenarios = np.arange(min(returns['GDAXI']),max(returns['GDAXI']),0.02)
# Szenarien für DAX - step size 0.02

scenarios = [] # Ab hier nochmal gucken

for oneFVXValue in fvxScenarios:
    for oneGDAXIValue in gdaxiScenarios:
        oneScenario = [oneFVXValue, oneGDAXIValue]
        for oneStockName in stockNames:
            alpha = float(modelCoeffs[modelCoeffs['Names'] == oneStockName]['Alpha'])
            beta_gdaxi = float(modelCoeffs[modelCoeffs['Names'] == oneStockName]['B_GDAXI'])
            beta_fvx = float(modelCoeffs[modelCoeffs['Names'] == oneStockName]['B_FVX'])
            oneStockPredictedReturn = alpha + beta_gdaxi * oneGDAXIValue + beta_fvx * oneFVXValue
            oneScenario.append(oneStockPredictedReturn)
        scenarios.append(oneScenario)

scenarios = pd.DataFrame(scenarios)

scenarios.columns = ['FVX', 'GDAXI', 'Apple', 'ADBE', 'CVX', 'GOOG', 'IBM', 'MDLZ', 'MSFT', 'NFLX', 'ORCL', 'SBUX']

CoVarMatrixScenarios = scenarios[stockNames].cov()

scenariosTotalRisk = np.dot(np.dot(weights,CoVarMatrixScenarios),weights.T)

print(scenariosTotalRisk)

def calculateVaR(risk,confLevel,principal=1,numMonths=1):   #risk = Portfolio Varian
    vol = math.sqrt(risk)
    return abs(principal*norm.ppf(1-confLevel,0,1)*vol*math.sqrt(numMonths))    # Norm.ppf calculates the z score mean = 0 std = 1

print(calculateVaR(scenariosTotalRisk,0.99))
# Ergebniss sagt: Probability, that we wil experience a loss of X% or greater is 1%
# Ergebniss sagt: In 1 out of 100 trading periods we can expect to loose x% or worse.
print(calculateVaR(historicalTotalRisk,0.99))

print(calculateVaR(factorModelTotalRisk,0.99))


