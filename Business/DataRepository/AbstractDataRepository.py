from abc import ABC, abstractmethod
import pandas as pd

register = []

class AbstractDataRepository(ABC):
    def __init_subclass__(cls, **kwargs):
        """
        Methode um die tatsächlichen Adapter zu registrieren.
        :param kwargs:
        :return:
        """

        super().__init_subclass__()
        register.append(cls.__name__)
        print('Ein Adapter der Klasse {} wurde erzeugt!'.format(cls.__name__))

    def __new__(cls, *args, **kwargs):
        instanz = super().__new__(cls)
        print('Eine Instanz der Adapter-Klasse {} wurde erzeugt!'.format(cls.__name__))
        return instanz

    def get_data(self, *args, **kwargs) -> pd.DataFrame:
        """
        Methode zum Laden von Daten aus einer bestimmten Datenquelle. Die Logik der Daten akquise wird hierbei im
        zugrundekiegenden Adapter implementiert.

        :param args:
        :param kwargs:
        :return:
        """
        return self._get_data(*args, **kwargs)

    @abstractmethod
    def _get_data(self, *args, **kwargs):
        raise NotImplementedError
