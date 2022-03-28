import os
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

    @staticmethod
    def load_data():
        # df = pd.read_...
        absolute_dataset_path = os.path.abspath('pd/HousePrice.csv')
        df = pd.read_csv(absolute_dataset_path)
        return df

    @staticmethod
    def show_loaded_data(df):
        # print(df.head())
        # print(df.head(10))
        # print(df[:10]) # based on python

        # print(df.tail())

        # print(df.Area)
        # print(df['Area'])

        """
        https://www.tgju.org/profile/price_cad
        """
        tmp = df.copy()
        tmp['Price(CAD)'] = tmp['Price'] * 212400
        # print(tmp.head())

        # print(tmp.shape)

        print(tmp.describe())  # describe all numerical values

    def missing_values(self, df):
        pass


if __name__ == '__main__':
    numpy_obj = MyTinyNumpy()
    # numpy_obj.show_version()

    pandas_obj = MyPandas()
    # pandas_obj.show_version()
    # pandas_obj.create_dataframe()
    loaded_data = pandas_obj.load_data()
    # pandas_obj.show_loaded_data(loaded_data)
    pandas_obj.missing_values(loaded_data)
