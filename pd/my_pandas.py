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
        # print(df.notnull().head())
        # print(df.isnull().sum())  # find how many nulls do you have?!
        # print(df[df['Address'].isnull()])  # find all nulls data

        # df['Address'].fillna(value='Nakoja-Abad', inplace=True)  # fill null positions
        # print(df.isnull().sum())

        df.dropna(how='any', inplace=True)  # drop rows, when find any null in it
        print(df.shape)

    def string_methods(self, df):
        tmp = df['Address'].replace('Pardis', 'ShahreYar', inplace=False)
        print(tmp[:10])

        tmp = df['Address'].str.lower()
        print(tmp.head(10))

    def rename_columns(self, df):
        tmp = df.copy()
        tmp.rename(
            columns={
                'Address': 'add',
                'Price': 'Gheymat'
            },
            inplace=True
        )
        print(df.head())
        print(tmp.head())

        tmp.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        print(tmp.head())

    def data_type(self, df):
        # print(df.dtypes)  # strings in DataFrame are object! such as String Class in JAVA <3

        # df['Room'] = df['Room'].astype(float)  # int to float
        # print(df.dtypes)
        # print(df.head())

        # print(df['Room'].value_counts())
        tmp = df.copy()
        # print(tmp.tail())
        tmp['Parking'] = df['Parking'].astype('category')
        # print(tmp.dtypes)
        # print(tmp['Parking'].tail().cat.codes)
        print(tmp['Parking'].cat.categories)

    def working_on_some_methods(self, df):
        print(df.shape)
        print(df.columns.tolist())
        print(df.describe())
        print(df.info())
        print(df.memory_usage(deep=True))
        print(df['Price'].max())
        print(df['Area'].min())
        print(df['Room'].mean())

        print(df['Price'].argmax())
        print(df.iloc[df['Price'].argmax()])

        print(df['Room'].value_counts())
        print(df['Room'].value_counts(dropna=False))
        print(df['Room'].value_counts(dropna=False, normalize=True))
        print(df['Room'].value_counts(dropna=False, normalize=True).index)
        print(df['Room'].value_counts(dropna=False, normalize=True).values)

        print(df['Room'].nunique())
        print(df['Room'].unique())


if __name__ == '__main__':
    numpy_obj = MyTinyNumpy()
    # numpy_obj.show_version()

    pandas_obj = MyPandas()
    # pandas_obj.show_version()
    # pandas_obj.create_dataframe()
    loaded_data = pandas_obj.load_data()
    # pandas_obj.show_loaded_data(loaded_data)
    # pandas_obj.missing_values(loaded_data)
    # pandas_obj.string_methods(loaded_data)
    # pandas_obj.rename_columns(loaded_data)
    # pandas_obj.data_type(loaded_data)
    pandas_obj.working_on_some_methods(loaded_data)
