from Business.DataAdapter.DataAdapterCSV import DataAdapterCSV
from Business.Service.ServiceStatisticTools import ServiceStatisticTools
from Business.Service.ServiceModellSarimax import ServiceModellSarimax
import pandas as pd

if __name__=='__main__':
    print('I run the script')
    _adapter = DataAdapterCSV(filepath=r'C:\Users\jhaus\PycharmProjects\Business\Test-Data\Zeitreihen - manipuliert.csv', date_cols=[])
    _data = _adapter.get_data()

    # Statistische Tests
    _stats = ServiceStatisticTools(data = _data, testnames=['ACF', 'ADF'], xcol='Hist_Date', ycol='Amount_EUR')
    _stats.run()
    print('x')

    # Modellierung
    _model = ServiceModellSarimax(data=_data, xcol='Hist_Date', ycol='Amount_EUR')
    _model.run()


