import numpy as np
import pandas as pd


class MyTinyNumpy:
    def __init__(self):
        self.message = f'NumPy Current Running Version: {np.__version__}'

    def show_version(self):
        print(self.message)


class MyPandas:
    def __init__(self):
        self.message = f'Pandas Current Running Version: {pd.__version__}'

    def show_version(self):
        print(self.message)

    def create_dataframe(self):
        self.message = f'DataFrame Creation'
        df = pd.DataFrame([1, 2, 3, 'jimsa', True, np.nan])
        df = pd.DataFrame([1, 2, 3, 'jimsa', True, np.nan], [np.nan, False, 'jimsa', 3, 2, 1])
        df = pd.DataFrame([[1, 2, 3, 'jimsa', True, np.nan], [np.nan, False, 'jimsa', 3, 2, 1]])
        df = pd.DataFrame([[1, 2, 3, 'jimsa'], [np.nan, False, 'jimsa', 3, 2, 1]])
        df = pd.DataFrame(
            {
                'id': ['a', 'b', 'c'],
                'data': ['a1', 'b1', 'c1'],
            },
            index=[1, 2, 3]
        )
        print(df)


if __name__ == '__main__':
    numpy_obj = MyTinyNumpy()
    numpy_obj.show_version()

    pandas_obj = MyPandas()
    pandas_obj.show_version()
    pandas_obj.create_dataframe()
