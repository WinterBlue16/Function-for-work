import pandas as pd


def save_dataframe_to_csv(df):
    df.to_csv('저장할 파일명.csv', index=0)
