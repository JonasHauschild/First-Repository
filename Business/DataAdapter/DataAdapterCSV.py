import os
import pandas as pd

from DataRepository.AbstractDataRepository import AbstractDataRepository
from Settings import Settings

class DataAdatpterCsv(AbstractDataRepository):
    def __init__(self,
                 filepath: str = 'None',
                 date_cols: list = None):
        if date_cols is None:
            date_cols = []
            self.filepath = filepath
            self.date_cols = date_cols

    def _get_data(self):
        _full_path = os.path.join(Settings.dir_root, self.filepath)
        _file_name = os.path.basename(_full_path)
        _path_name = os.path.dirname(_full_path)
        print('I read the data in {] from {}!'.format(_file_name, _path_name))

        df = pd.read_csv(_full_path,
                         decimal=',',
                         delimiter=';',
                         thousands='.',
                         parse_dates=self.date_cols,
                         dayfirst=True)
        return df
