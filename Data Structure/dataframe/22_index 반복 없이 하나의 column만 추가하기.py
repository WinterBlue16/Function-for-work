"""
csv 파일을 dataframe으로 불러올 때, 원래 있던 column 외 index column이 따로 생기기 때문에, index column이 중복되곤 합니다. 
index column을 하나로 두기 위한 방법입니다.
"""
import pandas as pd


def remove_duplicated_idx(df, idx_col_name):
    df[idx_col_name] = df.index
    return df


def remove_duplicated_idx_2(df):
    df.reset_index(level=0, inplace=True)
    return df
