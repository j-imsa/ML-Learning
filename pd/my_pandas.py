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
        self.absolute_dataset_path = os.path.abspath('pd/HousePrice.csv')
        self.absolute_dataset_path = \
            self.absolute_dataset_path[:(len(self.absolute_dataset_path) - len('HousePrice.csv'))]

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

    def load_data(self):
        # df = pd.read_...
        # absolute_dataset_path = os.path.abspath('pd/HousePrice.csv')
        df = pd.read_csv(self.absolute_dataset_path + 'HousePrice.csv')
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

    def apply_method(self, num):
        return num + 10

    def working_on_some_methods(self, df):
        # print(df.shape)
        # print(df.columns.tolist())
        # print(df.describe())
        # print(df.info())
        # print(df.memory_usage(deep=True))
        # print(df['Price'].max())
        # print(df['Area'].min())
        # print(df['Room'].mean())

        # print(df['Price'].argmax())
        # print(df.iloc[df['Price'].argmax()])
        # print(df.iloc[[df['Price'].argmax(), df['Price'].argmin()]])
        # print(df.iloc[[df['Price'].argmax(), df['Price'].argmin()]].sort_values('Room', ascending=True))
        # print(df.iloc[[df['Price'].argmax(), df['Price'].argmin()]].sort_values('Room', ascending=False))
        # print(df.loc[df['Price'].argmax(), 'Room'])
        # print(df.at[df['Price'].argmax(), 'Room'])

        # print(df['Room'].value_counts())
        # print(df['Room'].value_counts(dropna=False))
        # print(df['Room'].value_counts(dropna=False, normalize=True))
        # print(df['Room'].value_counts(dropna=False, normalize=True).index)
        # print(df['Room'].value_counts(dropna=False, normalize=True).values)

        # print(df['Room'].nunique())
        # print(df['Room'].unique())

        # print(df[df['Room'] > 4])
        # print(df[(df['Room'] > 4) & (df['Price'] < 300000000)])
        # print(df[df['Room'].isin([0, 5])])
        # print(df[df['Room'].isin([0, 5])]['Area'])

        # print(df.groupby('Address').Room.mean())
        # print(df.groupby('Address').Room.min())
        # print(df.groupby('Address').Room.max())
        # print(df.groupby('Address')['Room'].agg(['count', 'max', 'min', 'mean']))
        # print(df.groupby('Address').mean())

        # MatPlotLib
        # df.groupby('Address').mean().plot(kind='bar')

        # for index, row in df.iterrows():
        #     print(f'{index} -> {row.Room}')

        # print(df[['Room', 'Price']].head())
        # print(df.drop(['Room', 'Parking'], axis=1, inplace=False).head())  # axis 1 for columns
        # print(df.drop([2, 3, 4], axis=0, inplace=False).head())  # axis 0 for rows

        # df.to_csv(self.absolute_dataset_path + 'df.csv', header=True, index=False)
        # df.to_excel(self.absolute_dataset_path + 'df.xlsx', header=True,
        #             index=False)  # needs to install openpyxl module
        # df.to_pickle(self.absolute_dataset_path + 'df.pkl')

        # print(df.sample(5))
        # print(df.sample(n=5, random_state=20))
        # print(df.sample(frac=0.05, random_state=20))

        # print(df.Parking.unique())
        # print(df.Parking.map({True: 'TT', False: 'FF'}).head(20))
        # print(pd.get_dummies(df.Parking))

        # print(df.duplicated().sum())
        # print(df.duplicated().count())
        # print(df[df.duplicated()])
        # print(df.iloc[[54, 55]])
        # tmp = df.drop_duplicates()
        # print(tmp.iloc[[54, 55]])

        df['new_val'] = df.Room.apply(self.apply_method)
        print(df.head())

        df['np_val'] = np.where(df.Parking, 'Parking Darad!', 'Parking Nadarad!')
        print(df.head(20))

    def working_on_indexes(self, df):
        print(df.index)

        df.index += 1
        print(df.index)
        print(df.head())
        print(df['Price'].argmax())
        print(df.iloc[df['Price'].argmax()])

        df.index.name = 'index'
        print(df.head())

    def working_on_samples(self, df):
        pass


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
    # pandas_obj.working_on_some_methods(loaded_data)
    # pandas_obj.working_on_indexes(loaded_data)
    pandas_obj.working_on_samples(loaded_data)
