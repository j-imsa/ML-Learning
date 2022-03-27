# https://pandas.pydata.org/
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# Latest version: 1.4.1

import pandas as pd


class MyPandas():
    def __init__(self):
        pass

    def show_pandas_version(self):
        print(pd.__version__)


if __name__ == '__main__':
    obj = MyPandas()
    obj.show_pandas_version()
