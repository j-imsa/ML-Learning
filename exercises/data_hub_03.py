import os
import time
from os import listdir

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


def python_assignment_03_q4(df):
    """
    I believe the best approach is to:
    1. Read documentation regarding iteration algorithms used in libraries.
    2. Avoiding the usage of libraries since they have certain side effects, such as requiring resources to be loaded.
    3. Use of Python low-level structures to implement the iteration mechanism
    """

    tic = time.perf_counter()
    df_dict = df.to_dict()
    for key, val in df_dict.items():
        tmp = f'{key} -> {val}'
    toc = time.perf_counter()
    print(f'Finished in {toc - tic:0.4f} seconds by Dict')

    tic = time.perf_counter()
    for key, val in df.iterrows():
        tmp = f'{key} -> {val}'
    toc = time.perf_counter()
    print(f'Finished in {toc - tic:0.4f} seconds by DataFrame')

    # My output:
    # Finished in 0.0578 seconds by Dict
    # Finished in 3.6781 seconds by DataFrame


from numpy import array


def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence) - 1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


def my_spliter(df, n):
    lstX, lstY = [], []


def python_assignment_03_q5():
    # define input sequence
    raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    a, b = split_sequence(raw_seq, 8)
    print(a)
    print(b)

    """The split sequence_function divides a 1D-list to the first, a 2D-list into n groups, and then removes n count 
    items from the first of the 1D-list. For the DataFrame, I'll return a list of dataframes grouped by n, 
    and a dataframe with no n first element. """

    df = pd.DataFrame([
        [1, 2, 3],
        ['a', 'b', 'c'],
        ['الف', 'ب', 'ج']
    ])
    x, y = my_spliter(df, 2)
    print(x)
    print(y)


def python_assignment_03_q6():
    path = '/tmp'
    excel_files = []
    for i in listdir(path):
        if i[-4:] == 'xlsx':
            excel_files.append(path + os.path.sep + i)

    df = pd.DataFrame()
    for file in excel_files:
        tmp = pd.read_excel(file, sheet_name='PolicyData')
        print(tmp.shape)
        df = pd.concat([df, tmp])

    print(df.head())
    print(df.shape)


def python_assignment_03_q7():
    path = '/tmp/sampledatainsurance.xlsx'
    df = pd.read_excel(path, sheet_name='PolicyData')

    for i in range(5):
        tmp = df.sample(frac=0.2)  # where did you say 'without repetition'? :)
        tmp.to_excel(f'/tmp/test/tmp{i + 1}.xlsx')

    print('ok...')


def python_assignment_03_q8():
    print('This question reminds me of an experience! How? Typically, I utilise CSV or other simple file formats, '
          'and if I am confronted with an IO issue, I will inquire and conduct research on best practises, '
          'benchmarks, and so on.')
    print('Also, I discovered the \'feather\' format to be a great choice for storing data because it has a fast I/O '
          'speed, doesn\'t take up too much disc space, and doesn\'t require any unpacking when loaded back into RAM.')


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

    # python_assignment_03_q3(df)
    # python_assignment_03_q4(df)
    # python_assignment_03_q5()
    # python_assignment_03_q6()
    # python_assignment_03_q7()
    python_assignment_03_q8()
    # python_assignment_03_q9()
    # python_assignment_03_q10()
