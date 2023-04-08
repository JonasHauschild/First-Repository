from DataAdapter.DataAdapterCSV import DataAdapterCSV
from Service.ServiceStatisticTools import ServiceStatisticTools
from Service.ServiceModellSarimax import ServiceModellSarimax

if __name__=='__main__':
    print('I run the script')
    _adapter = DataAdapterCSV(filepath='Test-Data\\Zeitreihen - manipuliert.csv', date_cols = [])
    _data = _adapter.get_data()

    # Statistische Tests
    _stats = ServiceStatisticTools(data = _data, testnames=['ACF', 'ADF'], xcol='Hist_Date', ycol='Amount_EUR')
    _stats.run()

    # Modellierung
    _model = ServiceModellSarimax(data=_data, xcol='Hist_Date', ycol='Amount_EUR')
    _model.run()


