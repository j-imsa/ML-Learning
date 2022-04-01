import os

import numpy as np
import pandas as pd


def python_assignment_03_q1(df):
    tmp = df.copy()
    new_order_list = tmp.columns[::-1].tolist()
    print(tmp[new_order_list].head())


def python_assignment_03_q2(df):
    # print(df.head())
    # df.columns = ['col1', 'col2', 'col3', 'col4']
    # print(df.head())
    # df.col1 = df.col1.astype('category')
    # print(df.dtypes)
    # print(df.col1)
    # print(pd.get_dummies(df.col1))
    # print(pd.get_dummies(['a', 'a', 'b', 'ab']))

    for col in df.columns:
        tmp = df[col]
        for index, row in tmp.iteritems():
            print(row)


def python_assignment_03_q3(df):
    print(df.tail())
    tmp = df.iloc[::-1]
    tmp.reset_index(drop=True, inplace=True)
    # print(tmp.index)
    print(tmp.head())


if __name__ == '__main__':
    # df = pd.read_csv('../pd/HousePrice.csv')
    # os.system(
    #     'wget -c https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020'
    #     '-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-size'
    #     '-bands-csv.csv -O sample-data.csv')
    df = pd.read_csv('sample-data.csv')
    # python_assignment_03_q1(df)

    # df = pd.DataFrame([['aab', 'a', 'a', 'b'],
    #                    ['ear', 'e', 'a', 'r'],
    #                    ['bb', 'b', 'b']])
    # python_assignment_03_q2(df)

    python_assignment_03_q3(df)
    # python_assignment_03_q4()
    # python_assignment_03_q5()
    # python_assignment_03_q6()
    # python_assignment_03_q7()
    # python_assignment_03_q8()
    # python_assignment_03_q9()
    # python_assignment_03_q10()
