"""
dataframe에 현재 시간을 기준으로 한 column을 추가합니다.
"""
import pandas as pd


def add_datetime_col(df):
    df['created_at'] = pd.to_datetime('now')
    return df
