# https://pandas.pydata.org/
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# https://pypi.org/project/pandas/
# Latest version: 1.4.1
# pip install pandas
# pip install pandas==1.4.1
# Pandas = Panel + Data ?

import numpy as np
import pandas as pd


class MyTinyNumpy():
    def __init__(self):
        print(f'NumPy Current Running Version: {np.__version__}')


class MyPandas():
    def __init__(self):
        pass

    def show_pandas_version(self):
        print(f'Pandas Current Running Version: {pd.__version__}')

    def do_it(self):
        df = pd.DataFrame([1, 2, 3, 'jimsa', True, np.nan])
        print(df)


if __name__ == '__main__':
    numpy_obj = MyTinyNumpy()
    pandas_obj = MyPandas()
    pandas_obj.show_pandas_version()
    pandas_obj.do_it()
